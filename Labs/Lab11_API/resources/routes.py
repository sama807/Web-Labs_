from .resources import inventoryApi,deleteInventoryApi,searchInventory,ContactsAPI,ContactCRUDAPI

def initalize_routes(api):
    api.add_resource(inventoryApi, '/api/inventory')
    api.add_resource(deleteInventoryApi, '/api/delinventory/<id>')
    # api.add_resource(searchInventory, '/api/search/<name>')
    api.add_resource(searchInventory, '/api/searchInventory')
    api.add_resource(ContactsAPI, "/api/contacts")
    api.add_resource(ContactCRUDAPI,"/api/contacts/<id>")


