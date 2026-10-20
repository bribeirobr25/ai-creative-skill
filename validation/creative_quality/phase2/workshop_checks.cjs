/* Task-specific observed probes, composed by the existing browser collector. */
module.exports=async({page,width,check,shot})=>{
 const checks=[];
 const visual=await page.evaluate(()=>{
  const box=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height}};
  const map=document.querySelector('.learning-map'),cta=document.querySelector('#primary-cta');
  let opacity=1;for(let e=map;e;e=e.parentElement)opacity*=Number(getComputedStyle(e).opacity);
  const mb=map.getBoundingClientRect();
  const labels=[...map.querySelectorAll('figcaption,li,img')];
  const contentFits=labels.every(e=>{let r=e.getBoundingClientRect();return r.width>0&&r.height>0&&r.left>=mb.left-1&&r.right<=mb.right+1&&r.top>=mb.top-1&&r.bottom<=mb.bottom+1;});
  const rgb=s=>{const a=s.match(/[\d.]+/g)?.map(Number);return a&&a.length>=3&&(!a[3]||a[3]===1)?a.slice(0,3):null};
  const lum=c=>c.map(x=>{x/=255;return x<=.04045?x/12.92:((x+.055)/1.055)**2.4}).reduce((n,x,i)=>n+x*[.2126,.7152,.0722][i],0);
  const ratios=[];
  for(const e of document.querySelectorAll('h1,.intro,.truth,.primary,figcaption,.learning-map li,.cards h3,.plan')){
   let bg=null;for(let p=e;p&&!bg;p=p.parentElement){const s=getComputedStyle(p).backgroundColor;if(s!=='rgba(0, 0, 0, 0)'&&s!=='transparent')bg=rgb(s);}
   const fg=rgb(getComputedStyle(e).color);if(!bg||!fg)throw Error('Unsupported contrast color');
   const a=lum(fg),b=lum(bg);ratios.push((Math.max(a,b)+.05)/(Math.min(a,b)+.05));
  }
  const cb=cta.getBoundingClientRect();const headline=document.querySelector('h1');
  return {opacity,contentFits,contrastMin:Math.min(...ratios),contrastSamples:ratios.length,cta:box(cta),map:box(map),headlineFits:headline.scrollWidth<=headline.clientWidth,ctaWithinInitialViewport:cb.top>=0&&cb.bottom<=innerHeight,externalActions:[...document.querySelectorAll('a[href],form[action]')].filter(e=>/^(https?:|mailto:)/.test(e.getAttribute('href')||e.getAttribute('action')||'')).length};
 });
 checks.push(check('learning-path-visible','effective opacity > 0',visual.opacity,visual.opacity>0));
 checks.push(check('learning-path-content-fits',true,visual.contentFits,visual.contentFits));
 checks.push(check('headline-fits',true,visual.headlineFits,visual.headlineFits));
 checks.push(check('primary-action-in-initial-viewport',true,visual.ctaWithinInitialViewport,visual.ctaWithinInitialViewport));
 checks.push(check('sampled-text-contrast','>= 4.5 selected solid-color pairs',Number(visual.contrastMin.toFixed(3)),visual.contrastMin>=4.5));
 checks.push(check('no-external-actions',0,visual.externalActions,visual.externalActions===0));
 await page.locator('#primary-cta').focus();
 const focus=await page.locator('#primary-cta').evaluate(e=>({style:getComputedStyle(e).outlineStyle,width:parseFloat(getComputedStyle(e).outlineWidth)}));
 checks.push(check('keyboard-focus-visible',true,focus.style!=='none'&&focus.width>0,focus.style!=='none'&&focus.width>0));
 await page.keyboard.press('Enter');await page.waitForTimeout(800);
 checks.push(check('primary-navigation','#oficinas',new URL(page.url()).hash,new URL(page.url()).hash==='#oficinas'));
 await page.locator('[data-filter="tecnologia"]').focus();await page.keyboard.press('Enter');
 const count=await page.locator('.cards article:visible').count();checks.push(check('filter',1,count,count===1));
 await page.locator('[data-filter="all"]').click();
 const opener=page.locator('.plan').first();await opener.focus();await page.keyboard.press('Enter');
 checks.push(check('dialog-open',true,await page.locator('dialog').evaluate(d=>d.open),await page.locator('dialog').evaluate(d=>d.open)));
 const initial=await page.locator('#hours').evaluate(e=>e===document.activeElement);checks.push(check('dialog-initial-focus',true,initial,initial));
 await page.locator('#hours').fill('2');await page.locator('#plan-form button').click();
 const result=await page.locator('#result').innerText();checks.push(check('local-calculation','Seu plano: 3 semanas, com até 2 horas por semana.',result,result==='Seu plano: 3 semanas, com até 2 horas por semana.'));
 await shot('interaction');
 await page.locator('#hours').fill('0');await page.locator('#plan-form button').click();
 const invalid=await page.locator('#hours').getAttribute('aria-invalid')==='true'&&await page.locator('#error').isVisible();checks.push(check('invalid-input',true,invalid,invalid));
 await page.locator('.close').focus();await page.keyboard.press('Shift+Tab');
 const wrap=await page.locator('#plan-form button').evaluate(e=>e===document.activeElement);checks.push(check('dialog-focus-wrap',true,wrap,wrap));
 await page.keyboard.press('Escape');const restored=await opener.evaluate(e=>e===document.activeElement);checks.push(check('escape-restores-focus',true,restored,restored));
 return {checks,visual};
};
