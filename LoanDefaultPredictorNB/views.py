from django.shortcuts import render
from.forms import Feature_Form

# Create your views here.

def home (request) :
    print("hello")
    if request.method == 'POST' :
       print('posted') 
       dataform = Feature_Form(request.POST)
       if dataform.is_valid():
           dataform.save()
           print('seved')
    else :
        print("it's not a post request")
        
    #return render(request,'LoanDefaultPredictorNB/Predictor_template.html',{'form' : Feature_Form})
    return render(request,'LoanDefaultPredictorNB/Predictor_template.html',{'form' : Feature_Form})