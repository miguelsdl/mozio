from django.http import HttpResponseRedirect
from rest_framework import viewsets
from api.serializers import ProviderSerializer, ServiceAreaSerializer
from api.models import Provider, ServiceArea
from rest_framework.response import Response
from django.contrib.gis.geos import GEOSGeometry
import json


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def list(self, request):
        queryset = ServiceArea.objects.all()
        serializer = ServiceAreaSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        name = request.POST.get('name')
        price = request.POST.get('price')
        provider = request.POST.get('provider', None)
        area = json.loads(request.POST.get('polygon'))
        coordinates = area.get('coordinates')[0]
        polygon_new = list()

        for coor in coordinates:
            polygon_new.append("{} {}".format(coor[0], coor[1]))

        polygon = "POLYGON(({}))".format(", ".join(polygon_new))
        geo_polygon = GEOSGeometry(polygon)

        o = ServiceArea(name=name, price=price, provider=provider if provider else None, polygon=geo_polygon)
        o.save()

        return HttpResponseRedirect(redirect_to='/api/polygon/')
