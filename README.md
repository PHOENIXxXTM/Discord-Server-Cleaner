# Discord-Server-Cleaner
⚙️ A powerful Discord management bot built with Python that safely wipes servers — including channels, roles, and members — with confirmation and detailed action logs.

# 🧹 Discord Server Cleaner Bot

A safe and powerful **Discord server cleaning tool** built with **Python (`discord.py`)**.  
It can delete **all channels**, **roles**, and even **kick members** with full **confirmation prompts** and **detailed logging**.

> ⚠️ **Use responsibly.** This bot is meant for your **own servers** or **testing environments**.  
> Never use it on public or unauthorized servers — doing so violates Discord’s Terms of Service.

---

## ✨ Features

- 🧹 **Server Cleaner:** Deletes all text, voice, and category channels.
- 🧾 **Role Wiper:** Removes all roles except `@everyone`.
- 👢 **Kick All Members:** Safely kicks all non-bot members with confirmation.
- ⚠️ **Confirmation System:** Prevents accidental wipes.
- 📜 **Logging:** Saves all actions to a `cleanup_log.txt` file.
- ♻️ **Error-safe:** Automatically creates a new log channel after cleanup.

---

## ⚙️ Setup

### 1️⃣ Requirements

- Python **3.8+**
- A Discord Bot Token (from [Discord Developer Portal](https://discord.com/developers/applications))
- The `discord.py` library

Install dependencies:
```bash
pip install discord.py
```
### 2️⃣ Enable Intents

Go to your bot page on the Discord Developer Portal
:

Under Bot → scroll down to Privileged Gateway Intents

Enable:

✅ SERVER MEMBERS INTENT

✅ MESSAGE CONTENT INTENT

✅ PRESENCE INTENT

Click Save Changes

### 3️⃣ Add Your Token

In your main.py file:

TOKEN = "YOUR_BOT_TOKEN_HERE"


Or store it securely in a .env file:

DISCORD_BOT_TOKEN=your_token_here


And load it in your code:

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

### 4️⃣ Invite Your Bot

Use this OAuth2 URL (replace YOUR_CLIENT_ID):

https://discord.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=8&scope=bot


Make sure the bot has Administrator permissions.

### 🚀 Usage
Command	Description
!cleanserver	Ask for confirmation before deleting everything

!confirmclean	Confirm and delete all channels and roles

!kickall	Ask for confirmation before kicking all members

!confirmkick	Kick all non-bot members

!shutdown	Gracefully shuts down the bot


After cleanup, a new channel #cleanup-log is automatically created,
and a text file cleanup_log.txt is updated with all actions.

📂 Project Structure

📁 Discord-Server-Cleaner/

│

├── main.py              # Bot source code

├── cleanup_log.txt      # Action logs (auto-generated)

└── README.md            # Project documentation


### 🧠 Notes

You must run !cleanserver before !confirmclean.

Don’t restart the bot between confirmation steps — flags reset after restart.

The bot cannot delete @everyone.

All actions are logged with timestamps.

### 🧑‍💻 Author

### Phoenix
💬 Built for Discord automation & server management.
🛠️ Made with ❤️ using discord.py

###⚠️ Disclaimer

This project is for educational and administrative purposes only.
The creator and contributors are not responsible for any misuse or damage caused by this bot.
Always comply with Discord’s Terms of Service
.
