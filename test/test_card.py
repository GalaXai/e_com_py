import unittest
from creditcard.card import Card


class TestCard(unittest.TestCase):

    def test_AllowsAssignCredit(self):
        card = Card("123456789")
        card.assign_credit(1000)
        self.assertEqual(card.get_credit(), True)
        self.assertEqual(card.get_credit_amount(), 1000)
        self.assertEqual(card.get_credit_to_repay(), 1000)
        self.assertEqual(card.get_balance(), 1000)

    def test_AllowsDifferentCreditLimits(self):
        card1 = Card("123456789")
        card2 = Card("987654321")

        card1.assign_credit(1000)
        card2.assign_credit(2000)

        self.assertEqual(card1.get_credit_amount(), 1000)
        self.assertEqual(card2.get_credit_amount(), 2000)

    def test_DenyCreditAmountBellowThreshold(self):
        card = Card("123456789")
        with self.assertRaises(Exception):
            card.assign_credit(99)

    def test_CantAssignLimitTwice(self):
        card = Card("123456789")
        card.assign_credit(1000)
        with self.assertRaises(Exception):
            card.assign_credit(1000)

    def test_AllowsWithdraw(self):
        card = Card("123456789")
        card.assign_credit(1000)
        card.withdraw(500)
        self.assertEqual(card.get_balance(), 500)

    def test_DenyWithdrawalLimitReached(self):
        card = Card("123456789")
        card.assign_credit(10000)
        for _ in range(5):
            card.withdraw(500)
        with self.assertRaises(Exception):
            card.withdraw(500)

    def test_DenyWithdrawInsufficientFunds(self):
        card = Card("123456789")
        card.assign_credit(1000)
        with self.assertRaises(Exception):
            card.withdraw(1500)

    def test_AllowsRepayCredit(self):
        card = Card("123456789")
        card.assign_credit(1000)
        card.repay_credit(500)
        self.assertEqual(card.get_credit_to_repay(), 500)

    def test_DenyRepayCreditBellowZero(self):
        card = Card("123456789")
        card.assign_credit(1000)
        with self.assertRaises(Exception):
            card.repay_credit(1500)

    def test_DenyRepayCreditMoreThanOwed(self):
        card = Card("123456789")
        card.assign_credit(1000)
        card.repay_credit(500)
        with self.assertRaises(Exception):
            card.repay_credit(600)

    def test_DenyRepayCreditWhenNoCreditAssigned(self):
        card = Card("123456789")
        with self.assertRaises(Exception):
            card.repay_credit(500)


if __name__ == "__main__":
    unittest.main()
