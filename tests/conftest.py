import os
import sys
app_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(app_dir)

import pytest
from sqlalchemy import create_engine


@pytest.fixture()
def session_fixture():
    engine = create_engine(
        url="sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool

        
    )