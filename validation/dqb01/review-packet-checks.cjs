// UI smoke only: never creates or counts a human review.
const {chromium}=require('playwright'),fs=require('fs'),path=require('path');
const {pathToFileURL}=require('url');
const [root,out]=process.argv.slice(2);
(async()=>{
 const browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_EXECUTABLE?{executablePath:process.env.CHROMIUM_EXECUTABLE}:{})});
 const rows=[];
 for(const packet of ['R1-r0','R2-r0','R1-r1','R2-r1'])for(const width of [1440,390]){
  const context=await browser.newContext({viewport:{width,height:width===390?844:900}}),page=await context.newPage(),errors=[];
  page.on('pageerror',e=>errors.push(e.message));
  await page.goto(pathToFileURL(path.resolve(root,packet,'index.html')).href);
  const state=await page.evaluate(()=>({noOverflow:document.documentElement.scrollWidth<=innerWidth,emptyFormRejected:!document.querySelector('form').checkValidity(),scoreFields:document.querySelectorAll('select[name$="_X"],select[name$="_Y"]').length,humanChecked:document.querySelector('[name=human_independent]').checked}));
  const links=[];
  for(const label of ['X','Y']){
   const href=await page.getByRole('link',{name:'Abrir versão '+label}).getAttribute('href');
   const site=await context.newPage();await site.goto(pathToFileURL(path.resolve(root,packet,href)).href);
   links.push({label,loaded:(await site.locator('body').innerText()).includes('NOMA')});await site.close();
  }
  // Exercise download handler with an explicitly synthetic empty form. No checkbox
  // assertion, rating, or response file is retained or submitted to the coordinator.
  const downloadPromise=page.waitForEvent('download');
  await page.locator('form').evaluate(f=>f.dispatchEvent(new Event('submit',{bubbles:true,cancelable:true})));
  const download=await downloadPromise;const data=JSON.parse(fs.readFileSync(await download.path(),'utf8'));
  const downloadWorks=data.packet===packet.split('-')[0]&&data.stage===packet.split('-')[1]&&!data.values.human_independent;
  await download.delete();
  rows.push({packet,width,...state,links,downloadWorks,errors,pass:state.noOverflow&&state.emptyFormRejected&&state.scoreFields===36&&!state.humanChecked&&links.every(x=>x.loaded)&&downloadWorks&&errors.length===0});
  await context.close();
 }
 await browser.close();const result={scope:'AUTOMATED_UI_SMOKE_NOT_HUMAN_REVIEW',human_responses:0,rows};
 fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({passed:rows.filter(x=>x.pass).length,failed:rows.filter(x=>!x.pass)},null,2));process.exitCode=rows.every(x=>x.pass)?0:1;
})();
