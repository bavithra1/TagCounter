"""
This file consists of placeholder for all routers
"""
from fastapi import APIRouter
from api import tags_api, home_api
router =  APIRouter()
router.include_router(tags_api.router)
router.include_router(home_api.router)