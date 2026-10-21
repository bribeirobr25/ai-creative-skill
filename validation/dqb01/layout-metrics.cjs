const {chromium}=require('playwright'),fs=require('fs');
const [base,out,...variants]=process.argv.slice(2);
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_EXECUTABLE?{executablePath:process.env.CHROMIUM_EXECUTABLE}:{})});const result=[];
for(const variant of variants)for(const width of [1440,390]){
 const context=await browser.newContext({viewport:{width,height:width===1440?900:844},reducedMotion:'reduce'});const p=await context.newPage();
 const box=async l=>l.evaluate(e=>{const r=e.getBoundingClientRect(),s=getComputedStyle(e);return {x:r.x,y:r.y,width:r.width,height:r.height,bottom:r.bottom,font:s.fontFamily,fontSize:s.fontSize,fontWeight:s.fontWeight}});
 await p.goto(base+'/'+variant+'/',{waitUntil:'networkidle'});
 const home={headline:await box(p.locator('h1')),primaryAction:await box(p.getByRole('link',{name:/Explorar coleção/}).first()),pageHeight:await p.evaluate(()=>document.documentElement.scrollHeight)};
 await p.goto(base+'/'+variant+'/#/colecao',{waitUntil:'networkidle'});await p.waitForTimeout(100);
 const catalog={arcoPrice:await box(p.getByText('€180',{exact:true}).first()),pageHeight:await p.evaluate(()=>document.documentElement.scrollHeight)};
 await p.goto(base+'/'+variant+'/#/produto/arco',{waitUntil:'networkidle'});await p.waitForTimeout(100);
 const product={name:await box(p.getByRole('heading',{name:'Arco',exact:true})),primaryAction:await box(p.getByTestId('add-cart')),pageHeight:await p.evaluate(()=>document.documentElement.scrollHeight)};
 result.push({variant,width,home,catalog,product});await context.close();
}await browser.close();fs.writeFileSync(out,JSON.stringify({scope:'layout observations, not universal quality thresholds',result},null,2));console.log(JSON.stringify(result.map(x=>({variant:x.variant,width:x.width,productCTA:x.product.primaryAction.y,catalogPrice:x.catalog.arcoPrice.y})),null,2));})();
