import csv,sys,os

project_dir = "C:/Users/Admin/Desktop/sample/enginesearch1/enginesearch/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from shop.models import Category

data = csv.reader(open("C:/Users/Admin/Desktop/sample/enginesearch1/data.csv"),delimiter=",")



for row in data:
	if row[0] != 'number':
		product = Category()
		product.id = row[0]
		product.number = row[0]
		product.name = row[1]
		product.slug = row[2]
		product.created_at = row[3]
		product.updated_at = row[4]
		product.rating = row[5]
		product.url = row[6]
		product.save()
		


		



