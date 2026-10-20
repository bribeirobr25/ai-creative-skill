/* Local browser evidence adapter for the existing validation harness.
 * Inputs and screenshots stay outside Git. No AI provider or publication.
 * Usage: node browser_evidence.cjs private-config.json output-directory
 */
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const [configPath, output] = process.argv.slice(2);
const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
fs.mkdirSync(output, {recursive:true});
const sha = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const rows = [];
const check = (id, expected, actual, ok) => ({
  id, expected, actual, outcome:ok?'PASS':'FAIL', execution_mode:'browser_observed'
});
(async()=>{
 const browser = await chromium.launch({headless:true,executablePath:process.env.CHROMIUM_EXECUTABLE||undefined});
 try {
 for(const target of config.targets){
  const url = new URL(target.url);
  if(!['127.0.0.1','localhost','[::1]'].includes(url.hostname)) throw Error('Loopback preview required');
  for(const width of config.widths || [1440,390]){
   const context = await browser.newContext({viewport:{width,height:width>760?900:844},deviceScaleFactor:1});
   const blocked=[],errors=[],httpErrors=[];
   await context.route('**/*', route=>{
    const u=new URL(route.request().url());
    if(u.origin===url.origin || ['data:','blob:'].includes(u.protocol)) return route.continue();
    blocked.push(u.origin);return route.abort();
   });
   const page=await context.newPage();
   page.on('pageerror',e=>errors.push(String(e)));
   page.on('response',r=>{if(r.status()>=400)httpErrors.push({status:r.status(),path:new URL(r.url()).pathname});});
   await page.goto(target.url,{waitUntil:'networkidle'});
   await page.evaluate(()=>document.fonts.ready);
   // Load lazy images and trigger reveals, then return to the initial viewport.
   await page.evaluate(async()=>{
    for(let y=0;y<document.documentElement.scrollHeight;y+=600){
      scrollTo({top:y,behavior:'instant'});await new Promise(r=>setTimeout(r,150));
    }
    await Promise.all([...document.images].filter(im=>im.getClientRects().length).map(im=>im.decode().catch(()=>{})));
    scrollTo({top:0,behavior:'instant'});
   });
   await page.waitForTimeout(800);
   const metrics=await page.evaluate(()=>{
    const rect=el=>{let r=el.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height}};
    const samples=selector=>[...document.querySelectorAll(selector)].map(el=>({
      text:el.textContent.trim().slice(0,100),rect:rect(el),
      font:getComputedStyle(el).fontSize,lineHeight:getComputedStyle(el).lineHeight,
      color:getComputedStyle(el).color,background:getComputedStyle(el).backgroundColor
    }));
    return {
     viewport:{width:innerWidth,height:innerHeight},documentHeight:document.documentElement.scrollHeight,
     scrollWidth:document.documentElement.scrollWidth,
     brokenImages:[...document.images].filter(im=>im.getClientRects().length&&(!im.complete||!im.naturalWidth)).map(im=>im.getAttribute('src')),
     hiddenImagesNotTested:[...document.images].filter(im=>!im.getClientRects().length).map(im=>im.getAttribute('src')),
     headings:samples('h1,h2'),heroImage:samples('.hero-visual img'),
     images:[...document.images].map(im=>({src:im.getAttribute('src'),alt:im.alt,natural:[im.naturalWidth,im.naturalHeight],rect:rect(im),fit:getComputedStyle(im).objectFit})),
     resources:performance.getEntriesByType('resource').map(r=>({name:new URL(r.name).pathname,bytes:r.transferSize,ms:r.duration})),
     navigationMs:performance.getEntriesByType('navigation')[0]?.duration,
     primaryCTA:samples('.hero .button'),
     links:[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))
    };
   });
   const stem=`${target.id}-${width}`;
   const screenshots=[];
   async function shot(suffix,options={}){
    const name=`${stem}-${suffix}.png`;await page.screenshot({path:path.join(output,name),...options});
    screenshots.push({file:name,sha256:sha(path.join(output,name))});
   }
   await shot('hero');
   await shot('full',{fullPage:true});
   const checks=[
    check('horizontal-overflow',width,metrics.scrollWidth,metrics.scrollWidth<=width),
    check('images-loaded',[],metrics.brokenImages,metrics.brokenImages.length===0)
   ];
   if(target.minHeroHeight){
    const height=metrics.heroImage[0]?.rect.height||0;
    checks.push(check('hero-not-collapsed',`height >= ${target.minHeroHeight}px (case-specific)`,height,height>=target.minHeroHeight));
   }
   if(target.kind==='gallery'){
    await page.locator('[data-filter="texture"]').click();
    const count=await page.locator('.product-card:visible').count();
    checks.push(check('filter-count',3,count,count===3));
    await page.locator('[data-filter="all"]').click();
    const opener=page.locator('.product-image[data-product]').first();
    await opener.click();
    checks.push(check('dialog-open',true,await page.locator('dialog').evaluate(d=>d.open),await page.locator('dialog').evaluate(d=>d.open)));
    const first=await page.locator('#gallery-image').getAttribute('src');
    await page.keyboard.press('ArrowRight');
    const second=await page.locator('#gallery-image').getAttribute('src');
    checks.push(check('gallery-next','different photo',second,second!==first));
    await page.waitForTimeout(150);await shot('dialog');
    await page.locator('.dialog-close').focus();await page.keyboard.press('Shift+Tab');
    const trapped=await page.evaluate(()=>document.querySelector('dialog').contains(document.activeElement));
    checks.push(check('dialog-focus-wrap',true,trapped,trapped));
    await page.keyboard.press('Escape');
    const restored=await opener.evaluate(el=>document.activeElement===el);
    checks.push(check('dialog-escape-restores-focus',true,restored,restored));
   } else if(target.kind==='calculator'){
    await page.locator('#target').fill('100');await page.locator('#saved').fill('0');await page.locator('#months').fill('3');
    await page.locator('#goal-form button[type="submit"]').click();
    const amount=await page.locator('#result-amount').innerText();
    checks.push(check('calculation','≈ R$ 33,33',amount,amount.includes('33,33')&&amount.includes('≈')));
    await page.locator('#months').fill('0');await page.locator('#goal-form button[type="submit"]').click();
    const invalid=await page.locator('#form-error').isVisible();
    checks.push(check('invalid-term',true,invalid,invalid));
    await page.locator('#tab-choice').focus();await page.keyboard.press('ArrowRight');
    const tab=await page.locator('#tab-consequence').getAttribute('aria-selected');
    checks.push(check('tabs-keyboard','true',tab,tab==='true'));
   }
   if(target.kind==='workshop'){
    const observed=await require('./phase2/workshop_checks.cjs')({page,width,check,shot});
    checks.push(...observed.checks);metrics.workshopVisual=observed.visual;
   }
   if(width<760 && target.kind!=='workshop'){
    await page.evaluate(()=>scrollTo(0,0));
    await page.locator('.menu-toggle').click();
    checks.push(check('mobile-menu','true',await page.locator('.menu-toggle').getAttribute('aria-expanded'),await page.locator('.menu-toggle').getAttribute('aria-expanded')==='true'));
    await page.keyboard.press('Escape');
    const closed=await page.locator('.menu-toggle').getAttribute('aria-expanded');
    checks.push(check('mobile-menu-escape','false',closed,closed==='false'));
   }
   await page.emulateMedia({reducedMotion:'reduce'});
   const motion=await page.evaluate(()=>({
    scroll:getComputedStyle(document.documentElement).scrollBehavior,
    active:[...document.querySelectorAll('*')].filter(el=>{
      const s=getComputedStyle(el);return s.animationName!=='none'&&s.animationDuration.split(',').some(x=>parseFloat(x)>0);
    }).length
   }));
   checks.push(check('reduced-motion',{scroll:'auto',active:0},motion,motion.scroll==='auto'&&motion.active===0));
   checks.push(check('script-errors',[],errors,errors.length===0));
   checks.push(check('resource-errors',[],httpErrors,httpErrors.length===0));
   checks.push(check('external-network',[],blocked,blocked.length===0));
   rows.push({id:target.id,width,build_sha256:target.build_sha256,metrics,checks,screenshots});
   await context.close();
  }
 }
 fs.writeFileSync(path.join(output,'browser-evidence.json'),JSON.stringify({
  schema:'creative-quality-browser-evidence/1',time:new Date().toISOString(),
  browser:browser.version(),playwright:require('playwright/package.json').version,
  coverage:'Chromium emulation; not physical devices, full accessibility audit, conversion or human aesthetic approval.',
  production_approval:'UNVERIFIED',provider_calls:0,rows
 },null,2));
 console.log(JSON.stringify(rows.map(r=>({id:r.id,width:r.width,checks:r.checks.length,fail:r.checks.filter(c=>c.outcome==='FAIL')})),null,2));
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
