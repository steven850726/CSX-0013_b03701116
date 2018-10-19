from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django import forms
from guestbook.models import Vocabulary


def index(request):
	#v1 = Vocabulary.objects.create(vocab='한국', meaning='韓國')
	#v2 = Vocabulary.objects.create(vocab='공책', meaning='筆記本')

	questions = Vocabulary.objects.all()
	#questions = ['韓國','筆記本','三']
	return render(request, 'guestbookver1.html', locals())


def create(request):

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
