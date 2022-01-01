import sys
import pyautogui
import time
import pyperclip
import os
import random
import datetime
import platform



def send_msg(my_msg, repeat_number):
    for i in range(int(repeat_number)):
        time_wait = random.uniform(1, 2)
        print('Repeat Number : ', i + 1, end='')
        print(' // Time wait : ', time_wait)
        time.sleep(time_wait)
        pyautogui.keyDown('enter')
        pyperclip.copy(my_msg)
        pyautogui.hotkey('command', 'v')
        pyautogui.keyDown('enter')
        pyautogui.keyDown('esc')
        pyautogui.keyDown('down')


def filter_friend(filter_keyword, init_number):
    # 사람 아이콘 클릭
    try:
        click_img(img_path + 'inactive_person.png')
        try:
            click_img(img_path + 'active_person.png')
        except Exception as e :
            print('Not fouund active person icon ', e)
    except Exception as e :
        print('Not fouund inactive person icon: ', e)
    # try:
    #     click_img(img_path + 'x.png')
    # except:
    #     pass
    # time.sleep(1)
    
    # 돋보기 아이콘 오른쪽 클릭
    click_img_plus_x(img_path+'search_icon.png', 30)
    pyautogui.keyDown('a')
    pyautogui.keyDown('esc')
    click_img_plus_x(img_path+'search_icon.png', 30)


    if filter_keyword == '':
        print("ESC")
        pyautogui.keyDown('esc')
    else:
        pyperclip.copy(filter_keyword)
    
    
    pyautogui.hotkey('command', 'v')
    for i in range(int(init_number)):
        print("init_number",init_number)
        pyautogui.keyDown('down')
    time.sleep(1)



def get_os_position(x,y):
    if platform.system() == "Darwin":
        return x//2, y//2
    return x, y

def image_postion(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    if location == None:
        pass
    x, y = location
    return x, y


def click_img(imagePath):
    x, y = image_postion(imagePath)
    pyautogui.click(get_os_position(x, y))


def click_img_plus_x(imagePath, pixel):
    x, y = image_postion(imagePath)
    pyautogui.click(get_os_position(x + pixel, y))


def doubleClickImg (imagePath):
    x, y = image_postion(imagePath)
    pyautogui.click(get_os_position(x, y), clicks=2)


def set_delay():
    delay_time = input("몇 초 후에 프로그램을 실행하시겠습니까? : ")
    print(delay_time + "초 후에 프로그램을 실행합니다.")
    for remaining in range(int(delay_time), 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r프로그램 실행!\n")


def logout():
    try:
        click_img(img_path + 'menu.png')
    except Exception as e:
        print('e ', e)
    try:
        click_img(img_path + 'logout.png')
    except Exception as e:
        print('e ', e)


def bye_msg():
    input('프로그램이 종료되었습니다.')


def set_import_msg():
    with open("send_for_text.txt", "r", encoding='UTF-8') as f:
        text = f.read()
        print('======== 아래는 전송할 텍스트입니다. ========\n', text)
        return text


def initialize():
    print('Monitor size : ', end='')
    print(pyautogui.size())
    print(pyautogui.position())
    # filter_keyword = input("필터링할 친구 이름. 없으면 enter.  ex) 학생 직장 99 : ")
    # repeat_number = input("반복할 횟수(ex. 필터링 검색된 친구 수) : ")
    init_number = input("필터링한 친구 기준 시작지점(ex. 필터링된 친구 시작지점) : ")
    filter_keyword = "(0)"
    repeat_number="999"

    my_msg = input("전송할 메세지. enter를 누를 경우 send_for_text.txt를 전송 : ")
    now = datetime.date.today()
    currentMonth = str(now).split('-')[1]
    print('=================')
    print('메세지 전송 시작!')
    print('=================')
    return (filter_keyword, init_number, repeat_number, my_msg)


# config
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'
conf = 0.9
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = False

# def cron_main():
if __name__ == "__main__":
    now = datetime.date.today()
    currentDate = str(now).split('-')[2]
    (filter_keyword, init_number, repeat_number, my_msg) = initialize()
    if len(my_msg) > 2:
        filter_friend(filter_keyword, init_number)
        send_msg(my_msg, repeat_number)
        # bye_msg()
    else:
        long_msg = set_import_msg()
        set_delay()
        filter_friend(filter_keyword, init_number)
        send_msg(long_msg, repeat_number)
        logout()
        # bye_msg()



# 예약방식 interval로 설정, 10초마다 한번 실행
# 예약방식 cron으로 설정, 각 5배수 분의 10, 30초마다 실행
# ex) (5분 10, 30초), (10분 10, 30초), (15분 10, 30초)
# 스케줄링 시작


