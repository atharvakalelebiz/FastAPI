from fastapi import FastAPI, HTTPException
from openai import OpenAI
import os 
from dotenv import load_dotenv
import schemas
import crud
import database
from sqlalchemy.orm import Session
from fastapi import Depends
import models

load_dotenv()

client = OpenAI(
    base_url="https://beta.sree.shop/v1",
    api_key="ddc-beta-bnsvvfd1nx-OpH3p78LEiLmJRbTnylkWEazAn0Pwnrqt1L"
)

app = FastAPI(title = "English to Hindi Translator")
models.create_tables()
@app.post("/translate", response_model = schemas.TranslationResponse)
async def translate_text(request: schemas.TranslationRequest, db:Session = Depends(database.get_db)):
    try:
        response = client.chat.completions.create(
            model = "Provider-7/gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a translator. Translate English to Hindi accurately."},
                {"role": "user", "content": f"Translate this English text to Hindi: {request.text}"}
            ],
        )
        translated_text = response.choices[0].message.content.strip()
        crud.create_translation(db, original_text=request.text, translated_text=translated_text)
        return{
            "original_text": request.text,
            "translated_text": translated_text
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Translation failed. Please try again later."
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)