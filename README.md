
### Web Django Covid-19 Information
This work is small panel system  in table format  that shows  COVID-19 infection of countries, with the following fields:


| Field | Format | 
| :---: | :---: | 
| country | String | 
| confirmed | Integer |  
| deaths | Integer | 
| recovered | Integer | 

#### Main actions  :

1- The application  authenticate the admin user, and only the admin can register or edit new data. The lookup table is public.

2 - The system have an admin user.

3- The system  have a template that  store COVID-19 data and a template that stores the countries names.

4 - The system  have a simple CRUD for COVID-19 data.

5 - The data register  have a combo box that loads the country model data.

6 - Only the administrator user can register data in the COVID-19 table.


#### Operating instruction :
##### From the terminal:
```
$ cd web-django-Lorrayne/countrys_covid/ 
```


```
$ python manage.py runserver

```
After executed enter the link: http://127.0.0.1:8000/ in your browser.

Click on the button "Adminstrator " for manage the table.
```
Username : Lorrayne
Password : mercedesf1
```



