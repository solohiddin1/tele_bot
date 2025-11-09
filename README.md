# 🎵 Telegram YouTube Music Bot  

A simple Telegram bot that lets users **search, download, and listen to music from YouTube** directly in Telegram.  

## ✨ Features
- 🔍 Search YouTube videos by title or link  
- 🎶 Download audio as `.mp3` using **yt-dlp**  
- 🧹 Sanitizes filenames for safe storage  
- 📩 Sends audio files directly in chat  
- 🖼 Handles text and image messages  
- 📤 Forwards user requests to admin (support system)  
- 📝 Logs user activity  

## 🛠 Tech Stack
- [Python](https://www.python.org/)  
- [python-telegram-bot](https://python-telegram-bot.org/)  
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  

## 🚀 Setup
1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/telegram-music-bot.git
   cd telegram-music-bot

    Create a virtual environment and install dependencies

python -m venv venv
source venv/bin/activate   # on Linux/Mac
venv\Scripts\activate      # on Windows
pip install -r requirements.txt

Add your Telegram Bot Token to the code:

TOKEN = "your-telegram-bot-token"

Run the bot

    python main.py

📂 Project Structure

.
├── main.py           # Main bot logic
├── requirements.txt  # Python dependencies
├── audios/           # Downloaded audio files
└── README.md         # Project documentation

⚠️ Disclaimer

This bot is for educational purposes only.
Downloading copyrighted content without permission may violate YouTube’s Terms of Service. Use responsibly.
