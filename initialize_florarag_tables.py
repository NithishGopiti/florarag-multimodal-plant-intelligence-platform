from florarag_database_connection import flora_engine
from florarag_models import Base

def initialize_tables():
    Base.metadata.create_all(bind=flora_engine)

if __name__ == "__main__":
    initialize_tables()
