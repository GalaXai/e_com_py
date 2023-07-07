class Card:
    def __init__(self, card_number: str) -> None:
        self.__balance = 0
        self.__credit = False
        self.__credit_amount = 0
        self.__creditToRepay = 0
        self.__withdrawalLimit = 0
        self.cardNumber = card_number

    def assign_credit(self, credit_amount: int) -> None:
        if self.__is_credit_already_assigned():
            raise Exception("Credit already assigned")

        if self.__is_bellow_threshold(credit_amount):
            raise Exception("Credit amount bellow threshold")

        self.__balance += credit_amount
        self.__creditToRepay += credit_amount
        self.__credit_amount += credit_amount
        self.__credit = True

    def withdraw(self, amount: int) -> None:
        if self.__check_withdraw_limit():
            raise Exception("Withdrawal limit reached \n" + "Please repay your credit to continue using your card")

        if self.__balance < amount:
            raise Exception("Insufficient funds")

        self.__balance -= amount
        self.__withdrawalLimit += 1

    def repay_credit(self, amount: int) -> None:
        if not self.__credit:
            raise Exception("You don't have any credit to repay")
        if self.__creditToRepay < amount:
            raise Exception("You can't repay more than you owe")
        self.__creditToRepay -= amount
        if self.__creditToRepay == 0:
            self.__credit = False

    def __check_withdraw_limit(self) -> bool:
        return self.__withdrawalLimit >= 5

    @staticmethod
    def __is_bellow_threshold(credit_amount: int) -> bool:
        return credit_amount < 100

    #  __ is for declaring private method
    def __is_credit_already_assigned(self) -> bool:
        return self.__credit is not False

    def get_balance(self) -> int:
        return self.__balance

    def get_credit(self) -> bool:
        return self.__credit

    def get_credit_to_repay(self) -> int:
        return self.__creditToRepay

    def get_credit_amount(self) -> int:
        return self.__credit_amount
