# import
import csv
from os import path

# csv파일을 read해서 정보를 가져오는 함수
def read_user_list():
    # 사용 할 csv_filename
    csv_filename = "userinfo.csv"

    # csv 파일이 존재해야만 기존정보가 존재해서 파일 읽기가 가능하므로 파일이 존재 할 때만 파일 읽기를 한다
    exist_csvfile = path.exists(csv_filename)
    if exist_csvfile:
        # csv 파일 읽기
        with open(csv_filename, 'r') as f:
            reader = csv.reader(f)
            user_list = list(reader)

    return user_list


# csv파일을 write하는 함수 (유저정보를 한줄씩 추가)
def write_userinfo(user_id, user_password):
    # 한 줄에 유저정보를 담기 위한 userdata 변수
    userdata = (user_id, user_password)
    
    # 사용 할 csv_filename
    csv_filename = "userinfo.csv"
    # csv 파일 쓰기
    # csv 쓰기 옵션을 'a'로 사용 새로운 유저정보를 csv파일 마지막줄에 추가해준다
    with open(csv_filename, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(userdata)


# csv파일을 update하는 함수 (변경 된 유저정보(새 비밀번호)를 유저리스트에 저장 후 전체 유저리스트 쓰기)
def update_userinfo(user_id, new_password):
    # 사용 할 csv_filename
    csv_filename = "userinfo.csv"
    # 유저 데이터 확인을 위해 기존의 유저정보를 불러온다
    userlist = read_user_list()
    # id에 맞는 유저리스트에서의 인덱스 값을 추출
    for user in userlist:
        if user[0] == user_id:
            user_index = userlist.index(user)
    # 유저리스트에서 비밀번호값을 변경한다
    userlist[user_index][1] = new_password

    # 변경된 정보를 csv파일에 전체쓰기한다
    with open(csv_filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(userlist)


# 비밀번호를 매개변수로 받아 각 항목 점수를 평가해서 리턴
def score_password(password):
    # 점수
    score = 0
    # 비밀번호에 허용된 특수문자열
    special_letters = "!@#$%^&*"

    # 비밀번호가 8자리 이상
    if len(password) >= 8:
        score += 1
    # 대문자 하나 이상
    if not password.islower():
        score += 1
    # 소문자 하나 이상
    if not password.isupper():
        score += 1
    # 숫자 하나 이상
    for letter in password:
        if letter.isdigit():
            score += 1
            break
    # 특수문자열에서 하나 이상
    for letter in password:
        if letter in special_letters:
            score += 1
            break

    return score


# id와 유저리스트를 매개변수로 받아서 id값의 중복여부를 확인하고 
# id값이 존재하면 유저정보, 존재하지 않으면 None을 리턴하는 함수
def check_equal_id(userid):
    # id값을 확인하기 위해 기존 csv파일을 읽어온다
    userlist = read_user_list()
    
    for user in userlist:
        if user[0] == userid:
            return user


# 새로운 유저 정보를 작성하는 함수
def create_user():
    # 사용자에게 ID와 비밀번호를 입력받는다
    user_id = input("ID: ")
    
    # 입력한 ID가 기존에 존재하는 ID일 경우, 존재하지 않는 ID를 입력할 때까지 입력창이 반복된다
    # check_equal_id() : 기존에 존재하는 id인지 user_list에서 확인한 다음에 존재하면 유저정보, 존재하지 않으면 None을 리턴한다
    while check_equal_id(user_id):
        user_id = input("Exist ID, Enter a different ID\nID: ")
        check_equal_id(user_id)

    # 위의 ID 검증과정을 통과하면 비밀번호 입력창을 출력한다
    user_password = input("PASSWORD: ")
    # 비밀번호 점수 평가
    score = score_password(user_password)
    score_standard = "8characters more\nuppercase one more\nlowercase one more\nnumber one more\nspecial characters one more"
    while score < 5:
        # user_password = input(f'\nYour passwore score: {score}\nWeakness password, Try again\n\n{score_standard}\n\nPASSWORD: ')
        # score = score_password(user_password)
        #
        if score < 3:
            user_password = input(f'\nYour passwore score: {score}\nWeakness password, Try again\n\n{score_standard}\n\nPASSWORD: ')
            score = score_password(user_password)
        #    
        else:
            answer = input("This password could be improved, Try again? (y/n): ")
            #
            if answer == 'n':
                score = 5
            elif answer == 'y':
                #
                user_password = input("PASSWORD: ")
                score = score_password(user_password)   
            else:
                print("Enter y or n")     

                

    # csv쓰기 함수를 사용하여 새로운 유저정보 마지막줄에 추가
    write_userinfo(user_id, user_password)
    

# 기존 유저의 비밀번호를 변경하는 함수
def change_password():
    # 유저에게 ID를 입력받는다
    user_id = input("ID: ")

    # ID값에 맞는 비밀번호도 가져올 수 있게 userinfo라는 변수에 check_equal_id값 할당
    userinfo = check_equal_id(user_id)
    # 입력한 ID가 기존에 존재하는 ID일 경우, 존재하지 않는 ID를 입력할 때까지 입력창이 반복된다
    # check_equal_id() : 기존에 존재하는 id인지 user_list에서 확인한 다음에 존재하면 유저정보, 존재하지 않으면 None을 리턴한다
    while not userinfo:
        user_id = input("Not found ID, Enter correct ID\nID: ")
        userinfo = check_equal_id(user_id)

    # 유저에게 비밀번호를 입력받는다
    input_password = input("PASSWORD: ")
    # id에 맞는 비밀번호
    correct_password = userinfo[1]

    # 현재 비밀번호와 입력된 비밀번호가 동일 할 때까지 비밀번호 입력을 반복한다
    while not input_password == correct_password:
        input_password = input("Incorrect PASSWORD, Enter correct PASSWORD\nPASSWORD: ")
    # 새로운 비밀번호    
    new_password = input("NEW PASSWORD: ")
    
    #
    update_userinfo(user_id, new_password)


# 전체 유저ID를 출력하는 함수
def display_all_user_id():
    #
    user_list = read_user_list()

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