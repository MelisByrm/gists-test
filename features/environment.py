import os
from dotenv import load_dotenv

def before_all(context):
    load_dotenv()

    context.GIST_ACCESS_TOKEN = os.getenv('GIST_ACCESS_TOKEN')