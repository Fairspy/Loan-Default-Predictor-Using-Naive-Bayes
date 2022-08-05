import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .predictions import make_predictions
from .models import Features
from .forms import Feature_Form

# Create your views here.
def index(request):
    return render(request, 'index.html')

def PredictView(request):
    if request.method=='POST':
        form=Feature_Form(request.POST or None)
        if form.is_valid():
            LoanDayDel = form.cleaned_data['LoanCurrentDaysDelinquent']
            CustomerPrincipalPayments = form.cleaned_data['LP_CustomerPrincipalPayments']
            GrossPrincipalLoss = form.cleaned_data['LP_GrossPrincipalLoss']
            CustomerPay = form.cleaned_data['LP_CustomerPayments']
            InterestFees = form.cleaned_data['LP_InterestandFees']
            ServiceFee = form.cleaned_data['LP_ServiceFees']
            MLoanPay = form.cleaned_data['MonthlyLoanPayment']
            AvailBCredit = form.cleaned_data['AvailableBankcardCredit']
            RevCreditBal = form.cleaned_data['RevolvingCreditBalance']
            res = make_predictions(LoanDayDel,CustomerPrincipalPayments,GrossPrincipalLoss,CustomerPay,InterestFees,ServiceFee,MLoanPay,AvailBCredit,RevCreditBal)        
            if res == 1:
                res = True
            else:
                res = False
            context = {'res' : res}
            return render(request, 'result.html',context)
    form=Feature_Form()
    return render(request, 'form.html', {'form':form})
