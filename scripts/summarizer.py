from openai import OpenAI
from scripts.config import OPENAI_API_KEY

client = OpenAI(api_key = OPENAI_API_KEY)

def summarise(article_text):
    if not article_text or len(article_text.strip()) < 100:
        return "Too short to summarize."
    
    prompt = f"""
    You are an expert news analyst and writer. Your job is to summarize the full news article provided below into clear and concise paragraphs. Ensure the summary captures:
    - The who, what, when, where, and why of the event or topic
    - All critical facts and developments from the article
    - Any key context, background, or implications
    - A neutral and objective tone

    Make sure the summary is self-contained and understandable without needing to refer to the original article.
    Each paragraph must contain at most 2-3 sentences for easy reading.

    Article:
    \"\"\"{article_text}\"\"\"
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert news summarizer."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Summary failed: {e}"
