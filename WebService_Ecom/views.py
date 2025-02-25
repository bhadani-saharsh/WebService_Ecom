from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "GET":
        print("query: ", request.GET.get('query'))
    return render(request, "WebService_Ecom/index.html")
