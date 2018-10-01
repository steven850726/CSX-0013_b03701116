from django.shortcuts import render,redirect   # 加入 redirect 套件
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
	questions = ['韓國','筆記本','三']
	return render(request, 'guestbookver1.html', locals())
