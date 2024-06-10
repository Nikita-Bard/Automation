rate = input("Оцените работу оператора от 1 до 5:")
rate_as_number = int(rate)
if(rate_as_number < 1):
    rate_as_number = 1
if(rate_as_number > 5):
    rate_as_number = 5
print(rate_as_number)

feedback = ""

if rate_as_number == 1:
    feedback = input("Иди ***:")
elif rate_as_number == 2:
    feedback = input("Расскажите, что Вас смутило:")
elif rate_as_number == 3:
    feedback = input("Расскажите, какого не 4?:")
elif rate_as_number == 4:
    feedback = input("Расскажите, молодец, но мог бы 5:")
else:
    feedback = input("Ты Повелитель этого мира:")

print("Спасибо за Ваш отзыв")