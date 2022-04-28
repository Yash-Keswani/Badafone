import json
from _csv import reader

import MySQLdb
import pandas
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound, HttpRequest, HttpResponse
from django.shortcuts import render, redirect
import pandas as pd
from django.db import connection

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_POST, require_GET

def display_table(request, table_name: str):
	with connection.cursor() as cursor:
		cursor.execute("SHOW TABLES")
		table_names = [x[0] for x in cursor.fetchall() if not x[0].startswith("auth") and not x[0].startswith("django")]
		cursor.execute("SHOW FULL TABLES WHERE TABLE_TYPE LIKE 'VIEW'")
		view_names = [x[0] for x in cursor.fetchall()]
		
		if table_name.lower() not in table_names and table_name.lower() not in view_names:
			return HttpResponseNotFound('<h1>Table name not found in schema</h1>')
		
		cursor.execute(f"SELECT * FROM {table_name}")
		dump = cursor.fetchall()
		headers = [i[0] for i in cursor.description]
	tosend = {"data": pd.DataFrame(dump, columns=headers).to_string()}
	return render(request, "badaonline/display_table.html", tosend)

"""
def all_plans(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM plan")
		dump = cursor.fetchall()
		headers = [i[0] for i in cursor.description]
	tosend = {"data": pd.DataFrame(dump, columns=headers).to_html(classes='tbl', justify="center", index=False)}
	return render(request, "badaonline/all_plans.html", tosend)
"""

def wildcard(request, page: str):
	if page in ["admin", "edit_plan", "empployee", "main_page", "resolved", "sales", "submit_query", "user",
	            "user_edit_plan", "user_stats", "unresolved", "login"]:
		return render(request, f"badaonline/{page}.html")
	else:
		return HttpResponseNotFound("Invalid Page Entered")

@require_GET
def login_page(request):
	return render(request, f"badaonline/login.html",
	              {"submit_url": reverse('authenticate')})

@require_GET
def sales(request):
	return render(request, "badaonline/sales.html")

@require_GET
def admin(request):
	return render(request, "badaonline/admin.html")

@require_GET
def customer(request):
	return render(request, "badaonline/user.html")

@require_GET
def employee(request):
	return render(request, "badaonline/employee.html")

@require_POST
def update_plan(request):
	with connection.cursor() as cursor:
		cursor.execute("")

@require_GET
def user_stats(request):
	"""
	if request.user.is_authenticated:
				 user = request.user.id
	"""
	user_id = 1597
	return render(request, "badaonline/user_stats.html", {
		'data': pandas.read_sql_query(
			"SELECT * FROM customer NATURAL JOIN usage_calling "
			"WHERE customer_ID = " + str(user_id), connection)
		            .transpose().to_html(classes='tbl', header=False)
	})

@require_GET
def unresolved(request):
	"""
	if request.user.is_authenticated:
         user = request.user.id
	"""
	user_id = 589090
	data = pandas.read_sql_query("SELECT * FROM support_ticket WHERE employee_ID = " + str(user_id), connection)
	return render(request, "badaonline/unresolved.html", {
		'data': data.to_html(classes='tbl'),
		'ID': data["ticket_ID"][0]
	})

@require_POST
def login(request: HttpRequest):
	redirect_pages = {"customer": reverse('customer_home'), "employee": reverse('employee_home'),
	                  "administrator": reverse('admin_home'), "sales": reverse('sales_home')}
	data = json.loads(request.body)
	username, password = data.get("username"), data.get("password")
	user: User = authenticate(request, username=username, password=password)
	if user is not None:
		return redirect(redirect_pages[user.groups.first().name.lower()])
	else:
		return HttpResponse(content="Invalid Username or Password", status=401)

def import_users(request: HttpRequest):
	with open('templates/users.tsv', 'r') as csv_file:
		csvf = reader(csv_file)
		data = []
		for username, password, *__ in csvf:
			user = User(username=username)
			user.set_password(password)
			data.append(user)
		User.objects.bulk_create(data)

def submit_query(request: HttpRequest):
	data_in = json.loads(request.body)
	try:
		with connection.cursor() as cursor:
			cursor.execute(f"UPDATE support_ticket SET ticket_response = '{data_in['response']:s}', closed=1 WHERE ticket_ID = {data_in['ID']:d};")
	except MySQLdb.Error | MySQLdb.Warning:
		return HttpResponse(content="Query Error", status=500)
	return HttpResponse(content=json.dumps({'response': data_in}))