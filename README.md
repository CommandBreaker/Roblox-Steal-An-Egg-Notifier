<div align="center">
🥚 Steal an Egg — Rare Egg Notifier

Automatically detect rare eggs in Roblox and get notified instantly.






<br>

Never miss a rare egg spawn again. 🥚✨

</div>
✨ What is this?

Steal an Egg — Rare Egg Notifier is a lightweight Windows program for Steal an Egg on Roblox.

It monitors your screen using OCR and automatically detects rare eggs. When a selected egg appears, the program sends an instant notification to Telegram or Discord.

🥚 Supported Eggs
Egg	Detection
🟣 Divine Egg	✅
🔵 Eternal Egg	✅
🔴 Secret Egg	✅
⚡ Features

🔍 Automatic OCR detection

🟣 Divine Egg detection

🔵 Eternal Egg detection

🔴 Secret Egg detection

📱 Telegram notifications

💬 Discord Webhook notifications

⏱️ Adjustable checking delay

⚙️ Automatic configuration

📦 Standalone .exe

🚫 No Python installation required

🚫 No dependencies required

📥 Download
<div align="center">
🚀 Ready to use — no installation required!

You don't need Python or any additional dependencies.

<a href="../../releases"> <img src="https://img.shields.io/badge/⬇️%20DOWNLOAD%20LATEST%20RELEASE-8A2BE2?style=for-the-badge&logo=github" alt="Download"> </a>

<br><br>

Download the latest .exe from:

GitHub → Releases → Latest Release

Then simply run the .exe.

</div>
🚀 Setup Guide

Follow the steps below to get everything working.

💡 You only need to configure Telegram OR Discord. You don't need both.

1️⃣ 💬 Discord Webhook Setup

Want notifications in Discord?

Follow these steps:

Step 1 — Open your server

Open your Discord server and go to:

Server Settings → Integrations → Webhooks

Step 2 — Create a Webhook

Click:

Create Webhook

Choose the channel where you want to receive notifications.

Step 3 — Copy the Webhook URL

Copy the generated Webhook URL and paste it into the notifier when requested.

⚠️ IMPORTANT

Never share your Discord Webhook URL publicly.

Anyone who has access to the webhook may be able to send messages through it.

2️⃣ 📱 Telegram Setup

Telegram requires two things:

🤖 Bot Token

🆔 Chat ID

🤖 Get Your Bot Token

Open @BotFather
 on Telegram.

Start the bot and send:

/newbot


Follow the instructions.

After creating your bot, BotFather will give you a Bot Token.

It will look similar to:

123456789:AAxxxxxxxxxxxxxxxxxxxx


Copy the token and enter it into the program.

⚠️ Never share your Bot Token.

Do not upload it to GitHub or send it to anyone.

💬 Send a Message to Your Bot

Open your newly created bot and send:

/start


Can't find your bot?

Simply search for its username in Telegram.

💡 Most bot usernames end with _bot.

🆔 Get Your Chat ID

Open @userinfobot
 on Telegram.

Start the bot.

It will send you information about your Telegram account.

Find:

ID


The number next to ID is your Chat ID.

Copy it and enter it into the notifier.

3️⃣ 🖱️ OP Auto Clicker Setup

The notifier works by reading the text visible on your screen.

To keep the required interaction running, you can use OP Auto Clicker.

📥 Download

Download OP Auto Clicker from the official website:

https://www.opautoclicker.com/

⚙️ Recommended Settings

Set:

Click Interval: 3 seconds


Then place your mouse at the required position in the game.

📸 Example

Set OP Auto Clicker to a 3-second click interval and move your mouse to the location shown below.

[YOUR OP AUTO CLICKER SCREENSHOT HERE]

4️⃣ 🎮 Roblox Camera Setup

For better OCR accuracy, make sure the game screen is as clear as possible.

Move your camera down so that unnecessary background text does not cover the area where the egg information appears.

📸 Example

[YOUR ROBLOX CAMERA EXAMPLE HERE]

💡 The clearer the text is, the easier it is for OCR to recognize the egg.

🔔 Notifications

When a selected egg is detected, you will receive a notification.

📱 Telegram
🟣 DIVINE EGG SPAWNED!

🔵 ETERNAL EGG SPAWNED!

🔴 SECRET EGG SPAWNED!

💬 Discord

Discord notifications include @everyone.

Example:

🟣 DIVINE EGG SPAWNED!
@everyone


This allows everyone in the selected Discord channel to be notified.

⚙️ First Launch

When you start the program for the first time, it will ask you to configure your settings.

Notification Method
1: Telegram
2: Discord

Egg Types
1: Divine Eggs
2: Eternal Eggs
3: Secret Eggs


You can select multiple egg types.

For example:

12


means:

🟣 Divine Eggs

🔵 Eternal Eggs

While:

123


means all three egg types.

⏱️ Checking Delay

You can choose a delay between:

0 - 10 seconds


Default:

5 seconds

⚙️ Configuration

After the initial setup, the program automatically creates:

config.txt


You don't need to edit this file manually.

It contains your:

Notification method

Telegram Bot Token

Telegram Chat ID

Discord Webhook

Selected egg types

Checking delay

🔐 Security Warning

config.txt contains your private notification credentials.

Never upload config.txt to GitHub.

❗ Troubleshooting
<details> <summary>🔍 The program doesn't detect eggs</summary>

Make sure:

Roblox is running in Fullscreen.

OP Auto Clicker is enabled.

Your mouse is at the required position.

The relevant egg text is visible.

The camera is positioned correctly.

The text isn't covered by other UI elements.

The egg text is clear enough for OCR.

</details> <details> <summary>📱 Telegram notifications aren't working</summary>

Check:

Your Bot Token.

Your Chat ID.

That you have sent /start to your bot.

That the Bot Token was entered correctly.

That the bot is still active.

</details> <details> <summary>💬 Discord notifications aren't working</summary>

Check:

Your Webhook URL.

That the webhook still exists.

That the webhook is connected to the correct channel.

That the webhook has permission to send messages.

</details> <details> <summary>📦 The program won't start</summary>

Try:

Downloading the latest release again.

Making sure you're using Windows.

Running the .exe again.

Checking whether Windows Defender or another antivirus has blocked the file.

</details>
📦 Releases

The latest compiled version is available in the Releases section.

You don't need:

❌ Python

❌ pip

❌ Additional packages

❌ Manual dependency installation

Just:

Download → Run → Configure → Play 🎮

🛡️ Security

Your Telegram Bot Token and Discord Webhook are private credentials.

Never:

❌ Upload config.txt

❌ Share your Bot Token

❌ Share your Discord Webhook

❌ Post your credentials in screenshots

If you accidentally expose a Telegram Bot Token, regenerate it through BotFather.

⭐ Support the Project

If this project is useful to you, consider giving the repository a ⭐ Star!

It helps support the project and lets others discover it.

<div align="center">
🥚 Don't miss the next rare egg.

Good luck! 🍀

<br>

⭐ Star the repository if you like it! ⭐

</div>
<div align="center">

<sub>Made for the Steal an Egg community 🥚</sub>

</div>
