import functools


class SuperPlugin:
    def __init__(self, bot):
        self.bot = bot
        self.name = '未命名功能'
    
    # 发消息的函数使用此装饰器
    @staticmethod
    def sender(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kw):
            try:
                return func(self, *args, **kw)
            except Exception as e:
                self.bot.send(self.name + '田了，快找聪脑袋来debug吧！错误信息：' + str(e))
        return wrapper