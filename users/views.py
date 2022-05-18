from django.core.mail import send_mail
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *


# Create your views here.
class CreateCoach(APIView):
   def post(self, request, format=None):
        result = {}
        result['status'] = 'NOK'
        result['valid'] = False
        result["result"] = {'message': 'Unauthorized', 'data': []}
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',  #--From email should be here--#
            ['to@example.com'],  #--To email should be here--#
            fail_silently=False,)
            result = {}
            result['status'] = 'OK'
            result['valid'] = True
            result["result"] = {'message': 'User created successfully'}
            return Response(result, status.HTTP_200_OK)
        return Response(result, status.HTTP_401_UNAUTHORIZED)

class CreateCoachee(APIView):
   def post(self, request, format=None):
        result = {}
        result['status'] = 'NOK'
        result['valid'] = False
        result["result"] = {'message': 'Unauthorized', 'data': []}
        name = request.data['name']
        email = request.data['email']
        password = request.data['password']
        pic = request.data['pic']
        phone = request.data['phone']
        data = Coachees.objects.create(name=name,email=email,password=password,pic=pic,phone=phone)
        if data:
            result = {}
            result['status'] = 'OK'
            result['valid'] = True
            result["result"] = {'message': 'User created successfully'}
            return Response(result, status.HTTP_200_OK)
        return Response(result, status.HTTP_401_UNAUTHORIZED)

class GetCoaches(APIView):
    def post(self, request, format=None):
        result = {}
        result['status'] = 'OK'
        result['valid'] = True
        coach_id = request.data['coach_id']
        data = Coaches.objects.filter(id=coach_id).all().values()
        if data:
            result["result"] = {'message': 'Details got successfully', 'data': data}
            return Response(result, status.HTTP_200_OK)
        result["result"] = {'message': 'No data found', 'data': []}
        return Response(result, status.HTTP_204_NO_CONTENT)

class GetCoachees(APIView):
    def post(self, request, format=None):
        result = {}
        result['status'] = 'OK'
        result['valid'] = True
        coach_id = request.data['coach_id']
        data = Coachees.objects.filter(id=coach_id).all().values()
        if data:
            result["result"] = {'message': 'Details got successfully', 'data': data}
            return Response(result, status.HTTP_200_OK)
        result["result"] = {'message': 'No data found', 'data': []}
        return Response(result, status.HTTP_204_NO_CONTENT) 

class UpdateCoach(APIView):
   def patch(self, request, format=None):
        result = {}
        result['status'] = 'NOK'
        result['valid'] = False
        result["result"] = {'message': 'Unauthorized', 'data': []}
        data = Coaches.objects.filter(id=Coaches.objects.latest('id').id).update(
            name = request.data['name'],
            email = request.data['email'],
            password = request.data['password'],
            pic = request.data['pic'],
            linked_in = request.data['linked_in'],
            charge = request.data['charge'],
            certi = request.data['certi'],
        )
        if data:
            result = {}
            result['status'] = 'OK'
            result['valid'] = True
            result["result"] = {'message': 'User updated successfully'}
            return Response(result, status.HTTP_200_OK)
        return Response(result, status.HTTP_401_UNAUTHORIZED)

class UpdateCoachee(APIView):
   def patch(self, request, format=None):
        result = {}
        result['status'] = 'NOK'
        result['valid'] = False
        result["result"] = {'message': 'Unauthorized', 'data': []}
        data = Coachees.objects.filter(id=Coachees.objects.latest('id').id).update(
            name = request.data['name'],
            email = request.data['email'],
            password = request.data['password'],
            pic = request.data['pic'],
            phone = request.data['phone'],
        )
        if data:
            result = {}
            result['status'] = 'OK'
            result['valid'] = True
            result["result"] = {'message': 'User updated successfully'}
            return Response(result, status.HTTP_200_OK)
        return Response(result, status.HTTP_401_UNAUTHORIZED)

class DeleteCoachee(APIView):
   def delete(self, request, format=None):
        result = {}
        result['status'] = 'NOK'
        result['valid'] = False
        result["result"] = {'message': 'Unauthorized', 'data': []}
        data = Coachees.objects.filter(id=Coachees.objects.latest('id').id).delete()
        if data:
            result = {}
            result['status'] = 'OK'
            result['valid'] = True
            result["result"] = {'message': 'User deleted successfully'}
            return Response(result, status.HTTP_200_OK)
        return Response(result, status.HTTP_401_UNAUTHORIZED)

class DeleteCoach(APIView):
   def delete(self, request, format=None):
        result = {}
        result['status'] = 'NOK'
        result['valid'] = False
        result["result"] = {'message': 'Unauthorized', 'data': []}
        data = Coaches.objects.filter(id=Coaches.objects.latest('id').id).delete()
        if data:
            result = {}
            result['status'] = 'OK'
            result['valid'] = True
            result["result"] = {'message': 'User deleted successfully'}
            return Response(result, status.HTTP_200_OK)
        return Response(result, status.HTTP_401_UNAUTHORIZED)

