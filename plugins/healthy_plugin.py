# 纯文本，传啥参数说啥话

from plugins.super_plugin import SuperPlugin
import random

class HealthyPlugin(SuperPlugin):
    def __init__(self, bot):
        super().__init__(bot)
        self.name = '健康提醒小助手儿'
    
    def lunch(self):
        texts1 = [
            '到中午啦！',
            '今天中午要吃啥？',
            '美好的一天从中午开始！',
            '孔子曰：“中午不吃，下午崩溃。”'
        ]
        texts2 = [
            '工作再忙也要记得吃午饭哦！',
            '什么？你还没点外卖？赶紧去点！',
            '走走走，我们去吃好吃的咯！',
            '做咁多都冇用，先食飯啦！'
        ]
        texts3 = [
            '不然要饿肚肚！',
            '堂主很担心你！',
            '中午不吃饭，下午变垃圾！',
            '不吃饭会变笨脑袋！'
        ]
        # 从三个列表中随机选取一条组合起来
        text = random.choice(texts1) + random.choice(texts2) + random.choice(texts3)
        print(text)
        self.bot.send(text)
    
    def dinner(self):
        texts1 = [
            'Dinner time!',
            '今晚吃点儿什么？',
            '快乐的一天从晚上开始！',
            '孟子曰：“晚上不吃，睡不着觉。”'
        ]
        texts2 = [
            '工作再多也要吃晚饭哦！',
            '别忘了在路上点外卖儿！',
            '我们走，去找好吃的！',
            '做楞啊做，食飯先啦！'
        ]
        texts3 = [
            '饿肚肚多难受！',
            '饿肚肚让人心疼！',
            '不吃晚饭，变成傻蛋！',
            '晚饭是人类进步的阶梯！'
        ]
        # 从三个列表中随机选取一条组合起来
        text = random.choice(texts1) + random.choice(texts2) + random.choice(texts3)
        print(text)
        self.bot.send(text)
    
    def sleep_weekday(self):
        texts1 = [
            '咦，这么晚啦！',
            '身体是种田的本钱！',
            '在忙啥呢？',
            '快去睡觉啦！'
        ]
        texts2 = [
            '赶快洗澡澡睡觉觉！',
            '别忘了睡觉！',
            '我们走，去睡觉！',
            '乖宝宝，睡觉觉！'
        ]
        texts3 = [
            '明天还要上班儿呢！',
            '不然明天多累儿呀！',
            '早睡早起身体好！',
            '不睡觉会变笨脑袋！'
        ]
        # 从三个列表中随机选取一条组合起来
        text = random.choice(texts1) + random.choice(texts2) + random.choice(texts3)
        print(text)
        self.bot.send(text)
    
    def sleep_weekend(self):
        texts1 = [
            '天啊，已经这么晚啦！',
            '在种哪门子田呢？',
            '还不睡觉嘛！'
        ]
        texts2 = [
            '虽然明天不上班儿，',
            '虽然今天是周末儿，',
            '虽然明天不用太早起，',
        ]
        texts3 = [
            '但也不能睡太晚呀！',
            '但也要按时睡觉哦！',
            '但也尽量早点儿睡！',
        ]
        # 从三个列表中随机选取一条组合起来
        text = random.choice(texts1) + random.choice(texts2) + random.choice(texts3)
        print(text)
        self.bot.send(text)