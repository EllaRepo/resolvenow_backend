from django.http import JsonResponse
from api.models import User, Complaint, CompTypes, Region

from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer, ComplaintSerializer, MyTokenObtainPairSerializer2

from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenObtainPairView2(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer2

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ComplaintView(generics.CreateAPIView):
    queryset = Complaint.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ComplaintSerializer
    

# Get All Routes

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/register/',
        '/api/token/refresh/'
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    if request.method == 'GET':
        data = f"Congratulation {request.user}, your API just responded to GET request"
        return Response({'response': data}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = "Hello buddy"
        data = f'Congratulation your API just responded to POST request with text: {text}'
        return Response({'response': data}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getRegions(request, email=None):
    print(email)
    if request.method == 'GET':
        region = []
        for obj in Region.objects.all():
            region.append(obj.__dict__['name'])
        print(region)
        return Response({'response': region}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCompTypes(request):
    if request.method == 'GET':
        ctypes = []
        for obj in CompTypes.objects.all():
            ctypes.append(obj.__dict__['name'])
        print(ctypes)
        return Response({'response': ctypes}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes([IsAuthenticated])
def complaints(request, email=None):
    print(email)
    if request.method == 'GET':
        cmplts = []
        for obj in Complaint.objects.all():
            if obj.__dict__['email'] == email:
                cmplts.append(obj.to_dict())
        return Response({'response': cmplts}, status=status.HTTP_200_OK)
    return Response({}, status.HTTP_400_BAD_REQUEST)