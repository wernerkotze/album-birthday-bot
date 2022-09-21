# import configparser
# import datetime
# import spotipy
# import spotipy.oauth2 as oauth2
# import numpy as np
# import lyricsgenius
# import pandas as pd 
# import random
# import requests
# import json
# import urllib
# import os
import ssl
# import unicodedata
# import math

# from nider.core import Font
# from nider.core import Outline

# from nider.models import Content
# from nider.models import Linkback
# from nider.models import Paragraph
# from nider.models import Image as Image
# from PIL import Image as Image2
# from PIL import ImageStat

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

# config = configparser.ConfigParser()
# config.read('config.cfg')
# client_id = config.get('SPOTIFY', 'CLIENT_ID')
# client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
# genius_access_key = config.get('GENIUS', 'ACCESS_TOKEN')

# auth = oauth2.SpotifyClientCredentials(
#     client_id=client_id,
#     client_secret=client_secret
# )

# token = auth.get_access_token()
# spotify = spotipy.Spotify(auth=token)

app = FastAPI()

artists = [
	{
		"id": "1",
		"name": "6LACK"
	},
	{
        "id": "2",
        "name": "blink-182"
    }
]


todos = [
    {
        "id": "1",
        "item": "Read a book."
    },
    {
        "id": "2",
        "item": "Cycle around town."
    }
]

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/", tags=["root"])
async def read_root() -> dict:
	return {"message": "Welcome to the best album birthday generator on the internet!"}

@app.get("/todo", tags=["todos"])
async def get_todos() -> dict:
	return { "data": todos }

@app.get("/artists", tags=["artists"])
async def get_artists() -> dict:
	return { "data": artists }
