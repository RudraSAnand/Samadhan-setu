const pins = [
  {x:60,y:54,cat:'Roads',status:'Resolved'},
  {x:180,y:40,cat:'Water',status:'Pending'},
  {x:120,y:140,cat:'Sanitation',status:'Pending'},
  {x:240,y:200,cat:'Roads',status:'In Progress'},
  {x:75,y:240,cat:'Sanitation',status:'Resolved'},
  {x:320,y:160,cat:'Water',status:'In Progress'},
  {x:290,y:81,cat:'Roads',status:'Pending'}
];
function pinClass(cat,status) {
  let c = '';
  if (cat==='Roads') c='pin-roads';
  if (cat==='Water') c='pin-water';
  if (cat==='Sanitation') c='pin-sanitation';
  if (status==='Pending') c += ' pin-pending';
  if (status==='In Progress') c += ' pin-inprogress';
  if (status==='Resolved') c += ' pin-resolved';
  return c;
}
function updateMap() {
  const cat = document.getElementById('mapCategory').value;
  const st = document.getElementById('mapStatus').value;
  const map = document.getElementById('dummyMap');
  map.innerHTML = '';
  pins.forEach(p => {
    if ((cat===''||p.cat===cat)&&(st===''||p.status===st)) {
      const div = document.createElement('div');
      div.className='pin '+pinClass(p.cat,p.status);
      div.style="position:absolute;left:" + p.x + "px;top:" + p.y + "px;border:2px solid #fff;box-shadow:0 0 3px #888;cursor:pointer;";
      div.title = p.cat + ' – ' + p.status;
      map.appendChild(div);
    }
  })
}
document.getElementById('mapCategory').onchange=updateMap;
document.getElementById('mapStatus').onchange=updateMap;
document.addEventListener('DOMContentLoaded',updateMap);
