from django.shortcuts import render
from .models import Students
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.



@csrf_exempt
def AllStudents(request):
    if (request.method == 'POST'):
        body_unicode = request.body.decode('utf-8')
        print(json.loads(body_unicode))
        # body = json.loads(body_unicode)
        # content = body['content']
        return JsonResponse({"bro":json.loads(body_unicode)})
    data=Students.objects.values()
    data=list(data)
    print(data[0]["age"])
    return JsonResponse({"mk":data})


