import random
import time

# 定義七段顯示器的數字模式
segments = {
    '0': [' _ ', '| |', '|_|'],
    '1': ['   ', '  |', '  |'],
    '2': [' _ ', ' _|', '|_ '],
    '3': [' _ ', ' _|', ' _|'],
    '4': ['   ', '|_|', '  |'],
    '5': [' _ ', '|_ ', ' _|'],
    '6': [' _ ', '|_ ', '|_|'],
    '7': [' _ ', '  |', '  |'],
    '8': [' _ ', '|_|', '|_|'],
    '9': [' _ ', '|_|', ' _|']
}

def display_numbers(numbers):
    # 三行對應於七段顯示器的上中下三部分
    line1 = line2 = line3 = ""
    for number in numbers:
        line1 += segments[number][0] + " "
        line2 += segments[number][1] + " "
        line3 += segments[number][2] + " "
    print(line1)
    print(line2)
    print(line3)

while True:
    # 生成10個隨機數字
    random_numbers = [str(random.randint(0, 9)) for _ in range(12)]
    # print(random_numbers)

    # 清除屏幕輸出 (在支持ANSI escape的終端中)
    print("\033[H\033[J", end="")

    # 顯示數字
    display_numbers(random_numbers)

    # 等待五秒
    time.sleep(3)
