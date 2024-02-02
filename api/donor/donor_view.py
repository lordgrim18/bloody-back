from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.models import Donor
from .donor_serializer import DonorCreateSerializer, DonorListSerializer


class DonorAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        JWT_authenticator = JWTAuthentication()
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            # unpacking
            user , token = response
            user_id = token.payload['user_id']

        serializer = DonorCreateSerializer(data=request.data, context={"request": request, "user_id": user_id})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "successfully created donor", "response": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "failed to create donor", "response": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        donors = Donor.objects.all()
        serializer = DonorListSerializer(donors, many=True)
        return Response({"message": "successfully fetched donors", "response": serializer.data}, status=status.HTTP_200_OK)