"""
This file consists of firebase_admin initialization for app
"""
from fastapi import APIRouter
from fastapi import FastAPI, Response
import firebase_admin
from firebase_admin import credentials, firestore
from pathlib import Path

import os
import json

fb_app = firebase_admin.initialize_app()

import google.cloud.logging
client = google.cloud.logging.Client()

logger_name = 'tag_counter_logs'
logger = client.logger(logger_name)
entry = {'config_set_up' : 'Complete'}
logger.log_struct(entry)



app = FastAPI()
