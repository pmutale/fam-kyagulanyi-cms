from django.contrib.auth import authenticate
from django.http import JsonResponse
from requests import Response
from rest_framework import status
from rest_framework.views import APIView


class LoginView(APIView):
    permission_classes = ()

    def post(self, request):
        response = {"token": False, "status": False, "error": False}
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        # try:
        if user:
            try:
                response["token"] = user.auth_token.key
                response["status"] = status.HTTP_200_OK
                return JsonResponse(response)
            except Exception as e:
                response["error"] = str(e)
                return JsonResponse(response)
        else:
            response["error"] = 'No username or password supplied' if not username or password else 'Wrong credintials'
            response["status"] = status.HTTP_400_BAD_REQUEST
            return JsonResponse(response)
