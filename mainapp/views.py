from .tasks import test_funct
from django.http import HttpResponse


# Create your views here.
def test(request):
    test_funct.delay()
    return HttpResponse("Done")


def index(request):
    return HttpResponse("Index")
