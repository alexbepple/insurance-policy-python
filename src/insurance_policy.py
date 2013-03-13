
class CarInsurance:
    extra_charge_rate_for_women = 0.1
    insurance_tax_rate = 0.19

    def __init__(self, power_kw):
        self.power_kw = power_kw

    def base_premium(self):
        return self.power_kw * 1.3

    def final_premium(self):
        tax = self.base_premium() * CarInsurance.insurance_tax_rate
        return self.base_premium() + tax

    def final_premium_for_women(self):
        extra_charge = self.base_premium() * CarInsurance.extra_charge_rate_for_women
        return self.final_premium() + extra_charge


