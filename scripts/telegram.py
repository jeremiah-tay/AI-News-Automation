import requests

def send_telegram_message(text, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    if not response.ok:
        print("Telegram API error:", response.status_code, response.text)
    return response.ok

def notify_articles_via_telegram(df, bot_token: str, chat_id: str) -> None:
    for _, row in df.iterrows():
        title = row.get('Title', 'No Title')
        summary = row.get('Summary', '')
        link = row.get('Link', '#')
        message = f"<b>{title}</b>\n\n{summary}\n\n<a href=\"{link}\">Read more</a>"
        success = send_telegram_message(message, bot_token, chat_id)
        if not success:
            print(f"❌ Failed to send: {title}")
