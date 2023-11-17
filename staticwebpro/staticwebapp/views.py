from django.shortcuts import render

# Create your views here.
from .models import place

from .models import team
def demo(request):
    obj = place.objects.all()
    objteam=team.objects.all()
    return render(request, "index.html", {'result': obj,'resultteam':objteam})
