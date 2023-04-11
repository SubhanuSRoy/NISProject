from fastapi import FastAPI
import joblib
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware

# Load the trained Random Forest Classifier model
rf = joblib.load("rf_model.pkl")
dt = joblib.load("dt_model.pkl")
knn = joblib.load("knn_model.pkl")
sv = joblib.load("sv_model.pkl")




# Create a FastAPI app
app = FastAPI()

# to allow all networks and cors
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the route to accept POST requests for login prediction
@app.post("/predict")
async def predict_login(request: Request):

    # Extract the input features from the request
    # Email = request["email"]
    # Password = request["password"]

    print(await request.body())
    request = await request.json()
    request = dict(request)

    Login_time = request["login_time"]
    IP_Addr = request["ip_addr"]

    # Preprocess the input features to convert categorical variables into numerical variables
    # Email = pd.factorize([Email])[0][0]
    # Password = pd.factorize([Password])[0][0]
    # IP_Addr = pd.factorize([IP_Addr])[0][0]

    if(IP_Addr == "182.79.4.254"):
        IP_Addr=0
    elif (IP_Addr == "10.0.0.1" ) :
        IP_Addr=1
    else:
        IP_Addr=2

    print(IP_Addr)

    # Make the prediction
    prediction1 = rf.predict([[IP_Addr, Login_time]])
    prediction2 = dt.predict([[IP_Addr, Login_time]])
    prediction3 = knn.predict([[IP_Addr, Login_time]])
    prediction4 = sv.predict([[IP_Addr, Login_time]])
    # print(prediction)
    predictions = prediction1, prediction2, prediction3, prediction4
    predictions = [str(i[0]) for i in predictions]

    # 1 means alert, and 0 means normal
    ct0=ct1=0
    
    for i in predictions:
        if(i=="alert"):
            ct1+=1
        else:
            ct0+=1
        print(i)

    print(predictions)
    print(ct0,ct1)
    # Prepare the response
    if ct0<ct1:
        status = "alert"
    else:
        status = "normal"
    
    print
    response = {"status": status}

    return response
    # except Exception as e:
    #     print("there is some issue")
    #     raise HTTPException(status_code=400, detail="Prediction failed")

# Run the FastAPI app locally
# if __name__ == "__main__":
#     import uvicorn
#     print("running on port 8000")
#     uvicorn.run(app, host="localhost", port=8000)
