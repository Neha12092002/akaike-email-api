
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils import mask_pii
from fastapi.responses import JSONResponse

app = FastAPI()

# Load model and vectorizer
model = joblib.load("email_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

class EmailInput(BaseModel):
    email: str

@app.post("/classify-email")
def classify_email(input: EmailInput):
    email_text = input.email
    masked_email, entities = mask_pii(email_text)
    vectorized = vectorizer.transform([masked_email])
    category = model.predict(vectorized)[0]

    return JSONResponse(content={
        "input_email_body": email_text,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    })
