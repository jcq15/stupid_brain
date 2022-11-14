from plugins.super_plugin import SuperPlugin
import requests
import json


class YiyanPlugin(SuperPlugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.base_url = 'https://v1.hitokoto.cn/'
        self.name = '每日一言'

    # 一言
    @SuperPlugin.sender
    def yiyan(self):
        url = self.base_url + '?c=d&c=i'
        res = requests.get(url)
        res_data = json.loads(res.text)
        text = f"{res_data['hitokoto']}\n——{res_data['from_who']}《{res_data['from']}》\n\n来源：{self.name}"
        print(text)
        self.bot.send(text)


if __name__ == '__main__':
    YiyanPlugin(None).yiyan()