from student import serialize
from student.models import DetailsModel
from student.serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics

class ListAPI(generics.ListAPIView):
    queryset = DetailsModel.objects.all()
    serializer_class = DetailsSerializer

    def post(self,request):
        serializeobj=DetailsSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(1)
        return Response(serializeobj.errors)

class DetailsUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetailsModel.objects.all()
    serializer_class = DetailsSerializer
    
       

























































# class DetailsDelete(APIView):
#     def get(self,request,pk):
#         try:
#             detailObj=DetailsModel.objects.get(pk=pk)
#         except:
#             return Response("Not Found in Database")
#         detailObj.delete()
#         return Response('successfuly deleted')


# class DetailsTable(APIView):
#     def get(self,request):
#         detailsObj=DetailsModel.objects.all()
#         dlSerializeObj=DetailsSerializer(detailsObj,many=True)
#         return Response(dlSerializeObj.data)






















# class DetailsDelete(APIView):
#     def get(self,request,pk):
#         try:
#             detailObj=DetailsModel.objects.get(pk=pk)
#         except:
#             return Response("Not Found in Database")
#         detailObj.delete()
#         return Response('successfuly deleted')