from book import Book
# from borrow import Borrow


class Return(Book):
    def __init__(self):
        Book.__init__(self)

    def return_library(self):
        book_name = input("반납할 책 이름을 입력해주세요 : ")
        for book in self.book_list:
            if book.title != book_name:
                print('대여 목록에 존재하지 않는 책입니다!')
            else:
                del book_list[book_list.index(book_name)]

    def show_book(self):
        for index, book in enumerate(self.book_list):
            print(f'\n{index + 1}번.')
            print(book)
