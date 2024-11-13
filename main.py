import time

import pyautogui as p

# 图片保存路径
paths = {
    'reply': 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\1_reply.png',
    'ai': 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\2_AI.png',
    'insert': 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\3_Insert.png',
    'post': 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\4_post.png'
}


# 点击按钮的通用函数
def click_button(button_name, confidence=0.9, wait_time=1):
    try:
        location = p.locateCenterOnScreen(paths[button_name], confidence=confidence)
        if location is not None:
            p.click(location.x, location.y)
            print(f"已点击{button_name}按钮")
            time.sleep(wait_time)
    except p.ImageNotFoundException:
        print(f"{button_name}按钮没找到")


if __name__ == '__main__':
    while True:
        click_button('reply')
        click_button('ai', wait_time=3)
        click_button('insert', confidence=0.7)
        click_button('post', confidence=0.7, )
        p.click(10, 300)
        for _ in range(10):
            p.press("down")
        print("换一个评论回答")
