# Backend server for DriverSafetyApp
# Provides endpoints for ML predictions
# You can later integrate fatigue detection models here

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Backend running"}

@app.post("/predict")
def predict():
    # Placeholder response until ML model added
    return {"alert": False, "message": "Model not implemented yet"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
