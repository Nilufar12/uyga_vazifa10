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

# Flight = namedtuple("Flight", ["from_city", "to_city", "duration"])
#
# flights = [
#     ("Toshkent", "Samarqand", 1.2),
#     ("Toshkent",	"Istanbul",	5),
#     ("Nukus", "Toshkent", 1.5),
#     ("Toshkent", "Seul", 6.5),
#     ("Buxoro", "Toshkent", 1.2)
# ]
#
# duration = 0
#
# for flight in flights:
#     f = Flight(*flight)
#     if f.duration > 2:
#         duration += f.duration
#         print(f'''
# 2 soatdan uzun bo'lgan parvozlar: {f.from_city}-{f.to_city},
# Parvoz vaqti: {f.duration} soat''')
#
# print(f"\nUmumiy parvoz vaqti: {duration} soat")
                
                
# 5-topshiriq: Reyting tizimi
# Movie namedtuple:
# title, rating, year
# 2015-yildan keyin chiqqan va rating >= 8 bo‘lgan filmlarni chiqaring
#
# Movie = namedtuple("Movie", ["title", "rating", "year"])
#
# movies_data = [
#     ("Oppenheimer", 8.4, 2023),
#     ("Interstellar", 8.7, 2014),
#     ("Dune: Part Two", 8.6, 2024),
#     ("Mad Max: Fury Road", 8.1, 2015),
#     ("Parasite", 8.5, 2019),
#     ("The Dark Knight", 9.0, 2008),
#     ("Spider-Man: Across the Spider-Verse", 8.6, 2023)
# ]
#
# for movie in movies_data:
#     m = Movie(*movie)
#     if m.rating >= 8 and m.year > 2015:
#         print(f'''
# Reytingi "8" va undan yuqori bo'lgan film: "{m.title}",
# Chiqarilgan yili: {m.year} yil''')

# 6-topshiriq: Ro‘yxatni tahlil qilish
# Berilgan sonlar ro‘yxatida:
# eng katta
# eng kichik
# o‘rtacha qiymatni aniqlang
# (faqat sequence funksiyalaridan foydalaning)
#
# numbers = [2, 6, 99, 56, 42, -12, 112, 13, 10, 82, 48, 100, 73, 19]
#
# eng_katta = max(numbers)
# eng_kichik = min(numbers)
# orta_qiymat = sum(numbers) / len(numbers)
#
# print(f'''
# Eng katta son: {eng_katta}
# Eng kichik son: {eng_kichik}
# O\'rta qiymat: {orta_qiymat}''')


# 7-topshiriq: Tuple o‘zgarmasligi
# Berilgan tuple:
# colors = ("red", "green", "blue", "yellow")
#
# "blue" rangining indeksini toping
# "black" rangini qo‘shishga urinib ko‘ring
# nima sababdan xato chiqishini tushuntiring

# colors = ("red", "green", "blue", "yellow")
#
# print("Ko\'k rangning indeksi:", colors.index("blue"))
# try:
#     colors.append("black")
# except AttributeError as e:
#     print(f"Xatolik: {e}")
#     print("Tushuntirish: Tuple ob'ektiga yangi element qo'shib bo'lmaydi (immutable).")
#
# try:
#     colors[0] = "white"
# except TypeError as e:
#     print(f"Xatolik: {e}")
#     print("Tushuntirish: Tuple ichidagi elementlarni o'zgartirish mumkin emas.")
                
                
# 8-topshiriq: String — Sequence
# Berilgan matnda:
# nechta harf
# nechta raqam
# nechta bo‘sh joy borligini hisoblang
#
# matn = "2024 — Ona tili darslarida bu oʻyindan foydalanish gap tuzish va bosh darajali boʻlaklarni aniqlashda qoʻllashimiz mumkin"
# harf = 0
# raqam = 0
# bosh_joy = 0
#
# for word in matn:
#     if word.isalpha():
#         harf += 1
#     elif word.isdigit():
#         raqam += 1
#     elif word.isspace():
#         bosh_joy += 1
#
# print(f'''
# Harflar soni: {harf} ta,
# Raqamlar soni: {raqam} ta,
# Bo\'sh joylar soni: {bosh_joy}''')


