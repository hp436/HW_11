import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.calculation import Base, Calculation

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/testdb"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_insert_calculation():
    db = TestingSessionLocal()
    calc = Calculation(a=3, b=2, type="Add", result=5)
    db.add(calc)
    db.commit()

    obj = db.query(Calculation).first()
    assert obj.result == 5

