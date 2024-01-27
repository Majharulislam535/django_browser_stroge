from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    response = render(request,'home.html')
    response.set_cookie('name','majharul')
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response=render(request,'delete.html')
    response.delete_cookie('name')
    return response


# session storage 

def set_session(request):
    data={
        'name':'majharul',
        'age':25,
        'language':'Bangla'
    }

    request.session.update(data)
    return render(request,'home.html')

# def get_session(request):
#     name=request.session.get('name','Guest')
#     age=request.session.get('age')
#     language=request.session.get('language')
#     return render(request,'get_session.html',{'name':name,'age':age,'language':language})

# session expired

def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name','Guest')
        age=request.session.get('age')
        #request.session.modified=True
        language=request.session.get('language')
        return render(request,'get_session.html',{'name':name,'age':age,'language':language})
    else:
        return HttpResponse('Your session has been expired>>>>>')



def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render(request,'delete.html')
