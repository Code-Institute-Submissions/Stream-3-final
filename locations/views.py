from django.shortcuts import render
from models import mapDetails
from .serializer import mapDetailsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

def get_locations(request):
    #https://maps.googleapis.com/maps/api/staticmap?center={{map.address}}&zoom={{map.zoom}}&size={{mapDimensions()}}&markers=color:red|{{map.address}}
    map_Details = mapDetails.objects.all()
    serializer = mapDetailsSerializer(map_Details, many=True)
    #content = JSONRenderer().render(serializer.data)
    content = serializer.data
    for mylist in content:
        print "mylist:",mylist

    print "myArray:",content
    args = {'myArray': content, 'map_details': map_Details}
    return render(request, 'locations.html', args)
