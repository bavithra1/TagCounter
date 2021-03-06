# Tag Counter

#Tech Stack: FastApi, FireStore Google Cloud


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

<img width="761" alt="Screen Shot 2021-05-10 at 8 32 37 PM" src="https://user-images.githubusercontent.com/62027571/117754289-e3504500-b1ce-11eb-9705-8ee500928ac9.png">

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

Screen Shot 2021-05-10 at 8.25.49 PM![image](https://user-images.githubusercontent.com/62027571/117753811-f7e00d80-b1cd-11eb-997d-d68a9160e369.png)

Screen Shot 2021-05-10 at 8.22.28 PM![image](https://user-images.githubusercontent.com/62027571/117753596-9881fd80-b1cd-11eb-83a0-78178ace9853.png)

Google Cloud Run

https://tag-counter-service-i6hyr7jqka-wl.a.run.app

<img width="1386" alt="Screen Shot 2021-05-10 at 8 38 24 PM" src="https://user-images.githubusercontent.com/62027571/117754710-bc464300-b1cf-11eb-91f8-13a33c74d52f.png">


TO Explore:

More test cases and testing with jmeter/locust

Log Structure

Refactoring Service File

batch (used)

Pub/Sub

Distributed Counter to reconsider the document structure


## License
[MIT](https://choosealicense.com/licenses/mit/)
