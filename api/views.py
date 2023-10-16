from rest_framework import status
from rest_framework.views import APIView, Response
from .models import Item
from .serializers import ItemSerializer


class DumpItAPI(APIView):

    def get(self, request):
        items = Item.objects.all()
        print("===>donnees get non serialise", items)
        items_data = ItemSerializer(items, many=True).data
        print("===>donnees get serialise", items_data)
        response_data = {"datas": items_data}
        print("===>Dictionnair avec donnees get serialise", response_data)
        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data.get('name')
        item = Item.objects.create(name=name)
        print("====>Donnees post serialise", item)
        response_data = {"response": "item created"}
        return Response(response_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        name = request.data.get('name')
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response": "Item doesnot exists"}
            return Response(response_data, status.HTTP_404_NOT_FOUND)
        item.name = name
        item.save()
        response_data = {"response": "object is updated sucefull"}
        return Response(response_data, status.HTTP_200_OK)

    def delete(self, request, id):
        item = Item.objects.filter(id=id).first()
        if item is None:
            response_data = {"response": "Item doesnot exists"}
            return Response(response_data, status.HTTP_404_NOT_FOUND)
        item.delete()
        response_data = {"response": "item Deleted"}
        return Response(response_data, status.HTTP_200_OK)
