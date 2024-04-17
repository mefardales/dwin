import os

# CONFIG RENDER CLOUD

TOKEN_RENDER = os.getenv('TOKEN_RENDER')
RENDER_URL = 'https://api.render.com/v1'

settings = {
    'url': RENDER_URL,
    'data': {
        'header': {'Accept': 'application',
        'Authorization': f'Bearer {TOKEN_RENDER}'}   
    },
    'rate_limit': 40, # https://api-docs.render.com/reference/rate-limiting
}   
