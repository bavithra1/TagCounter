"""
This file consists of services for tags module
"""
from database.dbcontext import db
from schema.tags_schema import Tag
from firebase_admin import credentials, firestore
from config.config import logger
import json

async def get_all_tags( next_start_tag = None, limit = 1000):
    '''
    This function returns all tags in dictionary format
    '''
    tags = {}
    if next_start_tag is None:
        tags_collection = db.collection('tags').order_by(u'name').limit(limit)
    else:
        tags_collection = db.collection('tags').order_by(u'name').start_after({
        u'name': next_start_tag}).limit(limit)
        
    last_doc = None
    for tag in tags_collection.get():
        tag = tag.to_dict()
        tags[tag['name']] =  tag['value']
        last_doc = tag['name']
    result = {'tags' : tags, 'next_start_tag' : last_doc}
    return result

async def get_tag(tag: Tag):
    '''
    This function returns a document reference
    '''
    doc_ref = db.collection('tags').document(tag.name)
    return doc_ref

async def update_counter(doc_ref, tag: Tag):
    try:
        batch = db.batch()
        batch.update(doc_ref, {"value": firestore.Increment(tag.value)})
        #doc_ref.update({"value": firestore.Increment(tag.value)})
        await update_tag_total_count_metrics(tag.value, batch)
        batch.commit()
        await get_total_count_metrics()
        return {'content' : {"Message" : "Tag Count Incremented"}, 'status_code' : 200 }
    except Exception as e:
        return {'content' : {"Message" : "Error updating counter"}, 'status_code' : 500 }

async def create_counter(tag: Tag):  
    try:
        batch = db.batch()
        doc_ref = await get_tag(tag)
        batch.set(doc_ref, {"name":tag.name, "value":tag.value})
        #doc_ref.set({"name":tag.name, "value":tag.value})
        await update_tag_total_count_metrics(tag.value, batch)
        batch.commit()
        await get_total_count_metrics()
        return {'content' : {"Message" : "Tag Count Created"}, 'status_code' : 201 }
    except Exception as e:
        return {'content' : {"Message" : "Error creating counter"}, 'status_code' : 500 }

async def update_tag_total_count_metrics(tag_count, batch):
    '''
    This function is used to update the tag total count
    '''
    try:
        print("Tag Count Given ", tag_count)
        doc_ref = db.collection('metrics').document("tags_total_count")
        
        batch.update(doc_ref, {"value": firestore.Increment(tag_count)})
    except Exception as e:
        raise Exception("Error updating count")
    
async def get_total_count_metrics():
    try:
        doc_ref = db.collection('metrics').document("tags_total_count")
        doc = doc_ref.get()
        tag = doc.to_dict()
        if doc.exists:
            print("Total Count", tag['value'])
            entry = {'desc' : 'total_tag_count_desc',
                    'total_tag_count' : tag['value']
                    }
            logger.log_struct(entry)
            
        else:
            raise Exception("Total Count Unavailable")
    except Exception as e:
        raise Exception("Error while getting  count")
    