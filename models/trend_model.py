import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

class TrendPredictor:
    def __init__(self, look_back=60):
        self.look_back = look_back
        self.model = self._build_model()
        self.scaler = MinMaxScaler(feature_range=(0, 1))

    def _build_model(self):
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(self.look_back, 1)))
        model.add(LSTM(50))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def preprocess_data(self, data):
        scaled_data = self.scaler.fit_transform(data.reshape(-1, 1))
        X, y = [], []
        for i in range(self.look_back, len(scaled_data)):
            X.append(scaled_data[i - self.look_back:i, 0])
            y.append(scaled_data[i, 0])
        return np.array(X), np.array(y)

    def reshape_for_lstm(self, X):
        return np.reshape(X, (X.shape[0], X.shape[1], 1))

    def train(self, data, epochs=10, batch_size=32):
        X, y = self.preprocess_data(data)
        X = self.reshape_for_lstm(X)
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def predict(self, data):
        last_60 = data[-self.look_back:]
        scaled_input = self.scaler.transform(last_60.reshape(-1, 1))
        X_test = np.reshape(scaled_input, (1, self.look_back, 1))
        predicted_scaled = self.model.predict(X_test)
        return self.scaler.inverse_transform(predicted_scaled)[0][0]

    def save_model(self, model_path='trend_model.h5', scaler_path='scaler.pkl'):
        self.model.save(model_path)
        joblib.dump(self.scaler, scaler_path)

    def load_model(self, model_path='trend_model.h5', scaler_path='scaler.pkl'):
        from tensorflow.keras.models import load_model
        self.model = load_model(model_path)
        self.scaler = joblib.load(scaler_path)
