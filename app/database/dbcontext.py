"""
This file consists of db handler
"""

from firebase_admin import credentials, firestore
db = firestore.client()
transaction = db.transaction()
