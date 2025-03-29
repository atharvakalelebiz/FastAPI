from sqlalchemy.orm import Session
from models import Translation
import schemas

def create_translation(db : Session, original_text: str, translated_text:str):
    db_translation = Translation(original_text=original_text, translated_text=translated_text)
    db.add(db_translation)
    db.commit()
    db.refresh(db_translation)
    return db_translation