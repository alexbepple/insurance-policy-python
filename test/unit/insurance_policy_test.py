from nose.tools import *
from insurance_policy import CarInsurance

class CarInsurance_Test:
    def setUp(self):
        self.golf = CarInsurance(100)
        self.beetle = CarInsurance(5)

    @istest
    def base_premium_depends_on_power(self):
        eq_(self.golf.base_premium(), 130.0)
        eq_(self.beetle.base_premium(), 6.5)

    @istest
    def final_premium_includes_tax(self):
        eq_(self.golf.final_premium(), 154.7)
        eq_(self.beetle.final_premium(), 7.735)

    @istest
    def is_more_expensive_for_women(self):
        eq_(self.golf.final_premium_for_women(), 167.7)
        eq_(self.beetle.final_premium_for_women(), 8.385)
