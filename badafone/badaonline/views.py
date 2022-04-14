from django.http import HttpResponseNotFound
from django.shortcuts import render
import pandas as pd
from django.db import connection

# Create your views here.

def display_table(request, table_name: str):
	with connection.cursor() as cursor:
		cursor.execute("SHOW TABLES")
		table_names = [x[0] for x in cursor.fetchall() if not x[0].startswith("auth") and not x[0].startswith("django")]
		
		if table_name.lower() not in table_names:
			return HttpResponseNotFound('<h1>Table name not found in schema')
		
		cursor.execute(f"SELECT * FROM {table_name}")
		dump = cursor.fetchall()
		headers = [i[0] for i in cursor.description]
	tosend = {"data": pd.DataFrame(dump, columns=headers).to_string()}
	return render(request, "badaonline/display_table.html", tosend)
