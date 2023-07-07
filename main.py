from creditcard.card import Card


def main():
    card1 = Card("123456789")
    card1.assigncredit(1000)
    card1.withdraw(500)
    card1.repay_credit(100)
    print(card1.get_balance())
    print(card1.get_credit())
    print(card1.get_credit_to_repay())


if __name__ == '__main__':
    main()
