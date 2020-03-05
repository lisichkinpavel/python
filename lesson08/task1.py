class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def day_to_int(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return cls(day, month, year)

    @staticmethod
    def date_validation(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        if day in range(1, 32) and month in range(1, 13) and year > 0:
            return f'Date is valid'
        else:
            return f'Date is NOT valid'


today = Date.day_to_int('01-02-2020')
print(today.day, today.month, today.year)
print(today.date_validation('45-05-2020'))
