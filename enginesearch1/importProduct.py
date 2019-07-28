import csv,sys,os

project_dir = "C:/Users/Admin/Desktop/sample/enginesearch1/enginesearch/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from shop.models import Product


data2= csv.reader(open("C:/Users/Admin/Desktop/sample/enginesearch1/Product1.csv"),delimiter=",");


for row in data2:
	if row[0] != 'number_id':
		product = Product()
		product.number_id= row[0]
		product.name = row[1]
		product.slug = row[2]
		product.description = row[3]
		product.price = row[4]
		product.available = row[5]
		product.stock = row[6]
		product.created_at = row[7]
		product.updated_at = row[8]
		product.image = row[9]
		product.save()
		


		

		

		



