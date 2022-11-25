# 每日一题

from plugins.super_plugin import SuperPlugin
import requests
import json
import datetime

class QuestionPlugin(SuperPlugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.name = '每日一题'
        self.filepath = 'resources/question.json'

    @SuperPlugin.sender
    def question(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        today = str(datetime.date.today())
        if today in data:
            text = "【每日一题】" + data[today]
            self.bot.send(text)
