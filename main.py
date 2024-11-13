import time

import pyautogui as p

# 按键的字典字符串数据结构，中文字符的key对应图片全名的value
buttons = {"回答": '1_reply.png', "豆包AI": '2_AI.png', "插入": '3_insert.png', "发布": '4_post.png'}


# 点击按钮的通用函数
def click_button(button_name, confidence=0.9, wait_time=1):
    try:
        location = p.locateCenterOnScreen(buttons[button_name], confidence=confidence)
        if location is not None:
            p.click(location.x, location.y)
            print(f"已点击{button_name}按钮")
            time.sleep(wait_time)
    except p.ImageNotFoundException:
        print(f"{button_name}按钮没找到")


# 无限循环的主函数，按顺序循环点击对应出现的按钮
if __name__ == '__main__':
    while True:
        click_button('回答')
        click_button('豆包AI', wait_time=3)
        click_button('插入', confidence=0.7)
        click_button('发布', confidence=0.7, )
        p.click(10, 300)
        for _ in range(10):
            p.press("down")
        print("换一个评论回答")
