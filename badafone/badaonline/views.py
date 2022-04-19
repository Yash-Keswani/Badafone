from django.http import HttpResponseNotFound
from django.shortcuts import render
import pandas as pd
from django.db import connection

# Create your views here.

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

def all_plans(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT * FROM plan")
		dump = cursor.fetchall()
		headers = [i[0] for i in cursor.description]
	tosend = {"data": pd.DataFrame(dump, columns=headers).to_html(classes='tbl', justify="center")}
	return render(request, "badaonline/all_plans.html", tosend)
