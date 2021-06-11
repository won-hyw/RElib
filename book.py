# book.py
# 책을 등록하는 역할
# title, author, publish(출판사), description, price, quantity(수량)
class Book:
    def __init__(self):
        self.title = ''
        self.author = ''
        self.publish = ''
        self.description = ''
        self.price = 0
        self.quantity = 1
        self.loan_date = ''

    def set_title(self):
        title = input('>> 책 제목을 입력해주세요: ')
        if title == '':
            print('책 제목을 입력해주세요....ㅠ')
            self.set_title()
        else:
            self.title = title

    def set_author(self):  # 책 저자를 입력하지 않으면은 무명으로 판단
        author = input('>> 책 저자를 입력해주세요: ')
        self.author = '무명' if author == '' else author

    def set_publish(self):
        publish = input('>> 책 출판사를 입력해주세요: ')
        self.publish = '' if publish == '' else publish

    def set_description(self):
        description = input('>> 한 줄 설명을 입력해주세요: ')
        self.description = '' if description == '' else description

    def set_price(self):
        price = input('>> 책 가격을 입력해주세요: ')
        self.price = 0 if price == '' else price

    def set_quantity(self):
        quantity = input('>> 책 수량을 입력해주세요: ')
        self.quantity = 1 if quantity == '' else quantity

    def set_book(self):
        self.set_title()
        self.set_author()
        self.set_publish()
        self.set_description()
        self.set_price()
        self.set_quantity()

    def __str__(self):
        return f'책 제목: {self.title}\n저자: {self.author}\n출판사: {self.publish}\n한줄설명: {self.description}\n가격: {self.price}\n수량: {self.quantity}'
