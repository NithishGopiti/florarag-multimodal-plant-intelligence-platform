from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

Base = declarative_base()

class PlantDiagnosis(Base):

    __tablename__ = "plant_diagnosis"

    id = Column(Integer, primary_key=True)

    plant_name = Column(String(120))
    disease_name = Column(String(120))

    diagnosis_result = Column(Text)
    recommendation = Column(Text)

class DiseaseKnowledge(Base):

    __tablename__ = "disease_knowledge"

    id = Column(Integer, primary_key=True)

    disease_name = Column(String(120))
    symptoms = Column(Text)
    treatment = Column(Text)
