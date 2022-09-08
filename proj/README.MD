Django Documentations Used on these projects

08) Models and Admin Panel

- python3 manage.py createsuperuser : 
    this allows you to create super user so you can log in from localhost:8000/admin

- python3 manage.py migrate :
    migrate executes those sql commands in the database file

What is Django Model?
    -Django model is a built in feature that django uses to create tables, their fields, and various constraints. Django Models is the sql of database one uses with django.

How to add models to your project application?
    - Go to admin.py and put following code
        from . models import "name of your models"
        admin.site.register("name of your model")

---------------------------------------------------------------------------------------------------

09) Database Relationships

- One to One : One table record can relate to one record in another table.
- One to many : One table record can relate to many records in another table.
- Many to many: This relationship occurs when multiple records in a table are associated with multiple records in another table. 

What is Django ForeignKey?
-ForeignKey is a django orm field to clumn mapping for creating and working with relationships between tables in relational database.

on_delete=models.CASCADE = This allows someone to delete aka CASCADE.

---------------------------------------------------------------------------------------------------

10) Database Queries
queryset = ModelName.objects.all() 
# queryset = variables that holds response
# ModelName = Model Name
# objects = Model objects attribute
# .all() = Method : other examples [.get(), .filter(), .exclude()]

---------------------------------------------------------------------------------------------------

11) Model Forms

Django has a {% csrf_token %} tag that is implemented to avoid malicious attacks. It generates a token on the server-side when rendering the page and makes sure to cross-check this token for any requests coming back in. If the incoming requests do not contain the token, they are not executed.

Model Form : It is a class which is used to create an HTML form by using the Model. It is an efficient way to create a form without writing HTML code. Django automatically does it for us to reduce the application development time.

how to use model form 
from django.forms import ModelForm
from .models import "name of your model"

--------------------------------------------------------------------------------------------------

13) Static Files

-python3 manage.py collectstatic

--------------------------------------------------------------------------------------------------
17) Signals

from django.dispatch import receiver

@receiver(post_save, sender=Profile)

def ready(self):
    import users.signals
#need to import this in admin.py

--------------------------------------------------------------------------------------------------
18) User Login, Logout and Flash messages
