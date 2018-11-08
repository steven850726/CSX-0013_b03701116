from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from guestbook.models import Vocabulary


def index(request):
	#v1 = Vocabulary.objects.create(vocab='한국', meaning='韓國')
	#v2 = Vocabulary.objects.create(vocab='공책', meaning='筆記本')

	questions = Vocabulary.objects.all()
	#questions = ['韓國','筆記本','三']
	return render(request, 'guestbookver1.html', locals())


def create(request):

	vocabularies = Vocabulary.objects.all()
	#context = {'Vocabulary': vocabulary}
	
	class NewVocab(forms.ModelForm):
		class Meta:
			model = Vocabulary
			fields = '__all__'

	if request.method == 'POST':
		form = NewVocab(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/create/')
	#		return render(request,'create.html',locals())
	else:
		form = NewVocab()
		return render(request, 'create.html', locals())


def login(request):

	if request.user.is_authenticated: 
		return redirect('/')

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		message = '登入成功！'
		return redirect('/')
	else:
		message = '尚未登入成功！'
		return render(request, 'login.html', locals())

#	if user is not None:
#		if user.is_active:
#			auth.login(request,user)
#			return redirect('/')
#			message = '登入成功!'
#		else:
#			message = '帳號尚未啟用!'
#	else:
#		message = '登入失敗!'
#	return render(request,"login.html",locals())

def logout(request):

	auth.logout(request)
	return redirect('/')


def register(request):

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
#			_login(request,username,password)
			return redirect('/login/')
	else:
		form = UserCreationForm()
		message = '尚未註冊成功！'
	return render(request, 'register.html',locals())

def delete(request, id):
	vocabularies = Vocabulary.objects.get(id=id)
	vocabularies.delete()
	return redirect('/create/',locals())

def edit(request, id):
	vocabularies = Vocabulary.objects.get(id=id)
	return render(request, 'edit.html', locals())

def update(request, id):
	vocabularies = Vocabulary.objects.get(id=id)
	vocabularies.vocab = request.POST['vocab']
	vocabularies.meaning = request.POST['meaning']
	vocabularies.save()
	return redirect('/create/')


