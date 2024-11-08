from .extentions import api
from .apis import HomeResource

api.add_resource(HomeResource,'/','/home')