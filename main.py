import requests
import json
import datetime
import time

from apscheduler.schedulers.background import BlockingScheduler

import password
from qywxserver import QYWXServer
from plugins.weather_plugin import WeatherPlugin
from plugins.yiyan_plugin import YiyanPlugin
from plugins.question_plugin import QuestionPlugin
from plugins.healthy_plugin import HealthyPlugin


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
question = QuestionPlugin(bot)
healthy = HealthyPlugin(bot)

# scheduler
scheduler.add_job(yiyan.yiyan, 'interval', hours=12, start_date='2022-11-13 12:02:00')
scheduler.add_job(weather.today, 'interval', days=1, start_date='2022-11-13 07:59:00')
scheduler.add_job(question.question, 'interval', days=1, start_date='2022-11-13 18:14:00')
scheduler.add_job(weather.nextday, 'interval', days=1, start_date='2022-11-13 23:01:00')
scheduler.add_job(healthy.lunch, 'interval', days=1, start_date='2022-11-13 11:28:00')
scheduler.add_job(healthy.dinner, 'interval', days=1, start_date='2022-11-13 17:58:00')
scheduler.add_job(healthy.sleep_weekday, 'cron', day_of_week='0-4', hour=22, minute=58)
scheduler.add_job(healthy.sleep_weekend, 'cron', day_of_week='0,6', hour=0, minute=28)

scheduler.start()

