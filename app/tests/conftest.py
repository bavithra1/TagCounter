"""
This file consists of common testing elements
"""
import sys
import os
import pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
from fastapi import FastAPI
from config import config
from fastapi.testclient import TestClient
from api.root_api import router

@pytest.fixture(scope="function")
def client():
    app = config.app
    app.include_router(router)
    with TestClient(app) as client:
        yield client