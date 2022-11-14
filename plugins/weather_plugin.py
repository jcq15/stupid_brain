from plugins.super_plugin import SuperPlugin
import requests
import json
import password


class WeatherPlugin(SuperPlugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.key = password.weather_key
        self.loc_code = 101010200  # 海淀
        self.base_url = 'https://devapi.qweather.com/v7/weather/'
        self.name = '每日天气'

    # 次日天气
    @SuperPlugin.sender
    def nextday(self):
        url = f'{self.base_url}3d?location={self.loc_code}&key={self.key}'
        weather_res = requests.get(url)
        weather = json.loads(weather_res.text)
        # print(weather)

        nextday = weather['daily'][1]
        weather_text = f"明天{nextday['tempMin']}℃~{nextday['tempMax']}℃，{nextday['textDay']}，{nextday['windDirDay']}{nextday['windScaleDay']}级。"
        # 如果降温
        if int(weather['daily'][0]['tempMin']) - int(weather['daily'][1]['tempMin']) >= 3 or\
            int(weather['daily'][0]['tempMax']) - int(weather['daily'][1]['tempMax']) >= 3:
            weather_text += '\n明天降温，活活冻死人！'
        # 如果下雨
        if '雨' in nextday['textDay']:
            weather_text += '\n明天下雨，淋成落汤鸡！'
        if '雪' in nextday['textDay']:
            weather_text += '\n明天下雪，变圣诞老人！'
        if int(nextday['windSpeedDay']) > 30:
            weather_text += '\n明天风大，把你吹上天！'
        weather_text += '\n\n来源：次日天气预报'
        self.bot.send(weather_text)

    @SuperPlugin.sender
    def today(self):
        url = f'{self.base_url}3d?location={self.loc_code}&key={self.key}'
        weather_res = requests.get(url)
        weather = json.loads(weather_res.text)
        # print(weather)

        today = weather['daily'][0]
        weather_text = f"今天{today['tempMin']}℃~{today['tempMax']}℃，{today['textDay']}，{today['windDirDay']}{today['windScaleDay']}级。"
        # 如果下雨
        if '雨' in today['textDay']:
            weather_text += '\n今天下雨，淋成落汤鸡！'
        if '雪' in today['textDay']:
            weather_text += '\n今天下雪，变圣诞老人！'
        if int(today['windSpeedDay']) > 30:
            weather_text += '\n今天风大，把你吹上天！'
        weather_text += '\n\n来源：当日天气预报'
        self.bot.send(weather_text)