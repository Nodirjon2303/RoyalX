from django.shortcuts import render

from .serializer import *
from rest_framework.response import Response
from rest_framework import viewsets


class Reason_view(viewsets.ModelViewSet):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer


class Student_view(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class Teacher_view(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def list(self, request, *args, **kwargs):
        queryset = Reja_teacher.objects.all()
        teacher = Teacher.objects.all()
        data = []
        for i in teacher:
            print('photo',  'aaaaaaaa')
            reja = []
            datas = {}
            for j in Reja_teacher.objects.filter(teacher=i):
                reja.append(j.reja)
            datas = {
                'name':i.full_name,
                'job':i.job,
                'description':i.description,
                'reja': reja,
                'shior': i.shior,
                'rasm': str(i.photo.path)
            }
            data.append(datas)
        return Response(data)

class Contact_view(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
