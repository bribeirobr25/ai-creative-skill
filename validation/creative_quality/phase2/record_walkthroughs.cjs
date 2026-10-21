/* Record equal silent interaction protocols from authorized loopback previews. */
const {chromium}=require('playwright'),fs=require('node:fs'),path=require('node:path'),crypto=require('node:crypto');
const [configFile,out]=process.argv.slice(2),config=JSON.parse(fs.readFileSync(configFile));
fs.mkdirSync(out,{recursive:true});
(async()=>{const browser=await chromium.launch({headless:true,executablePath:process.env.CHROMIUM_EXECUTABLE||undefined});const records=[];
try{for(const item of config.targets){const url=new URL(item.url);if(!['127.0.0.1','localhost'].includes(url.hostname))throw Error('Loopback required');for(const width of [1440,390]){
 const height=width===1440?900:844,start=Date.now();let blocked=0;
 const context=await browser.newContext({viewport:{width,height},recordVideo:{dir:out,size:{width,height}}});
 await context.route('**/*',r=>{if(new URL(r.request().url()).origin===url.origin)return r.continue();blocked++;return r.abort()});
 const p=await context.newPage(),video=p.video();await p.goto(item.url,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(2000);
 await p.locator('.hero .button').first().click();await p.waitForTimeout(1500);
 await p.locator('[data-filter="texture"]').click();if(await p.locator('.product-card:visible').count()!==3)throw Error('Filter failed');await p.waitForTimeout(1500);
 await p.locator('[data-filter="all"]').click();await p.waitForTimeout(1000);
 const opener=p.locator('.product-image[data-product]').first();await opener.focus();await p.keyboard.press('Enter');if(!await p.locator('dialog').evaluate(d=>d.open))throw Error('Dialog failed');await p.waitForTimeout(2000);
 await p.keyboard.press('ArrowRight');await p.waitForTimeout(2000);await p.keyboard.press('ArrowLeft');await p.waitForTimeout(1000);
 await p.locator('.dialog-close').focus();await p.waitForTimeout(1000);await p.keyboard.press('Escape');if(!await opener.evaluate(e=>e===document.activeElement))throw Error('Focus restore failed');await p.waitForTimeout(1000);
 await p.evaluate(()=>scrollTo({top:0,behavior:'instant'}));if(width===390){await p.locator('.menu-toggle').click();await p.waitForTimeout(1500);await p.keyboard.press('Escape');}await p.waitForTimeout(1500);
 await context.close();const name=`${item.id}-${width}.webm`;await video.saveAs(path.join(out,name));await video.delete();if(blocked)throw Error('Unexpected external requests');
 records.push({id:item.id,width,height,file:name,sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(out,name))).digest('hex'),elapsed_ms:Date.now()-start,external_requests:blocked,protocol:'hero, primary CTA, texture filter, all, keyboard open gallery, next, previous, focus close, Escape restore, mobile menu/Escape, top'});
}}fs.writeFileSync(path.join(out,'walkthrough-manifest.json'),JSON.stringify({browser:browser.version(),records},null,2));console.log(JSON.stringify(records));}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
