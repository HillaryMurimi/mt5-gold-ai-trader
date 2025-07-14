from transformers import pipeline
import logging

class SentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        try:
            self.classifier = pipeline("sentiment-analysis", model=model_name)
        except Exception as e:
            logging.error(f"Failed to load sentiment model: {e}")
            self.classifier = None

    def analyze_sentiment(self, texts):
        if not self.classifier:
            return []
        results = []
        for text in texts:
            result = self.classifier(text[:512])[0]  # Truncate long texts for BERT models
            sentiment = "bullish" if result["label"] == "POSITIVE" else "bearish"
            results.append({"text": text, "sentiment": sentiment, "score": result["score"]})
        return results

if __name__ == '__main__':
    sample_news = [
        "Gold prices soar after Fed's dovish tone.",
        "Investors worry as gold tumbles following strong dollar rally."
    ]
    analyzer = SentimentAnalyzer()
    sentiments = analyzer.analyze_sentiment(sample_news)
    for item in sentiments:
        print(item)
