from fastapi import FastAPI, Request
import pickle

app = FastAPI()

model_pickle = open("classifier.pkl", 'rb')
clf = pickle.load(model_pickle)
    

@app.get("/")
async def root():
   return {"Key":"Loan Application Approval"}


@app.post("/file2")
async def hello(request: Request):
   if request.method == 'POST':
      print(request)
   return {"Key":"inside hello post"}

@app.post("/predict")
async def prediction(request: Request):
   if request.method == 'POST':
    loan_req = await request.json()
    print(loan_req)

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount'] / 1000

    # Making predictions
    prediction = clf.predict(
        [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return {"response":pred}



# loan_application = {
#     'Gender': "Male",
#     'Married': "Unmarried",
#     'ApplicantIncome': 50000,
#     'Credit_History': "Cleared Debts",
#     'LoanAmount': 500000
# }