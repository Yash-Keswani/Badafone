from django.shortcuts import render
from django.contrib.auth.backends import BaseBackend
from django.db import connection

class MyBackend(BaseBackend):
	def authenticate(self, request, username=None, password=None):
		with connection.cursor() as cursor:
			cursor.execute()
			if X :=
	
# Create your views here.
