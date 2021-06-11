# library.py
# 1. 도서관 책 모아보기 2. 대여 3. 반납 4. 책 등록 5. 예약  6. 중고책 구매 구현
from book import Book


class MyLibrary(Book):
    def __init__(self):
        super().__init__()
        self.book_list = [] # 내가 대여한 책의 리스트
        self.library_list = []  # 도서관에 있는 모든 책을 담을 리스트 필요
        self.basic_book()
        self.reservationBook_list = {}

    def add_book(self):
        new_book = Book()
        new_book.set_book()
        self.library_list.append(new_book)  # 리스트에 담기

    def show_library(self):  # 도서관에 있는 모든 책을 보여줌
        for index, library in enumerate(self.library_list):
            print(f'\n{index + 1}번.')
            print(library)

    def res_book(self):
        self.show_library()
        res_book = input('>> 예약할 책을 입력하세요: ')
        month = int(input('>> 대여할 월을 입력해주세요 : '))
        day = int(input('>> 대여할 일을 입력해주세요 : '))
        first_loan_date = "대여시작일: " + str(month) + "월 " + str(day) + "일"
        while True:  # 최대 대여 기간을 넘겼을 경우 다시 입력하게 만든다.
            loan_term = int(input('>> 대여할 기간을 입력해주세요 (최대 14일) : '))
            if loan_term > 14:
                print(f'대여 기간은 최대 14일까지 가능합니다. 다시 입력해주세요.')
            else:
                break
        month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(loan_term-1): # 대여할 기간만큼 반복
            day += 1
            if day == month_list[month-1]: # day가 그 달의 최대 일일 경우 다음 달로 넘겨준다
                day = 1
                month += 1
        last_loan_date = "대여마감일: " + str(month) + "월 " + str(day) + "일"
        for book in self.library_list:
            if res_book in book.title:
                self.reservationBook_list = {
                    'book': book,
                    'loan_date1': first_loan_date,
                    'loan_date2': last_loan_date
                }
        for key, value in self.reservationBook_list.items():
            print(value)

    def borrow_book(self):
        self.show_library()
        book_name = input('>> 대여할 책 이름을 검색하세요 : ')
        for book in self.library_list:
            if book_name in book.title:
                borrow_book = Book() # 수량을 1개로 넘기기 위해서 객체를 생성하여 넘긴다.
                borrow_book.title = book.title
                borrow_book.author = book.author
                borrow_book.publish = book.publish
                borrow_book.description = book.description
                borrow_book.price = book.price
                self.book_list.append(borrow_book)
                if book.quantity == 1:
                    self.library_list.remove(book)  # 더 이상 빌릴 수 없게
                else:
                    book.quantity -= 1
                return
        print('도서관에 존재하지 않는 책입니다!!')

    def return_library(self):
        for index, book in enumerate(self.book_list):
            print(f'\n{index + 1}번.')
            print(book)
        book_name = input('반납할 책 이름을 입력해주세요 : ')
        for book in self.book_list:
            if book_name in book.title:
                for return_book in self.library_list:
                    if book_name in return_book.title:
                        return_book.quantity += 1
                    else:
                        self.library_list.append(book)  # 다시 빌릴 수 있게
                self.book_list.remove(book)
                return
        print('대여 목록에 책이 존재하지 않습니다!!')

    def buy_book(self):
        self.show_library()
        search_book = input('>> 구매할 책 이름을 검색하세요 : ')
        for buy in self.library_list:
            if search_book in buy.title:
                answer = input(f'{buy.title}의 가격은 {buy.price}입니다. 사시겠습니까? (네/아니오) : ')
                if answer == '네':
                    for book in self.library_list:
                        if search_book in book.title:
                            if book.quantity == 1:
                                self.library_list.remove(book)
                            else:
                                book.quantity -= 1
                    return
                else:
                    return
        print('원하시는 책을 찾을 수 없습니다.')

    def basic_book(self):
        첫번째 = Book()
        첫번째.title = '아몬드'
        첫번째.author = '손원평'
        첫번째.publish = '창비'
        첫번째.description = '감정을 느끼지 못하는 소년의 특별한 성장 이야기'
        첫번째.price = 12000
        첫번째.quantity = 2
        self.library_list.append(첫번째)
        두번째 = Book()
        두번째.title = '어린왕자'
        두번째.author = '앙투안 드 생택쥐페리'
        두번째.publish = '인디고(글담)'
        두번째.price = 9800
        self.library_list.append(두번째)
        세번째 = Book()
        세번째.title = '달러구트 꿈 백화점'
        세번째.author = '이미예'
        세번째.publish = '팩토리나인'
        세번째.description = '꿈을 사고파는 사람들의 뭉클하고 따뜻한 이야기'
        세번째.price = 13800
        세번째.quantity = 3
        self.library_list.append(세번째)
        네번째 = Book()
        네번째.title = '소년이 온다'
        네번째.author = '한강'
        네번째.price = 13000
        self.library_list.append(네번째)
