import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Load pipeline_v2.bin
with open("pipeline_v2.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

app = FastAPI(title="Lead Scoring API")

class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float

class PredictionResponse(BaseModel):
    conversion_probability: float
    will_convert: bool

@app.post("/predict", response_model=PredictionResponse)
def predict(lead: Lead):
    lead_dict = lead.model_dump()
    prob = float(pipeline.predict_proba([lead_dict])[0, 1])

    return PredictionResponse(
        conversion_probability=prob,
        will_convert=prob >= 0.5
    )