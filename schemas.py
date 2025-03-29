from pydantic import BaseModel

class TranslationRequest(BaseModel):
    text : str

class TranslationResponse(BaseModel):
    original_text : str
    translated_text : str

