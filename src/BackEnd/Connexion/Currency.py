import logging

logger = logging.getLogger(__name__)
class Currency(object):

    def __init__(self, name, _id, full_name, central_bank, country, fraction_digits):
        self.currency = name
        self._id = _id
        self.full_name = full_name
        self.central_bank = central_bank
        self.country = country
        self.fraction_digits = fraction_digits



