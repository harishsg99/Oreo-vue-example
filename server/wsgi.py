from oreoweb import App, configure, discover_providers

from . import settings
from .router import router

discover_providers("server.providerconf")

app = Oreoweb()
app.include_router(router)
configure(app, settings)
