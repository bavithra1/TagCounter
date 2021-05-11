"""
This file consists of apis for tags module
"""
from fastapi import FastAPI, Response, HTTPException
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services import tags_service
from database.dbcontext import db
from schema.tags_schema import Tag
from fastapi.responses import JSONResponse, HTMLResponse
from typing import Optional
router = APIRouter()


@router.get("/tags", response_description="All Tags" )
async def get_tag_stats(next_start_after: Optional[str] = None, limit : int = 1000 ):
    if limit > 1000:
        raise HTTPException(status_code=400, error_message="Limit cannot exceed 1000")

    tags = await tags_service.get_all_tags(next_start_after, limit)
    if tags:
        return JSONResponse(content = tags)
    else:
        raise HTTPException(status_code=404, error_message="Tags not Found")


@router.post('/tags', response_model=Tag, response_description="Increment Value for tags" )
async def increment_count(tag: Tag):
    doc_ref = await tags_service.get_tag(tag)
    response = {}
    if doc_ref and doc_ref.get().exists:
        response = await tags_service.update_counter(doc_ref, tag)
    else: 
        response = await tags_service.create_counter(tag)
    return JSONResponse(content = response["content"], status_code = response["status_code"])

    