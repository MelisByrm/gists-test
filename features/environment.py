import os

from dotenv import load_dotenv

from utils.helpers.api_base import APIBase


def before_all(context):
    load_dotenv()
    context.VALID_GIST_TOKEN = os.getenv('VALID_GIST_TOKEN')
    context.INVALID_GIST_TOKEN = os.getenv('INVALID_GIST_TOKEN')
    context.WITHOUT_PERMISSION_GIST_TOKEN = os.getenv('WITHOUT_PERMISSION_GIST_TOKEN')
    context.api = APIBase()

def before_scenario(context, scenario):
    context.access_token = None
    context.response = None

def before_step(context, step):
    context.current_step = step.name