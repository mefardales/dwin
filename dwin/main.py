import os
from rich import print as rprint
from api.render import RenderCloud
from config import settings


response = RenderCloud(data=settings)
rprint(response.authentication())