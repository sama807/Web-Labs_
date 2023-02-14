from .resources import UserApi, Verified

def initializeRoutes(api):
    api.add_resource(UserApi,'/api/user')
    api.add_resource(Verified,'/api/verify')