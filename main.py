# main.py
# 1. 도서관 책 모아보기 2. 대여 3. 반납 4. 책 등록 5. 예약  6. 중고책 구매 7. 종료
from library import MyLibrary


def show_menu():
    print('1. 도서관 책 모아보기')
    print('2. 대여')
    print('3. 반납')
    print('4. 책 등록')
    print('5. 예약')
    print('6. 중고책 구매')
    print('7. 종료')
    menu = input('>> 메뉴를 선택해주세요 : ')
    return menu


def main():
    my_book = MyLibrary()
    while True:
        menu = show_menu()
        if menu == '1':
            # 도서관 책 모아보기
            my_book.show_library()
        elif menu == '2':
            # 대여
            my_book.borrow_book()
        elif menu == '3':
            # 반납
            my_book.return_library()
        elif menu == '4':
            # 책 등록
            my_book.add_book()
        elif menu == '5':
            # 예약
            my_book.res_book()
        elif menu == '6':
            # 중고책 구매
            my_book.buy_book()
        elif menu == '7':
            # 종료
            break
        else:
            print('다시 입력하세요.')


if __name__ == '__main__':
    main()
