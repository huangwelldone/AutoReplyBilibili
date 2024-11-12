# Bilibili网站自动回复评论的脚本
# 使用方法：在你的浏览器里添加豆包AI插件，主屏幕网页打开任意UP主的视频评论区
# 豆包AI在你点击评论的时候有豆包帮你评论的选项，用此特性实现AI自动化评论
# 注意事项：你可以将网页放大至150%，这样需要点击的按钮就可以比较大，分辨率识别的更准
import time

import pyautogui as p

# 图片保存路径
replyPath = 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\1_reply.png'
AIPath = 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\2_AI.png'
insertPath = 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\3_Insert.png'
PostPath = 'C:\\Users\\HuangWellDone\\Desktop\\PythonProject\\AutoReplyBili\\4_post.png'


# 点击回复按钮
def click_reply():
    try:
        location = p.locateOnScreen(replyPath, confidence=0.9)
        if location is not None:
            x, y = p.center(location)
            p.click(x, y)
            print("已点击回复按钮")
        else:
            print("没有找到回复按钮")
    except p.ImageNotFoundException:
        print("回复图片没找到")


# 点击AI回复按钮
def click_ai():
    try:
        location = p.locateOnScreen(AIPath, confidence=0.9)
        if location is not None:
            x, y = p.center(location)
            p.click(x, y)
            print("已点击AI按钮")
        else:
            print("没有找到AI按钮")
    except p.ImageNotFoundException:
        print("回复AI没找到")


# 点击插入按键
def insert_ai_reply():
    try:
        location = p.locateOnScreen(insertPath, confidence=0.7)
        if location is not None:
            x, y = p.center(location)
            p.click(x, y)
            print("已点击插入按钮")
        else:
            print("没有找到插入按钮")
    except p.ImageNotFoundException:
        print("插入按钮没找到")


# 点击发布按键
def post_reply():
    try:
        location = p.locateOnScreen(PostPath, confidence=0.7)
        if location is not None:
            x, y = p.center(location)
            p.click(x, y)
            print("已点击发布按钮")
        else:
            print("没有找到发布按钮")
    except p.ImageNotFoundException:
        print("发布按钮没找到")


if __name__ == '__main__':
    while True:
        click_reply()
        time.sleep(1)
        click_ai()
        time.sleep(6)
        insert_ai_reply()
        time.sleep(1)
        post_reply()
        p.click(10, 300)
        for _ in range(10):
            p.press("down")
        print("换一个评论回答")
