import requests
import json
import datetime
import time

from apscheduler.schedulers.background import BlockingScheduler

import password
from qywxserver import QYWXServer
from plugins.weather_plugin import WeatherPlugin
from plugins.yiyan_plugin import YiyanPlugin

# 创建后台执行的 schedulers
scheduler = BlockingScheduler(timezone='Asia/Shanghai')

bot = QYWXServer(
    password.company_id,   # 企业id
    password.agent_id,              # agent id
    password.agent_secret,  # secret
    scheduler
)

# plugins
weather = WeatherPlugin(bot)
yiyan = YiyanPlugin(bot)

# scheduler
scheduler.add_job(weather.nextday, 'interval', days=1, start_date='2022-11-13 23:01:00')
scheduler.add_job(weather.today, 'interval', days=1, start_date='2022-11-13 07:59:00')
scheduler.add_job(yiyan.yiyan, 'interval', hours=6, start_date='2022-11-13 06:02:00')  # 0, 6, 12, 18
# scheduler.add_job(weather.today, 'interval', seconds=6, start_date='2022-11-13 06:02:00')  # 0, 6, 12, 18


scheduler.start()