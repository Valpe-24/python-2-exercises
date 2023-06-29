class TaxMan:
    def __init__(self, items, tax):
        self.items = items
        self.tax = tax
        self.__price_with_tax = self.calc_total

    def calc_total(self):
        price_list = list(map(lambda p: p['price'], self.items))
        total_price = 0
        tax_int = int(self.tax.replace("%", ""))

        for price in price_list:
            total_price += price

        price_tax = total_price * (tax_int/100) + total_price
        return price_tax

    @property
    def get_total(self):
        return self.__price_with_tax

