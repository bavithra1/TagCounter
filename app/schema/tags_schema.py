"""
This file consists of pydantic schemas for tags module
"""
from pydantic import BaseModel, constr, conint

class Tag(BaseModel):
    name : constr(min_length = 3, max_length = 15, regex=r'^[a-z_]{3,15}$')
    value : conint(gt=0, lt=10)

class ResponseTag(BaseModel):
    name : constr(min_length = 3, max_length = 15, regex=r'^[a-z_]{3,15}$')
    value : conint(gt=0, lt=10)

