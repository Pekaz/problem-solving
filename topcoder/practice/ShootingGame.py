from decimal import Decimal

class ShootingGame:
    def findProbability(self, p):
        pA = Decimal(p) / Decimal(1000000.0)
        result = pA/(1-pA)
        if result>1:
            return -1.0
        return float(result)
