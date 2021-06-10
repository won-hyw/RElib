# library.py
# 1. 대출 2. 반납 3. 책 등록 4. 예약  5. 중고책 구매 6. 종료
from book import Book

def show_menu():
    print('1. 대출')
    print('2. 반납')
    print('3. 책 등록')
    print('4. 예약')
    print('5. 중고책 구매')
    print('6. 종료')
    menu = input('>> 메뉴를 선택해주세요 : ')
    return menu


def main():
    my_book = Book()
    while True:
        menu = show_menu()
        if menu == '1':
            pass
        elif menu == '2':
            pass
        elif menu == '3':
            my_book.add_book()
        elif menu == '4':
            pass
        elif menu == '5':
            pass
        elif menu == '6':
            break
        else:
            print('다시 입력하세요.')


if __name__ == '__main__':
    main()
