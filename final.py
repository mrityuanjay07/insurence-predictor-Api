from fastapi import FastAPI, Path,HTTPException,Query
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, model, model_version


app = FastAPI()

@app.get("/")
def hello():
    return {"message": "insurance premium prediction API"}

@app.get("/about")
def about():
    return {"message": "This is fully functional insurence premium prediction API which is use to predict the premium of the insurence of the customer ."}

@app.get('/health')
def health_check():
    return{
        'status':'Ok',
        'model_load': 'model is loaded',
        

    }


@app.post('/predict')
def predict_premium(data: UserInput):

    user_input ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

            prediction = predict_output(user_input)

            return JSONResponse(status_code=200, content={'predicted_category': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e) )




