# README #

###How to run the project###

1. Clone the project in you local repository
2. Go to enginesearch1 folder
3. Type in command line => python manage.py runserver

### How to modify csv file###

* dat.csv refers to category
* Product.csv refers to product
* Each product is linked with category through number id 
* So, if you want to set product of category 3, you set 3 in number_id in product.csv
* Note that to upload image in product.csv we give link to the image folder and image name


###How to upload to database through csv file ###
* Note: Just run these commands, after you have deleted previous products and categories from django admin so that there won't be any duplication
* Go inside enginesearch1 folder
* Type in command line => python importCategory.py
* Type again => python importProduct.py
* Then you can run project by typing => python manage.py runserver

### How to delete previous products and categories ###
* After you have run the project go to: localhots:8000/admin url
* Inside Categories, select all categories, choose delete from drop down menu and hit Go.
* Inside Product, select all products, choose delete from drop down menu and hit Go."# selcouth-searchengine-prototype" 
"# selcouth-searchengine-prototype" 
