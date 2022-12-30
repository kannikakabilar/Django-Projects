import email
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x = request.POST['name'] # Takes the first name 'POSTED' by the the user and assigns it to x
  y = request.POST['soi']
  z = request.POST['email']
  member = Members(fullname=x, soi=y, email=z)
  member.save()
  return HttpResponseRedirect(reverse('index')) # go back to index.html page
  
def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
  
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecord(request, id):
  first = request.POST['name']
  soi = request.POST['soi']
  eml = request.POST['email']
  mem_id = int(request.POST['id'])
  member = Members.objects.get(id=id)
  if mem_id != member.id:
    return HttpResponseRedirect(reverse('index'))
  member.fullname = first
  member.soi = soi
  member.email = eml
  member.save()
  return HttpResponseRedirect(reverse('index'))
