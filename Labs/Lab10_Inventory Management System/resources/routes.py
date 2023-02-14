from .resources import inventoryApi,deleteInventoryApi,searchInventory,updateApi

def initalize_routes(api):
    api.add_resource(inventoryApi, '/api/inventory')
    # api.add_resource(deleteInventoryApi, '/api/delinventory/<id>')
    api.add_resource(updateApi, '/api/updateInv/<name>')
    # api.add_resource(searchInventory, '/api/search/<name>')
    api.add_resource(searchInventory, '/api/searchInventory')



