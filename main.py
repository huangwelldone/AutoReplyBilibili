import time

import pyautogui as p

import xlrd


def mouseclick(img, click_times, wait_time, key):
        try:
            locate = p.locateCenterOnScreen(image=img, confidence=0.9)
            if locate is not None:
                p.click(locate.x, locate.y, clicks=click_times, interval=0.2, duration=0.2, button=key)
                time.sleep(wait_time)
        except p.ImageNotFoundException:
            print("未找到匹配样式")


def main_work():
    i = 1
    while i < sheet1.nrows:
        cmd_type = sheet1.row(i)[0]
        cmd_name = sheet1.row(i)[2].value
        cmd_wait_time = sheet1.row(i)[3].value
        if cmd_type.value == "单击图标":
            img = sheet1.row(i)[1].value
            mouseclick(img, 1, wait_time=cmd_wait_time, key="left")
            print(f"{cmd_name}按钮已点击")
        elif cmd_type.value == "滚轮":
            p.scroll(-400, 10, 500)
            time.sleep(1)
            print(f"{cmd_name}已操作")
        i += 1


if __name__ == '__main__':
    wb = xlrd.open_workbook("command.xls")
    sheet1 = wb.sheet_by_index(0)
    print("已导入命令表格")
    while True:
        main_work()

# # 按键的字典字符串数据结构，中文字符的key对应图片全名的value
# buttons = {"回答": '1_reply.png', "豆包AI": '2_AI.png', "插入": '3_insert.png', "发布": '4_post.png'}


# # 点击按钮的通用函数
# def click_button(button_name, confidence=0.9, wait_time=1):
#     try:
#         location = p.locateCenterOnScreen(buttons[button_name], confidence=confidence)
#         if location is not None:
#             p.click(location.x, location.y)
#             print(f"已点击{button_name}按钮")
#             time.sleep(wait_time)
#     except p.ImageNotFoundException:
#         print(f"{button_name}按钮没找到")
#
#
# # 无限循环的主函数，按顺序循环点击对应出现的按钮
# if __name__ == '__main__':
#     while True:
#         click_button('回答')
#         click_button('豆包AI', wait_time=3)
#         click_button('插入', confidence=0.7)
#         click_button('发布', confidence=0.7, )
#         p.click(10, 300)
#         for _ in range(10):
#             p.press("down")
#         print("换一个评论回答")
