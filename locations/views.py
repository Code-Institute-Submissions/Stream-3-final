from django.shortcuts import render
from models import mapDetails
from .serializer import mapDetailsSerializer


def get_locations(request):
    map_Details = mapDetails.objects.all()
    serializer = mapDetailsSerializer(map_Details, many=True)
    content = serializer.data
    for mylist in content:
        print "mylist:",mylist
    print "myArray:",content
    args = {'myArray': content, 'map_details': map_Details}
    return render(request, 'locations.html', args)
