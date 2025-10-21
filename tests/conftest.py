import os
import sys
app_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(app_dir)

from database import SessionLocal
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import StaticPool
from sqlalchemy.orm.session import Session, sessionmaker
from models import Base, Item
from schemas import DecodedToken



@pytest.fixture()
def session_fixture():
    engine = create_engine(
        url="sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool
    )
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        item1 = Item(name="PC1", price=10000, description="test1", user_id="1")
        item2 = Item(name="PC2", price=10000, description="test2", user_id="2")
        db.add(item1)
        db.add(item2)
        db.commit()
        yield db
    finally:
        db.close()

@pytest.fixture()
def user_fixture():
    return DecodedToken(username="user1", user_id=1)