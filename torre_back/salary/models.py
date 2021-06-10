from django.db import models

class Salary:
    def __init__(self, code=None, currency=None, min_amount=None, max_amount=None, periodicity=None, visible=None):
        self.code       = code
        self.currency   = currency
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.periodicity= periodicity
        self.visible    = visible
