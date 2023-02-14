from flask import request, Response, jsonify
from flask_restful import Resource
from database.models import inventory,Contacts


class inventoryApi(Resource):
    def get(self):
        obj = inventory.objects().to_json()
        print(obj)
        return Response(obj, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        print(body)
        inv = inventory(**body).save()
        # inv=inventory(name=body["name"],description=body["description"],price=body["price"]).save()
        id = inv.id
        return {'id': str(id), 'post': 'successful'}, 200

class updateApi(Resource):

    def put(self, name):
        reqdata = request.get_json()
        inventory.objects.get(name=name).update(**reqdata)
        return {'id': str(id), 'update': 'successful'}, 200


class deleteInventoryApi(Resource):
    def delete(self, id):
        inventory.objects.get(id=id).delete()
        return {'id': str(id), 'delete': 'done'}, 200

    def put(self, id):
        reqdata = request.get_json()
        inventory.objects.get(id=id).update(**reqdata)
        return {'id': str(id), 'update': 'successful'}, 200


    # def get(self):
    #     n = request.args.get("name")
    #     des = request.args.get("description")
    #     obj=inventory.objects(name=n,description=des),to_json()
    #     return Response(obj, mimetype="application/json", status=200)
class searchInventory(Resource):
    # def get(self, name):
    #     item = inventory.objects.get(name=name).to_json()
    #     return Response(item, mimetype="application/json", status=200)

    def get(self):
        n1 = request.args.get("n1")
        n2 = request.args.get("n2")
        obj=inventory.objects(name__in=[n1,n2])
        return Response(obj, mimetype="/application/json", status=200)





