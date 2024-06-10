year = int(input('Введите год: '))
def is_year_leap(year):
    if year % 4 == 0:
        return 'високосный'
    else:
        return 'не високосный'
result = is_year_leap(year)
print(f'{year} год: {result}')