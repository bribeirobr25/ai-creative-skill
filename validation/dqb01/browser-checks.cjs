// Bounded research adapter: actual local interactions, not aesthetic scoring.
const {chromium}=require('playwright');
const fs=require('fs'), path=require('path'), crypto=require('crypto');
const [baseUrl,outDir,...variants]=process.argv.slice(2);
if(!baseUrl||!outDir||!variants.length) throw Error('baseUrl outDir A/r0 B/r0 ... required');
fs.mkdirSync(outDir,{recursive:true});
const browserOptions={headless:true};
if(process.env.CHROMIUM_EXECUTABLE)browserOptions.executablePath=process.env.CHROMIUM_EXECUTABLE;
const normalized=s=>s.replace(/\s+/g,' ').trim();
const money=s=>Number((s.match(/\d[\d.,]*/)||['NaN'])[0].replace(/,/g,'.'));
(async()=>{
 const browser=await chromium.launch(browserOptions);let rows=[];
 for(const variant of variants)for(const viewport of [{width:1440,height:900},{width:390,height:844}]){
  const id=variant.replace('/','-')+'-'+viewport.width;
  const context=await browser.newContext({viewport,deviceScaleFactor:1,reducedMotion:'reduce'});
  const page=await context.newPage(), checks=[], errors=[], external=[], failedRequests=[];
  const url=baseUrl.replace(/\/$/,'')+'/'+variant+'/';
  await page.route('**/*',route=>{let u=route.request().url();if(u.startsWith(baseUrl)||u.startsWith('data:')||u.startsWith('blob:'))return route.continue();external.push(u);return route.abort();});
  page.on('pageerror',e=>errors.push(e.message));
  page.on('response',r=>{if(r.status()>=400)failedRequests.push({url:r.url(),status:r.status()})});
  const el=id=>page.locator('[data-testid="'+id+'"]:visible').first();
  const check=async(id,fn)=>{try{const detail=await fn();if(detail===false)throw Error('condition false');checks.push({id,pass:true,detail});}catch(e){checks.push({id,pass:false,error:e.message.slice(0,450)})}};
  const settle=async()=>{await page.waitForTimeout(200);await page.evaluate(()=>document.fonts.ready)};
  const shot=async(state,fullPage=false)=>{await settle();const file=id+'-'+state+'.jpg';await page.screenshot({path:path.join(outDir,file),type:'jpeg',quality:90,fullPage,animations:'disabled'});return file};
  const captures=[];
  await check('load-home',async()=>{const r=await page.goto(url,{waitUntil:'networkidle'});return r.ok()});
  captures.push(await shot('home'));captures.push(await shot('home-full',true));
  await check('home-content',async()=>{let t=normalized(await page.locator('body').innerText());return t.includes('Para levar o que importa.')&&t.includes('NOMA')&&t.includes('Menos excesso. Mais presença.')});
  await check('home-disclosure',async()=>/Protótipo demonstrativo/.test(await page.locator('body').innerText()));
  const layout=async(label)=>{
   await check(label+'-no-overflow',()=>page.evaluate(()=>({viewport:innerWidth,scroll:document.documentElement.scrollWidth})).then(x=>x.scroll<=x.viewport+1?x:false));
   await check(label+'-images',()=>page.locator('img:visible').evaluateAll(xs=>xs.length>0&&xs.every(x=>x.complete&&x.naturalWidth>0)));
  };
  await layout('home');
  await check('catalog-navigation',async()=>{await el('nav-catalog').click();await settle();return await el('product-arco').isVisible()&&await el('product-trama').isVisible()});
  captures.push(await shot('catalog',true));await layout('catalog');
  await check('budget-filter',async()=>{await el('filter-budget').click();await settle();return await el('product-arco').isVisible()&&!await el('product-trama').isVisible()});
  await check('reset-filter',async()=>{await el('filter-all').click();await settle();return await el('product-arco').isVisible()&&await el('product-trama').isVisible()});
  await check('arco-detail',async()=>{await el('product-arco').click();await settle();const t=await page.locator('body').innerText();return /24\s*[×x]\s*17\s*[×x]\s*8/.test(t)&&t.includes('Caramelo')&&await el('add-cart').isVisible()});
  captures.push(await shot('product',true));await layout('product');
  await check('add-and-cart',async()=>{await el('add-cart').click();await el('nav-cart').click();await settle();return await el('cart-quantity').isVisible()&&money(await el('cart-subtotal').innerText())===180});
  captures.push(await shot('cart-one',true));
  async function quantity(n){let e=el('cart-quantity');if(await e.evaluate(x=>x.tagName)==='SELECT')await e.selectOption(String(n));else{await e.fill(String(n));await e.dispatchEvent('change');await e.blur();}await settle();}
  await check('quantity-two-subtotal',async()=>{await quantity(2);return money(await el('cart-subtotal').innerText())===360});
  captures.push(await shot('cart-two',true));await layout('cart');
  await check('quantity-limits',async()=>{const e=el('cart-quantity');if(await e.evaluate(x=>x.tagName)==='SELECT')return e.evaluate(x=>[...x.options].every(o=>+o.value>=1&&+o.value<=9));await quantity(0);let subtotal=money(await el('cart-subtotal').innerText());const state=await e.evaluate(x=>({value:+x.value,invalid:!x.checkValidity()}));return subtotal>=180&&Number.isFinite(subtotal)&&((state.value>=1&&state.value<=9)||state.invalid)});
  await check('remove-and-empty',async()=>{await el('cart-remove').click();await settle();return await el('cart-empty').isVisible()&&!await el('cart-quantity').isVisible()});
  captures.push(await shot('cart-empty',true));
  await check('cart-disclosure',async()=>/Protótipo demonstrativo/.test(await page.locator('body').innerText()));
  await check('return-home',async()=>{await el('nav-home').click();await settle();return /Para levar o que importa\./.test(normalized(await page.locator('body').innerText()))});
  await check('keyboard-navigation',async()=>{let e=el('nav-catalog');await e.focus();await page.keyboard.press('Enter');await settle();return await el('product-arco').isVisible()});
  await check('no-script-errors',()=>errors.length===0);
  await check('no-external-requests',()=>external.length===0);
  await check('no-failed-resources',()=>failedRequests.length===0);
  const row={variant,viewport,checks,captures,errors,external,failedRequests};rows.push(row);
  fs.writeFileSync(path.join(outDir,'results.json'),JSON.stringify({scope:'functional_and_rendered_evidence_not_design_rating',rows},null,2));
  await context.close();
 }
 const smokes=[];
 for(const variant of variants)for(const width of [320,768]){
  const context=await browser.newContext({viewport:{width,height:width===320?740:1024},reducedMotion:'reduce'});const page=await context.newPage();await page.goto(baseUrl+'/'+variant+'/',{waitUntil:'networkidle'});
  smokes.push({variant,width,...await page.evaluate(()=>({scrollWidth:document.documentElement.scrollWidth,noOverflow:document.documentElement.scrollWidth<=innerWidth+1}))});await context.close();
 }
 await browser.close();
 const sha256={};for(const name of fs.readdirSync(outDir).filter(x=>x.endsWith('.jpg')))sha256[name]=crypto.createHash('sha256').update(fs.readFileSync(path.join(outDir,name))).digest('hex');
 const flat=rows.flatMap(x=>x.checks),summary={scope:'functional_and_rendered_evidence_not_design_rating',runAt:new Date().toISOString(),browserVersion:browser.version(),passed:flat.filter(x=>x.pass).length,failed:flat.filter(x=>!x.pass).length,rows,smokes,sha256};
 fs.writeFileSync(path.join(outDir,'results.json'),JSON.stringify(summary,null,2));
 console.log(JSON.stringify({passed:summary.passed,failed:summary.failed,failures:rows.flatMap(r=>r.checks.filter(x=>!x.pass).map(x=>({variant:r.variant,width:r.viewport.width,...x}))),smokes},null,2));
 process.exitCode=summary.failed?1:0;
})();
