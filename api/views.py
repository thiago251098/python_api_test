from django.shortcuts import render
import requests
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import logging
from rest_framework import permissions


class OpenBreweries(APIView):

    URL = "https://api.openbrewerydb.org/breweries/"

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):

        ret = requests.get(url=self.URL)

        if ret.status_code != 200:
            response_error(
                f"error in the api {self.URL}", error_code=ret.status_code)

        beer_dict = {"names_beer": []}
        for beer in ret.json():
            beer_dict["names_beer"].append(beer["name"])

        return Response(beer_dict)


class PostChallenge(APIView):

    logger_error = logging.getLogger('django-error')

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            ret_dict = {"user": str(request.data["User"]), "Order": float(
                request.data["Order"]), "PreviousOrder": bool(request.data["PreviousOrder"])}
        except Exception as err:
            self.logger_error.error(err)
        return Response(ret_dict)


def response_error(error_message, error_code=0):
    data = {"error": error_message}
    if error_code != 0:
        data["error_code"] = error_code

    return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
