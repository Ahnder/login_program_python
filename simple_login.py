# import
import csv
from os import path

# 새로운 유저 정보를 작성하는 함수
def create_user():
    # 사용자에게 ID와 비밀번호를 입력받는다
    user_id = input("ID: ")

    # 사용 할 csv_filename
    csv_filename = "userinfo.csv"
    # csv 파일이 존재해야만 기존정보가 존재해서 파일 읽기가 가능하므로 파일이 존재 할 때만 파일 읽기를 한다
    exist_csvfile = path.exists(csv_filename)
    if exist_csvfile:
        # csv 파일 읽기
        with open(csv_filename, 'r') as f:
            reader = csv.reader(f)
            user_list = list(reader)
        # 리스트 내포를 사용해서 유저가 존재하면 유저정보를, 존재하지 않으면 빈리스트를 값으로 가진다
        exist_user = [userinfo 
                      for userinfo in user_list 
                      if userinfo[0] == user_id]
    
        # 입력한 ID가 기존에 존재하는 ID일 경우, 존재하지 않는 ID를 입력할 때까지 입력창이 반복된다
        # exist_user: 입력한 ID가 기존에 존재할 경우 유저정보리스트를 값으로 가지므로 True, 존재하지 않을경우 빈리스트를 값으로 가지므로 False
        while exist_user:
            user_id = input("Exist ID, Enter a different ID\nID: ")
            exist_user = [userinfo 
                      for userinfo in user_list
                      if userinfo[0] == user_id]

    # 위의 ID 검증과정을 통과하면 비밀번호 입력창을 출력한다
    user_password = input("PASSWORD: ")

    data = (user_id, user_password)
    
    # csv파일 write 하기 위한 리스트
    data_list = list()
    data_list.append(data)

    # csv 파일 쓰기
    # csv 쓰기 옵션을 'w'에서 'a'로 바꿔서 새로운 유저정보를 추가해준다
    with open(csv_filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(data_list)
    

# 기존 유저의 비밀번호를 변경하는 함수
def change_password():
    # 유저에게 ID를 입력받는다
    user_id = input("ID: ")

    # 사용 할 csv_filename
    csv_filename = "userinfo.csv"

    # csv 파일이 존재해야만 기존정보가 존재해서 파일 읽기가 가능하므로 파일이 존재 할 때만 파일 읽기를 한다
    exist_csvfile = path.exists(csv_filename)
    if exist_csvfile:
        # csv 파일 읽기
        with open(csv_filename, 'r') as f:
            reader = csv.reader(f)
            user_list = list(reader)
        # 리스트 내포를 사용해서 유저가 존재하면 유저정보를, 존재하지 않으면 빈리스트를 값으로 가진다
        exist_user = [userinfo 
                      for userinfo in user_list 
                      if userinfo[0] == user_id]
    
        # 비밀번호를 변경하기 위해서는 기존에 유저정보가 존재해야 하므로 
        # 입력한 ID가 기존에 존재하지 않는 ID일 경우, 존재하는 ID를 입력할 때까지 입력창이 반복된다
        # exist_user: 입력한 ID가 기존에 존재할 경우 유저정보리스트를 값으로 가지므로 True, 존재하지 않을경우 빈리스트를 값으로 가지므로 False
        while not exist_user:
            user_id = input("Not found ID, Enter correct ID\nID: ")
            exist_user = [userinfo 
                      for userinfo in user_list
                      if userinfo[0] == user_id]   


        # 유저에게 비밀번호를 입력받는다
        # 위의 exist_user를 통과해야 비밀번호 입력 기능을 출력하고
        # exist_user에 ID값에 맞는 비밀번호 정보도 들어있으니 바로 적용한다
        user_password = input("PASSWORD: ")
        # 현재 비밀번호
        correct_password = exist_user[0][1]
        # 현재 비밀번호와 입력된 비밀번호가 동일 할 때까지 비밀번호 입력을 반복한다
        while not user_password == correct_password:
            user_password = input("Incorrect PASSWORD, Enter correct PASSWORD\nPASSWORD: ")

        # 새로운 비밀번호    
        new_password = input("NEW PASSWORD: ")

        
        # 변경 된 비밀번호 csv 파일 쓰기
        # csv파일을 읽어온 리스트에서 변경된 비밀번호에 맞는 유저 인덱스를 추출해서
        # 변경 된 값을 적용한 뒤 csv 파일에 전체 리스트를 쓴다
        for userinfo in user_list:
            if userinfo[0] == user_id:
                user_index = user_list.index(userinfo)

        # 유저리스트에서 알맞은 유저인덱스를 찾아 변경된 비밀번호 값 적용
        user_list[user_index][1] = new_password

        # 변경된 유저리스트를 csv파일에 'w'옵션으로 쓰기
        with open(csv_filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(user_list)               

    # 변경된 비밀번호로 유저 정보 출력
    # user_data = (user_id, new_password)

    # return user_list


# 전체 유저ID를 출력하는 함수
def display_all_user_id():
    # csv 파일 읽어오기
    # 사용 할 csv_filename
    csv_filename = "userinfo.csv"

    # csv 파일이 존재해야만 기존정보가 존재해서 파일 읽기가 가능하므로 파일이 존재 할 때만 파일 읽기를 한다
    exist_csvfile = path.exists(csv_filename)
    if exist_csvfile:
        # csv 파일 읽기
        with open(csv_filename, 'r') as f:
            reader = csv.reader(f)
            user_list = list(reader)

    # 모든 유저 ID 리스트
    all_user_id_list = list()
    for userinfo in user_list:
        all_user_id_list.append(userinfo[0])        

    print("All_User_IDs:\n" + '\n'.join(all_user_id_list))


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
                create_user()
            elif select_menu == 2:   # change a password
                change_password()
            elif select_menu == 3:   # display all user id
                display_all_user_id()
            elif select_menu == 4:   # quit
                print("Selection: 4, Exit the program")
                break
            else:
                print("Select correct menu number")

        except Exception:
            print("The input is not number, Select correct menu number")         
           

#
login_mainmenu()                  