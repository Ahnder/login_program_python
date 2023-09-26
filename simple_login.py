# import csv
import csv

# 새로운 유저 정보를 작성하는 함수
def create_user():
    # 사용자에게 ID와 비밀번호를 입력받는다
    user_id = input("ID: ")

    # 사용 할 csv_filename
    csv_filename = "userinfo.csv"
    # csv 파일 읽기
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)
        read_user_list = list(reader)
    # 리스트 내포를 사용해서 유저가 존재하면 유저정보를, 존재하지 않으면 빈리스트를 값으로 가진다
    exist_user = [userinfo 
                  for userinfo in read_user_list 
                  if userinfo[0] == user_id]
    
    # 입력한 ID가 기존에 존재하는 ID일 경우, 존재하지 않는 ID를 입력할 때까지 입력창이 반복된다
    while exist_user:
        user_id = input("Exist ID, Enter a different ID\nID: ")
        exist_user = [userinfo 
                  for userinfo in read_user_list 
                  if userinfo[0] == user_id]

    # user_password = input("PASSWORD: ")

    # data = (user_id, user_password)
    
    # # csv파일 write 하기 위한 리스트
    # data_list = list()
    # data_list.append(data)

    # # csv 파일 쓰기
    # with open(csv_filename, 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(data_list)

    return user_id


# 로그인 프로그램 메인메뉴 함수
def login_mainmenu():
    # 터미널에서 사용자가 가장 먼저 보게될 메뉴
    login_menu = "\n1) Create a new User ID\n2) Change a password\n3) Display all User IDs\n4) Quit\n\nEnter Selection: "

    # 4번 종료 메뉴가 선택될 떄까지 메뉴화면을 계속 출력한다
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
                print("Select correct menu number")

        except Exception:
            print("The input is not number, Select correct menu number")         
           

#
print(create_user())                     