from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from florarag_settings import florarag_settings

DATABASE_URL = (
    f"mysql+pymysql://{florarag_settings.MYSQL_USER}:"
    f"{florarag_settings.MYSQL_PASSWORD}@"
    f"{florarag_settings.MYSQL_HOST}:"
    f"{florarag_settings.MYSQL_PORT}/"
    f"{florarag_settings.MYSQL_DATABASE}"
)

flora_engine = create_engine(
    DATABASE_URL,
    pool_size=30,
    max_overflow=60,
    pool_pre_ping=True
)

FloraSession = sessionmaker(
    bind=flora_engine,
    autocommit=False,
    autoflush=False
)
