/* UI smoke only. Synthetic form data are discarded, never counted as human review. */
const {chromium}=require('playwright'),fs=require('node:fs');
(async()=>{const b=await chromium.launch({headless:true,executablePath:process.env.CHROMIUM_EXECUTABLE||undefined});const rows=[];
try{for(const packet of ['R1','R2'])for(const width of [1440,390]){
 const context=await b.newContext({viewport:{width,height:900},acceptDownloads:true});const p=await context.newPage();let external=0;await p.route('**/*',r=>{if(new URL(r.request().url()).hostname==='127.0.0.1')return r.continue();external++;return r.abort()});
 await p.goto(`http://127.0.0.1:8882/${packet}/`,{waitUntil:'networkidle'});await p.evaluate(()=>Promise.all([...document.images].map(i=>i.decode())));
 const measured=await p.evaluate(async()=>{await Promise.all([...document.querySelectorAll('video')].map(v=>new Promise((resolve,reject)=>{if(v.readyState>=1)return resolve();v.addEventListener('loadedmetadata',resolve,{once:true});v.addEventListener('error',reject,{once:true});})));return {overflow:document.documentElement.scrollWidth>innerWidth,images:[...document.images].length,videos:[...document.querySelectorAll('video')].map(v=>({width:v.videoWidth,height:v.videoHeight,duration:v.duration})),requiredFields:[...document.querySelectorAll('[required]')].length,initiallyValid:document.querySelector('form').checkValidity()};});
 if(measured.overflow||measured.images!==4||measured.videos.length!==4||measured.initiallyValid)throw Error('Review packet structure failed');
 if(width===1440&&packet==='R1'){
  await p.locator('#reviewer').fill('AUTOMATED_UI_SMOKE_NOT_A_REVIEW');await p.locator('#context').fill('Synthetic test; not a human response');await p.locator('#prior').fill('Automated form smoke only');
  for(const s of await p.locator('select').all())await s.selectOption((await s.getAttribute('name')).endsWith('preference')?'INSUFFICIENT':'NA');
  await p.locator('#reason-1440').fill('Synthetic validation only');await p.locator('#reason-390').fill('Synthetic validation only');for(const c of await p.locator('input[type=checkbox]').all())await c.check();
  const pending=p.waitForEvent('download');await p.locator('#download').click();const download=await pending;const payload=JSON.parse(fs.readFileSync(await download.path(),'utf8'));if(payload.values.reviewer_id!=='AUTOMATED_UI_SMOKE_NOT_A_REVIEW')throw Error('Export invalid');await download.delete();
 }
 if(external)throw Error('External request');await p.screenshot({path:`/tmp/cq2-review-${packet}-${width}.png`});rows.push({packet,width,...measured,external_requests:external,synthetic_export_discarded:width===1440&&packet==='R1'});await context.close();
}fs.writeFileSync(process.argv[2],JSON.stringify({kind:'UI_SMOKE_NOT_HUMAN_EVIDENCE',human_responses:0,rows},null,2));console.log(JSON.stringify(rows));}finally{await b.close()}})().catch(e=>{console.error(e);process.exitCode=1});
