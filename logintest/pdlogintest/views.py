# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from pdlogintest.models import User

def index(request):
	userList = User.objects.all()
	context = {'userList' : userList}
	return render(request,'pdlogintest/index.html',context)

def submitprofile(request):
	_username = request.POST['usernameinput'].lower()
	try:
		allWithName = User.objects.get(username=_username)
		print "already exists! " + _username
		return render(request,'pdlogintest/index.html', {'error_message' : "username taken!"})
	except User.DoesNotExist:
		user = User(username=_username,birthday=request.POST['birthdayinput'],description=request.POST['descriptioninput'])
		user.save()
		return  HttpResponseRedirect(reverse('userpage',args=(_username,)))

def userpage(request,user_name):
	user = get_object_or_404(User,username=user_name)
	return render(request, 'pdlogintest/userpage.html', {'userObj' : user, 'allusers' : User.objects.all()})