# 9-topshiriq: Range bilan filtr
# 1 dan 100 gacha bo‘lgan sonlardan:
# faqat 5 ga karrali
# ammo 3 ga karrali bo‘lmagan sonlarni ro‘yxatga joylang

# def karra(i):
#     return i % 5 == 0 and i % 3 != 0
#
#
# karrali = list(filter(karra, range(1, 101)))
# print(karrali)
                
# 10-topshiriq: Sequence + Named Tuple
# Book namedtuple:
# title, author, pages
# kitoblar ro‘yxatini yarating
# eng ko‘p sahifali kitobni aniqlang
# barcha kitoblar sahifalari yig‘indisini hisoblang

#
# Book = namedtuple("Book", ["title", "author", "pages"])
#
#
# books = [
#     ("Sariq devni minib", "Xudoyberdi To'xtaboyev", 320),
#     ("Kecha va kunduz", "Abdulhamid Cho'lpon", 440),
#     ("Dunyoning ishlari", "O'tkir Hoshimov", 280),
#     ("Ufq", "Said Ahmad", 650),
#     ("Navoiy", "Oybek", 410),
#     ("Ikki eshik orasi", "O'tkir Hoshimov", 520),
#     ("Sohibqiron", "Abdulla Oripov", 180)
# ]
# max_page = Book(*books[0])
# jami_sahifalar = 0
# for book in books:
#     b = Book(*book)
#     if b.pages > max_page.pages:
#         max_page = b
#     jami_sahifalar += b.pages
#
# print(f"Eng ko\'p sahifali kitob nimi :{max_page.title}, yozuvchisi: {max_page.author}, sahifalar soni: {max_page.pages}")
# print("Jami sahifalar soni:", jami_sahifalar)

# 11. Faqat juft sonlar iteratori
#
# Topshiriq:
# 1 dan 20 gacha faqat juft sonlarni qaytaradigan iterator klass yarating.

# class MyRange:
#     def __init__(self, start, end, step):
#         self.start = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             self.start += self.step
#         else:
#             raise StopIteration
#         return self.start -1
#
#
# numbers = MyRange(1, 20, 2)
#
# for i in numbers:
#     print(i)

# 12. Teskari iterator
# Topshiriq:
# Ro‘yxatni oxiridan boshiga qarab aylanuvchi iterator yarating.

# class MyRange:
#     def __init__(self, start, end, step):
#         self.start = start
#         self.end = end
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             self.end -= self.step
#         else:
#             raise StopIteration
#         return self.end
#
#
# numbers = MyRange(10, 40, 10)
# num = []
# for i in numbers:
#     num.append(i)
# print(num)

# 13. Iterator + shart             Ishlalmadim!!!
#
# Topshiriq:
# Ro‘yxatdan faqat 5 dan katta sonlarni qaytaradigan iterator yozing.
#
# class Katta:
#     def __init__(self, l):
#         self.l = l
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.l):
#             self.index += 1
#
#
#
# l = [2, 2, 6, 88, 1, -9, -10]
# num = Katta(l)
# print(list(num))

# 14. Faqat har ikkinchi element
# Topshiriq:
# Ro‘yxatdan faqat har ikkinchi elementni qaytaradigan iterator yarating.
# 📌 Misol:
# [10, 20, 30, 40, 50] → 20, 40

class MyList:
    def __init__(self, num, index):
        self.num = num
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            self.start += self.step
            self.index += 1
        else:
            raise StopIteration
        return self.start -1


num = [10, 20, 30, 40, 50]
numbers = MyList(num)

for i in numbers:
    print(i)
