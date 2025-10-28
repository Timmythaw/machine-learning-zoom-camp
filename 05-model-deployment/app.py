import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Load pipeline
with open('pipeline_v1.bin', 'rb') as f:
    pipeline = pickle.load(f)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9696)