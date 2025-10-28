import pickle

# Load pipeline
with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

# Test data from question 3
client = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

# Make prediction
probability = pipeline.predict_proba([client])[0, 1]
print(f"Predicted probability of enrollment: {probability:.3f}")