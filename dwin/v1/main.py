import os
from rich import print as rprint
from dwin.v1 import RenderCloud
from dwin.v1 import settings

response = RenderCloud(data=settings)
rprint(response.authentication())