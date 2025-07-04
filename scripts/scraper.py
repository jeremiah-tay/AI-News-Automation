from goose3 import Goose

def scrape_article_texts(urls):
    g = Goose()
    scraped_texts = []
    for url in urls:
        try:
            article = g.extract(url=url)
            text = article.cleaned_text.strip() if article.cleaned_text else ""
        except Exception:
            text = ""
        scraped_texts.append(text)
    return scraped_texts
