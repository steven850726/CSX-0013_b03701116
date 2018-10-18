from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from guestbook.models import Vocabulary


def index(request):
	#v1 = Vocabulary.objects.create(vocab='한국', meaning='韓國')
	#v2 = Vocabulary.objects.create(vocab='공책', meaning='筆記本')

	questions = Vocabulary.objects.all()
	#questions = ['韓國','筆記本','三']
	return render(request, 'guestbookver1.html', locals())


def create(request):

		#if request.method == 'POST':
		#	form = Vocabulary(request.POST)
		#	if form.is_valid():
		#		form.save()
		#		return redirect(create.get_absolute_url())
				return render(request,'create.html',locals())
		#else:
		#	form = Vocabulary()
		#	return render(request, 'create.html', {'form': form})
