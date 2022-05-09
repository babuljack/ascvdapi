from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import requests
# Create your views here.

def Home(request):
    return render(request,'index.html')


def Calculate(request):
    age=int(request.GET.get('age'));
    Totalcholesterol=int(request.GET.get('Totalcholesterol'));
    Diabetes=int(request.GET.get('Diabetes'));
    hdl=int(request.GET.get('HDL'));
    Gender=request.GET.get('Gender');
    smoker=int(request.GET.get('smoker'));
    Systolic=int(request.GET.get('Systolic'));
    Race=request.GET.get('Race');
    hypertensive=int(request.GET.get('hypertensive'));

    Url = f'https://ascvd.herokuapp.com/calc?age={age}&Totalcholesterol={Totalcholesterol}&hypertensive={hypertensive}&HDL={hdl}&Gender={Gender}&smoker={smoker}&Systolic={Systolic}&Race={Race}&Diabetes={Diabetes}'

    data=requests.get( Url )
    return HttpResponse(data)