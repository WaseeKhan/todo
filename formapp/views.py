from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, "formapp/home.html")

def addform(request):
	myname = request.POST['name']
	mymob = request.POST['mob']
	mystd = request.POST['std']
	FormModel(name =myname).save()
	FormModel(mob = mymob).save()
	FormModel(std = mystd).save()
	return redirect(request.META['HTTP_REFERER'])