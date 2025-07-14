class RiskModel:
    def __init__(self, max_risk_percent=2):
        self.max_risk_percent = max_risk_percent

    def calculate_risk_amount(self, balance):
        """
        Returns the dollar amount to risk on a single trade based on account balance.
        """
        return (self.max_risk_percent / 100.0) * balance

    def calculate_stop_loss_distance(self, entry_price, stop_price):
        """
        Calculates stop loss distance in pips.
        """
        return abs(entry_price - stop_price)

    def calculate_lot_size(self, balance, entry_price, stop_price, pip_value=10):
        risk_amount = self.calculate_risk_amount(balance)
        stop_loss_pips = self.calculate_stop_loss_distance(entry_price, stop_price)
        if stop_loss_pips == 0:
            return 0
        lot_size = risk_amount / (stop_loss_pips * pip_value)
        return round(max(lot_size, 0.01), 2)  # minimum 0.01 lots
