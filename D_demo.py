from A_models import Book, Member
from B_methods import Book as BookB, Member as MemberB
from C_factories import Book as BookC, Member as MemberC

# 2 libra manualisht
b1 = BookC("97899943", "Python Bazë", "A. Hoxha", 1200.0)
b2 = BookC("97888888", "OOP në Python", "E. Dema", 800.0)

# 2 libra nga from_string
b3 = BookC.from_string("97811111;Algoritme;B. Dervishi;900")
try:
    b4 = BookC.from_string("gabim;format")  # do hedhë gabim
except ValueError as e:
    print("Gabim në from_string:", e)

# 3 anëtarë
m1 = MemberC(12, "Arta Kola", "arta.kola@shkolla.al")
m2 = MemberC(15, "Bledi Hysa", "bledi.hysa@shkolla.al")
m3 = MemberC.anonymous()

# Raporti
books = [b1, b2, b3]
members = [m1, m2, m3]

print("\nLIBRAT:")
for book in books:
    base = book._format_money(book.price)
    discounted = book._format_money(book.apply_discount(20))
    print(f'- {book} | Bazë: {base} | -20%: {discounted}')

print("\nANËTARËT:")
for member in members:
    print(f'- {member}')

count_over_1000 = sum(1 for book in books if book.price > 1000)
print(f"\nTot > 1000 L: {count_over_1000}")
