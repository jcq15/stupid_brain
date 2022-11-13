import requests
import json
import datetime
import time

from apscheduler.schedulers.background import BlockingScheduler

import password
from qywxserver import QYWXServer
from weather_plugin import WeatherPlugin


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

# scheduler
# scheduler.add_job(weather.nextday, 'interval', seconds=10, start_date='2022-11-13 20:44:30')
scheduler.add_job(weather.nextday, 'interval', days=1, start_date='2022-11-13 23:00:00')
scheduler.add_job(weather.today, 'interval', days=1, start_date='2022-11-13 08:00:00')

scheduler.start()