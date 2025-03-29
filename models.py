from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from database import Base
from database import engine

class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)
    translated_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Translation(id={self.id}, original_text={self.original_text}, translated_text={self.translated_text})>"
    

def create_tables():
    Base.metadata.create_all(bind=engine)
