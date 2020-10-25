from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import *

# Create your views here.

def index(request):
	if request.method == "POST":
		form = NameForm(request.POST)
		if form.is_valid():
			subject= form.cleaned_data.get("subject")
			message= form.cleaned_data.get("message")
			sender= form.cleaned_data.get("sender")
			cc_myself= form.cleaned_data.get("cc_myself")
			print(subject,message,sender,cc_myself)
			return HttpResponseRedirect("thanks/")
	else:
		form = NameForm()
	return render(request, "index.html",{"form":form})

def thanks(request):
	return HttpResponse("<h1>Forms is Valid</h1>")