import numpy as np
import os.path

def make_predictions(LoanDayDel,CustomerPrincipalPayments,GrossPrincipalLoss,CustomerPay,InterestFees,ServiceFee,MLoanPay,AvailBCredit,RevCreditBal):
    import pickle
    BASE = os.path.dirname(os.path.abspath(__file__))
    print(BASE)
    x = [LoanDayDel,CustomerPrincipalPayments,GrossPrincipalLoss,CustomerPay,InterestFees,ServiceFee,MLoanPay,AvailBCredit,RevCreditBal]
    x_shaped = np.array(x).reshape(1,-1)
    tf = pickle.load(open(os.path.join(BASE,'../static/PowerTransform.pkl'),'rb'))
    x_final = tf.transform(x_shaped)
    model = pickle.load(open(os.path.join(BASE,'../static/model_final_NB.pkl'),'rb'))
    prediction = model.predict(x_final)
    return prediction