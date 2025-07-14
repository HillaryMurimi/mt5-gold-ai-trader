from lot_optimizer.risk_model import RiskModel

class LotSizeOptimizer:
    def __init__(self, max_risk_percent=2):
        self.risk_model = RiskModel(max_risk_percent)

    def optimize(self, balance, entry_price, stop_price, pip_value=10):
        return self.risk_model.calculate_lot_size(
            balance=balance,
            entry_price=entry_price,
            stop_price=stop_price,
            pip_value=pip_value
        )

if __name__ == '__main__':
    optimizer = LotSizeOptimizer(max_risk_percent=2)
    lot = optimizer.optimize(balance=5000, entry_price=1950.0, stop_price=1940.0)
    print(f"Optimized lot size: {lot}")
