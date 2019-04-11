Project Title
--------------------------------------------------------------------------------------
WebApplication -Inventory Management
---------------------------------------------------------------------------------------
Inventory Management is webapplication created using Flask framework to manage inventory 
of a list of products in respective warehouses. In this project there are 6 tabs in 
register tab user can register and then after registration he is able to login after 
login he can add/edit/view the product similarly he can add/edit/view location also he 
can make product_movement and can view the balance products (shows all trsaction ).
----------------------------------------------------------------------------------------
Steps to run setup the project
---------------------------------------------------------------------------------------
Download the zip file from given link
Extract the zip file
////////////////MAKE SURE PYTHON AND PIP are already installed on ypur desktop////////////

activate the virtual enviorment by using following command

(1)For WINDOWS:
      venv\Script\activate

    For linux:
       source venv\Script\activate


(2) pip install -r requirement.txt   (this file is already in folder)
///////////////It will install all required modules///////////////////

(3) In your command prompt run following command for IMPORTING DATABASE
First create database in Mysql using following command
        create database inventory_management;
	use inventory_management;
	source /home/assc/Downloads/app/app-master/sql_file.sql   ////this file is already in that folder
/////////////////It will create all required tables with data////////////////////

(4) Run the following command in active vertual environment
     python app.py

(5) First You can Register in register page and then u can login
    You can add product,edit product,add location ,edit location,add product movement ,edit product movement
	you can see product balance in Product_balance tab 


------------------------------------------------------------------------------------
Built with
-----------------------------------------------------------------------------------------
Pycharm
MySQL
 

--------------------------------------------------------------------------------------
Auathor
--------------------------------------------------------------------------------------------
Priyanka Shahane

