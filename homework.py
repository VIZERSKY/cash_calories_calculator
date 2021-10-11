import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)
        """общая функциональность для дочерних классов CaloriesCalculator и CashCalculator"""

    def add_record(self, record):
        self.records.append(record)
        """Сохранение новой записи о расходах или приемах пищи"""

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)
        """Сколько сегодня калорий сьеденно или потрачено денег"""

    def get_week_stats(self):
        week_stats =[]
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
            return sum(week_stats)
    """сколько калорий сьеденно или потрачено денег за последние семь дней"""
    def get_limit(self):
        limit_balance = self.limit - self.get_today_stats()
        return limit_balance


class CaloriesCalculator(Calculator):

    def get_remained_calories(self):
        calories_remained = self.get_limit()
        if calories_remained > 0:
            return ('Сегодня можно съесть что-нибудь ещё, '
            f'но с общей калорийностью не более {calories_remained} Ккал')
        else:
            return 'Хватит есть!'
"""Дочерний класс класса Calculator"""

class CashCalculator(Calculator):
    USD_RATE = 72.5
    EURO_RATE = 84
    RUB_RATE = 1
"""Дочерний класс класса Calculator"""
    def get_remained_cash(self, currency='rub'):
        crn =  {'usd': ('USD', CashCalculator.USD_RATE),
               'euro': ('EURO', CashCalculator.EURO_RATE),
               'rub': ('RUB', CashCalculator.RUB_RATE)}
        cash_remained = self.get_limit()
        if cash_remained == 0:
            return 'Денег нет, держись'
        if currency not in crn:
            return f'Валюта {currency} не поддерживается'
        name, rate = crn[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            return (f'На сегодня осталось {cash_remained}'
                                        f'{name}')
        else:
            return (f'Денег нет, держись: твой долг - {abs(cash_remained)}'
                        f'{name}')


class Record:
"""создание записей"""
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date =dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


cash_calculator = CashCalculator(5000)
calories_calculator = CaloriesCalculator(3000)


cash_calculator.add_record(Record(amount=2140, comment='поход в кафе в пятницу с друзьями', date='01.10.2021'))

cash_calculator.add_record(Record(amount=500, comment='закупка по акции в пятерочке',date='02.10.2021'))


calories_calculator.add_record(Record(amount=1200, comment='курочка гриль из шаурмичной за домом', date='03.10.2021'))
print(calories_calculator.get_calories_remained())