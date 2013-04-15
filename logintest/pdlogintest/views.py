# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from pdlogintest.models import User

def index(request):
	userList = User.objects.all()
	context = {'userList' : userList}
	return render(request,'pdlogintest/index.html',context)

def userpage(request,user_name):
	user = get_object_or_404(User,username = user_name)
	return render(request, 'pdlogintest/userpage.html',{'userObj' : user})
