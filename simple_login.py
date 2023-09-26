# 로그인 프로그램 메인메뉴 함수
def login_mainmenu():
    # 터미널에서 사용자가 가장 먼저 보게될 메뉴
    login_menu = "\n1) Create a new User ID\n2) Change a password\n3) Display all User IDs\n4) Quit\n\nEnter Selection: "

    
    while True:
        try:
            # 사용자가 입력하는 메뉴 번호를 정수형 숫자로 제한해서 받는다
            select_menu = int(input(login_menu))
            if select_menu == 1:    # create new user id and password
                print("Selection: 1")
            elif select_menu == 2:   # change a password
                print("Selection: 2")
            elif select_menu == 3:   # display all user id
                print("Selection: 3")
            elif select_menu == 4:   # quit
                print("Selection: 4, Exit the program")
                break
            else:
                print("Incorrect Selection")

        except Exception:
            print("Select correct menu number")         
           


login_mainmenu()                       