"""
This file consists of overview of end points
"""
from fastapi import FastAPI, Response
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services import tags_service
from database.dbcontext import db
from schema.tags_schema import Tag
from fastapi.responses import JSONResponse, HTMLResponse
from config import config
from firebase_admin import credentials, firestore

router = APIRouter()


@router.get("/", response_description="Read Me" )
async def index():
    body = """
        <html>
        <h1> <u> Tag Api Details </u> </h1>
        <h2> Supported Api </h2>
        <ul>
        <li> Get Tag Stats : /tags</li>
        <li> Increment Count: /tags</li>
        <li> Documentation: /docs </li>
        </ul>
        <div>
        <h3>
        Tag Counter
        </h3>

<span style="white-space: pre;">
Tag Counter consists of api end points

1. Get Tag Stats:

An endpoint that will return the current incremented counts for all stored tags.

Input:

     a. Limit for each fetch is set at 1000

     b.  Optional Parameter: next_start_after. If this parameter is provided, records after this tag name will be fetched

Output:
   
Format: Json
e.g.
{
  "tags": {
    "ab_": 0,
    "april": 4,
    "bar": 4,
    "dfe": 11,
    "dowe": 7,
    "foo": 63,
    "fopp": 2,
    "orange": 5,
    "test": 3
  },
  "next_start_tag": "test"
}

2. Increment Count

An endpoint that can receive a JSON body payload request that contains a tag name and value.


Validations:

This value is to be added to the current value stored for that tag (default start being 0). ==>

"If a tag name is present, it will increment the value.

If a tag name is not present, new tag with given value will be inserted"

The tag name will be a string that conforms to [a-z_]{3,15}


The value can be any positive integer (less than 10)

# Collections and Documents
Collection : tags
Document with id = tag name
Field: 'name': "ab_"
        'value': 2

Collection: metrics
Document with id = 'tags_total_count'
Field: 'value': ##total e.g. 5 ##

# File Structure

-- TAGCOUNTER

    -- app

        -- api

          #api endpoints placeholder

        -- config

          #configuration and initialization

        -- database

          #db handler

        -- schema

          #Pydantic models

        -- services

          #controllers for api endpoints

        -- tests
        
          #test cases

Logs in Json Payload under global resource type
User defined Log based metric created with filter total_tag_count_desc
TO Explore:
More test cases and testing with jmeter/locust
Log Structure
Refactoring Service File
batch (used)
Pub/Sub
Distributed Counter to reconsider the document structure



## License
[MIT](https://choosealicense.com/licenses/mit/)
  
</span>
        </html>
    """
    return HTMLResponse(content = body)