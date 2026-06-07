class CashRegister:

    def __init__(self, discount=0):
        self._discount = discount
        self.total = 0.0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
        else:
            self._discount = value

    def add_item(self, title, price, quantity=1):
        line_total = price * quantity
        self.total += line_total
        for _ in range(quantity):
            self.items.append(title)
        self.previous_transactions.append({
            "item": title,
            "price": line_total,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions or self.discount == 0:
            print("There is no discount to apply.")
            return
        self.total = self.total - (self.total * self.discount / 100)
        self.total = round(self.total, 2)
        display = int(self.total) if self.total == int(self.total) else self.total
        print(f"After the discount, the total comes to ${display}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"]
        self.total = round(self.total, 2)
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])