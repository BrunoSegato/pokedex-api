from pokedex.app import Application
from pokedex.middlewares import middlewares
from pokedex.routers import routers

app = Application(routers, middlewares)
