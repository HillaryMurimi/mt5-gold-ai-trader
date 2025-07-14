from models.sentiment_model import SentimentAnalyzer
import logging

class NewsSentimentHandler:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.analyzer = SentimentAnalyzer(model_name)

    def process_news(self, headlines):
        try:
            results = self.analyzer.analyze_sentiment(headlines)
            bullish_count = sum(1 for item in results if item['sentiment'] == 'bullish')
            bearish_count = sum(1 for item in results if item['sentiment'] == 'bearish')
            score = (bullish_count - bearish_count) / max(1, len(results))
            return {
                "summary": results,
                "bullish": bullish_count,
                "bearish": bearish_count,
                "sentiment_score": score
            }
        except Exception as e:
            logging.error(f"Error processing sentiment: {e}")
            return {
                "summary": [],
                "bullish": 0,
                "bearish": 0,
                "sentiment_score": 0
            }

if __name__ == '__main__':
    sample_headlines = [
        "Gold rallies as inflation fears mount.",
        "XAU/USD drops amid Fed tightening expectations."
    ]
    handler = NewsSentimentHandler()
    sentiment_report = handler.process_news(sample_headlines)
    print(sentiment_report)
