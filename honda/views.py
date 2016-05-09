from django.views.generic.base import TemplateView
from rest_framework import viewsets
from serializers import MotorSerializer
from models import Motor


# Create your views here.
class MotorView(TemplateView):
    template_name = 'index.html'


class MotorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Motor.objects.all()
    serializer_class = MotorSerializer
