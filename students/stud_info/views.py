from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Students
from .serializers import studentSerializer

class Get_students_List(APIView):
    def get(self, request):
        students_data = request.GET.get("id") #JSONParser().parse(request)
        if(students_data):
            students = Students.objects.get(id=students_data)
            serialized = studentSerializer(students)
            return Response(serialized.data)
        else:
            students = Students.objects.all()
            serialized = studentSerializer(students, many=True)
            return Response(serialized.data)
            
        return Response('Error')

    def post(self, request):
        students_data = JSONParser().parse(request)
        serializer=studentSerializer(data=students_data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added Successfully")
        return Response("Failed")

    def put(self, request):
        students_data = JSONParser().parse(request)
        students = Students.objects.get(id=students_data['id'])
        serializer=studentSerializer(students,data=students_data)
        if serializer.is_valid():
            serializer.save()
            return Response("Updated Successfully")
        return Response("Failed")

    def delete(self, request):
        students_data = JSONParser().parse(request)
        student = Students.objects.get(id=students_data['id'])
        student.delete()
        return Response("Deleted Successfully")
        
def homepage(request):
    return render(request, 'index.html')

def insertpage(request):
    return render(request, 'insert.html')

def deletepage(request):
    return render(request, 'delete.html')

def updatepage(request):
    return render(request, 'update.html')
