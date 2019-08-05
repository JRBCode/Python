#
# easygui.py
# @author bulbasaur
# @description 
# @created 2019-07-19T20:12:05.589Z+08:00
# @last-modified 2019-07-25T21:43:02.361Z+08:00
#

import Easygui as g
import sys


while True:
    g.msgbox("嗨，欢迎进入第一个界面小游戏^_^")

    msg = "请问你希望在鱼C工作室学习到什么知识呢？"
    title = "小游戏互动"
    choices = ["谈恋爱","编程","OOXX","琴棋书画"]

    choice = g.choicebox(msg, title, choices)

    g.msgbox("你的选择是：" + str(choice), "结果：")

    msg = "你希望重新开始小游戏吗？"
    title = "请选择"

    if g.ccbox(msg, title):
        pass
    else:
        sys.exit(0)
