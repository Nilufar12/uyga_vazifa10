# 1-topshiriq: Talaba ma’lumotlari
# namedtuple yordamida Student nomli tuzilma yarating:
# maydonlar: name, age, score
# 5 ta talaba obyektini yarating
# faqat balli 80 dan katta bo‘lgan talabalarni chiqaring

from collections import namedtuple
#
# Student = namedtuple("Student", ["name", "age", "score"])
#
# students = [
#     ("Aziz", 17, 80),
#     ("Said", 17, 88),
#     ("Zebo", 18, 90),
#     ("Barno", 19, 78),
#     ("Farruh", 19, 81)
# ]
#
# for student in students:
#     st = Student(*student)
#     if st.score > 80:
#         print(f"Student: {st.name}, yoshi: {st.age}, bali: {st.score}")

# 2-topshiriq: Mahsulotlar tahlili
# Product nomli namedtuple yarating:
# name, price, quantity
# mahsulotlar ro‘yxatini tuzing
# umumiy qiymati (price * quantity) 100 000 dan katta mahsulotlarni chiqaring
# Product = namedtuple("Product", ["name", "price", "quantity"])
#
# products = [
#     ("tvorog", 18000, 25),
#     ("smetana", 15000, 5),
#     ("yogurt", 10000, 15),
#     ("kofe", 45000, 30)
# ]
#
# for product in products:
#     pr = Product(*product)
#     if (pr.price * pr.quantity) > 100000:
#         print(f"Maxsulot nomi: {pr.name}, narxi: {pr.price}, soni: {pr.quantity}")

# 3-topshiriq: Eng katta yosh
# Person namedtuple:
# first_name, last_name, birth_year
# hozirgi yilni hisobga olib eng katta yoshli odamni aniqlang

# Person = namedtuple("Person", ["first_name", "last_name", "birth_year"])
#
# persons = [
#     ("Aziz", "Hafizov", 2000),
#     ("Said", "Sultonov", 2001),
#     ("Zebo", "Abdullayeva", 1990),
#     ("Barno", "Burhonova", 2005),
#     ("Farruh", "Sobirov", 1992)
# ]
#
# oldest_person = Person(*persons[0])
#
# for person in persons:
#     p = Person(*person)
#     if p.birth_year < oldest_person.birth_year:
#         oldest_person = p
# print(f"Ro'yhatdagi yoshi eng kattasi: {oldest_person.first_name}")

# 4-topshiriq: Reyslar jadvali
# Flight namedtuple:
# from_city, to_city, duration
# faqat 2 soatdan uzun bo‘lgan parvozlarni chiqaring
# umumiy parvoz vaqtini hisoblang

Flights = ("Flights", ["from_city", "to_city", "duration"])

flights = [
        ("Toshkent", "Samarqand", 1.2),
        ("Toshkent",	"Istanbul",	5),
        ("Nukus", "Toshkent", 1.5),
        ("Toshkent", "Seul", 6.5),
        ("Buxoro", "Toshkent", 1.2)
]























