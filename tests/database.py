from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
from app.config import settings
from app.database import Base, get_db

#SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:Lawrence19981123@localhost:5432/fastapi_Sanjeev_test"

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        
@pytest.fixture()
def session():
    Base.metadata.drop_all(bind=engine)   # drop table on the db:fastapi_Sanjeev_test
    Base.metadata.create_all(bind=engine) # create table on the db:fastapi_Sanjeev_test
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db    
    yield TestClient(app) 