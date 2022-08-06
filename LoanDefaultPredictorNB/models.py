from django.db import models

# Create your models here.


class Features(models.Model):
   LoanCurrentDaysDelinquent = models.FloatField(default = 0)
   LP_CustomerPrincipalPayments =models.FloatField(default = 0)
   LP_GrossPrincipalLoss = models.FloatField(default = 0)
   LP_CustomerPayments =  models.DecimalField(max_digits=10 , decimal_places=2 ,default = 0)
   LP_InterestandFees = models.FloatField(default = 0)
   LP_ServiceFees =  models.FloatField(default = 0)
   MonthlyLoanPayment = models.FloatField(default = 0)
   AvailableBankcardCredit = models.FloatField(default = 0)
   RevolvingCreditBalance = models.FloatField(default = 0)