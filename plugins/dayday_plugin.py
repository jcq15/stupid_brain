# 每日每日

from plugins.super_plugin import SuperPlugin
import requests
import json


class DaydayPlugin(SuperPlugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.base_url = 'https://v1.hitokoto.cn/'
        self.name = '每日每日'

    # 一言
    @SuperPlugin.sender
    def dayday(self):
        
        print(text)
        self.bot.send(text)