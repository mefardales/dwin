import os
from rich import print as rprint
from api.render import RenderCloud

TOKEN_RENDER = os.getenv('TOKEN_RENDER')
BASE_URL = 'https://api.render.com/v1'
RENDER_URL = 'https://api.render.com/v1/services?limit=20'
PAYLOAD = {
    'url': RENDER_URL,
    'data': {
        'header': {'Accept': 'application',
        'Authorization': f'Bearer {TOKEN_RENDER}'}   
    }
}   

response = RenderCloud(data=PAYLOAD)
rprint(response.authentication())