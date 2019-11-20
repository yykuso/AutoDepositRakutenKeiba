import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

RakutenKeiba_ID = os.environ.get("RakutenKeiba_ID")
RakutenKeiba_PW = os.environ.get("RakutenKeiba_PW")
RakutenKeiba_PIN = os.environ.get("RakutenKeiba_PIN")
RakutenKeiba_DEP = os.environ.get("RakutenKeiba_DEP")
