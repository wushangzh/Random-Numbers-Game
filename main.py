import random
from easygui import *

msgbox('欢迎来到猜数游戏!\n系统将在0-100之间取随机数，\n接着就可以进行猜数了！',
       '猜数游戏', '开始吧！', 'num.png')


def competition():
    while True:
        num = random.randint(0, 100)
        msg = '输入要猜的数字：'
        title = '猜数游戏'
        tms = 1
        while True:
            guess = integerbox(msg, title, 50, 0, 100, 'num.png')
            if tms > 10:
                msgbox('你在干嘛？十次了耶！重新开始辣！', '来自作者的嘲讽')
                tms = 1
                continue

            if guess is None:
                msgbox('你点了取消！即将退出！', '警告')
                break
            elif guess == num:
                msgbox('恭喜，猜对了！', title, '欧耶~')
                break
            elif guess > num:
                msgbox('猜的数字大了！', title)
            else:
                msgbox('猜的数字小了！', title)
            tms = tms + 1
            continue
        break


while True:

    competition()

    if ccbox('游戏结束！你想再来一次吗？', "提示", ['再来一次！', '退出吧！']):
        continue
    else:
        break
