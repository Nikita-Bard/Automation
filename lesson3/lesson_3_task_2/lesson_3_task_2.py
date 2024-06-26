from smartphone import Smartphone

catolog = []
phone1 = Smartphone('iPhone', '8', '+79223469875')
phone2 = Smartphone('iPhone', '14', '+79643216584')
phone3 = Smartphone('Samsung', 'A13', '+79656543212')
phone4 = Smartphone('Google', 'Pixel 8', '+79653496578')
phone5 = Smartphone('Xiaomi', 'Mi 11', '+79889875246779')

catolog.append(phone1)
catolog.append(phone2)
catolog.append(phone3)
catolog.append(phone4)
catolog.append(phone5)

for phone in catolog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")