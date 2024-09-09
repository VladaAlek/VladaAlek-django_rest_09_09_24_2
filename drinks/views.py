#from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.
def drink_list(request):

    # get all the drinks
    # serialize them
    # return JSON
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)
    return JsonResponse({"drinks": serializer.data}, safe=False)
