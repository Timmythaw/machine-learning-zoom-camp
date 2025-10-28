import requests

url = "http://localhost:9696/predict"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client)
result = response.json()
print(f"Conversion Probability: {result['conversion_probability']:.3f}")
print(f"Will Convert: {result['will_convert']}")