import os
from dotenv import load_dotenv
load_dotenv()

gitter_token = os.getenv('GITTER_TOKEN')
gitter_community = os.getenv('GITTER_COMMUNITY')
gitter_channel = os.getenv('GITTER_CHANNEL')
