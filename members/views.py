# from django.shortcuts import render
from .models import Member
from django.template import loader
from django.http import HttpResponse

# def members(request):
    # return HttpResponse("Hello world!")
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('allmembers.html')
    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
#  for testing purpose
def testing(request):
  mymembers = Member.objects.all()
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
    "firstname":'linux',
    'k':mymembers,
    'greeting':0,
    'x': ['Apple', 'Banana', 'Cherry'], 
    'y': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))
