# Django
from django.http import HttpResponse

# Utils
from datetime import datetime
import json

def hello_world(request):
    """Return a greeting!"""
    now = datetime.now()
    return HttpResponse(f'Oh, hi! Current server time is {now}')

def order_numbers(request):
    """order numbers!"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')] 
    sorted_numbers = sorted(numbers)
    data = {
        'status':'ok',
        'numbers':sorted_numbers,
        'message':'Integers sorted successfully!',
    }
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

def say_hi(request,name,age):
    """says hi"""
    if age < 12:
        message = 'Sorry, you are not allowed to be here!'
    else:
        message = 'Welcome to Platzigram'
    return HttpResponse(message)