from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd
import joblib

class StrategyClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train(self, data: pd.DataFrame):
        X = data.drop("strategy", axis=1)
        y = data["strategy"]  # strategy: scalping, day_trading, swing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(classification_report(y_test, predictions))

    def predict(self, input_features):
        return self.model.predict([input_features])[0]

    def save_model(self, path="strategy_classifier.pkl"):
        joblib.dump(self.model, path)

    def load_model(self, path="strategy_classifier.pkl"):
        self.model = joblib.load(path)

if __name__ == '__main__':
    # Example usage with dummy data
    data = pd.DataFrame({
        "volatility": [0.5, 1.2, 0.3],
        "volume": [100000, 300000, 50000],
        "momentum": [1.1, -0.8, 0.4],
        "sentiment_score": [0.9, -0.6, 0.2],
        "strategy": ["swing", "scalping", "day_trading"]
    })
    classifier = StrategyClassifier()
    classifier.train(data)
    print("Predicted strategy:", classifier.predict([0.4, 200000, 0.6, 0.3]))
