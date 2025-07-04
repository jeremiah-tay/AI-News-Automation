from scripts import inoreader, sheets, scraper, summarizer, telegram
from scripts.config import (
    TELEGRAM_BOT_TOKEN_AI_NEWS,
    TELEGRAM_CHAT_ID_AI_NEWS,
    TELEGRAM_BOT_TOKEN_TECH_STOCK_NEWS,
    TELEGRAM_CHAT_ID_TECH_STOCK_NEWS
)
import pandas as pd
from datetime import datetime, timezone, timedelta

###### CHANGE TO BEGIN PROCESS ####################
sheet_name = "AI News"
worksheet_name = "AI News"
bot_token = TELEGRAM_BOT_TOKEN_AI_NEWS
chat_id = TELEGRAM_CHAT_ID_AI_NEWS
####################################################

def main():
    # Step 1: Get articles
    token = inoreader.get_access_token()
    articles = inoreader.fetch_articles(token)

    # Step 2: Load sheet and filter new
    sheet, records = sheets.load_records(sheet_name = sheet_name, worksheet_name = worksheet_name)
    existing_ids = {row['Article ID'] for row in records if 'Article ID' in row}
    df = pd.DataFrame([
        {
            "Article ID": item.get('id'),
            "Date Scraped": item.get('crawled', ''),  # or use datetime.now()
            "Title": item.get('title'),
            "Date Published": item.get('published'),
            "Link": item.get('alternate', [{}])[0].get('href', ''),
            "Publication": item.get('origin', {}).get('title', ''),
            "Author": item.get('author', '')
        }
        for item in articles if item.get('id') not in existing_ids
    ])

    # Step 3: Process articles
    if not df.empty:
        df['Article Text'] = scraper.scrape_article_texts(df['Link'])
        print("Summarising...")
        df['Summary'] = df['Article Text'].apply(summarizer.summarise)
        sheets.append_articles(sheet, df)
        telegram.notify_articles_via_telegram(df, bot_token = bot_token, chat_id = chat_id)
    else:
        print("No new articles.")

if __name__ == "__main__":
    main()