#!/usr/bin/env python3
# coding: utf-8
from wxpy import *
bot = Bot()
# api可直接用,也可去图灵机器人官网申请
tuling = Tuling(api_key='476f6540842b49208a3d47e5d63258a6')
@bot.register(msg_types=TEXT)
def auto_reply_all(msg):
    tuling.do_reply(msg)
bot.join()
