# 📰 AI News Automation

AI News Automation is a fully automated pipeline that runs every 2 hours to deliver the latest AI-related articles. 
It fetches articles from Inoreader, extracts full text, summarizes the content using an AI model, stores the results in Google Sheets, and sends updates via Telegram—all without manual intervention.

---

## 🔧 Features

- 🔄 Automated article fetching from Inoreader
- 🌐 Full-text article scraping
- 🧠 AI-based summarization of content
- 📊 Google Sheets integration for storage
- 📬 Telegram bot notifications
- ⏱️ Runs every 2 hours via cron (macOS/Linux compatible)

---

## 📁 Project Structure
```
AI-News-Automation/
│
├── scripts/         # Utility scripts
│ ├── inoreader.py   # Access token and article fetch logic
│ ├── scraper.py     # Extracts full text from article links
│ ├── summarizer.py  # Summarizes text using an AI model
│ └── sheets.py      # Google Sheets integration
│
├── main.py          # Main automation pipeline
├── .env             # Contains environment variables
├── requirements.txt # Python dependencies
└── README.md        # You’re here!
```
