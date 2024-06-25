from user import User
from card import Card

alex = User('Alex')

alex.sayName()
alex.setAge(33)
alex.sayAge()

card = Card("5431 5467 5421 5468", "11/28", "Alex F")

alex.addCard(card)
alex.getCard().pay(1000)