class Book:
    # Konstruktor dhe __str__ si më lart

    def apply_discount(self, percent):
        if not (0 <= percent <= 50):
            raise ValueError("Zbritja duhet të jetë midis 0 dhe 50%.")
        discounted_price = self.price * (1 - percent / 100)
        return discounted_price

    def _format_money(self, value):
        return f"{value:.2f} L"


class Member:
    # Konstruktor dhe __str__ si më lart

    def change_email(self, new_email):
        if "@" not in new_email or "." not in new_email:
            raise ValueError("Email i ri jo i vlefshëm.")
        self.email = new_email
