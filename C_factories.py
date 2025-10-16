class Book:
    # Konstruktor, __str__, apply_discount, _format_money si më lart

    @classmethod
    def from_string(cls, data_str):
        try:
            isbn, title, author, price = data_str.split(";")
            price = float(price)
            return cls(isbn, title, author, price)
        except Exception:
            raise ValueError("Formati i gabuar për Book.from_string")


class Member:
    # Konstruktor, __str__, change_email si më lart

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    @classmethod
    def anonymous(cls):
        return cls(0, "Anonim", "anonim@shkolla.al")
