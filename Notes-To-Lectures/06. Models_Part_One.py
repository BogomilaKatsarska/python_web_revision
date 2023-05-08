'''
ORM = Object Relational Mapping
Django raw SQL log - insert in settings.py

auto_now - sets the field to now every time the object is saved
auto_now_add - sets the field to now when the object is first created

migrations - use to add changes made to the models into the DB

pip install psycopg2

python manage.py createsuperuser

To reverse a concrete migration, pass the app name and the number of the previous migration
python manage.py migrate web 002

Model Field Options:
- unique = True (adds unique constraint)
- default = -1
- null = False(by default). If True, empty values will be stored as NULL
- blank = False(by default). If True, the field is allowed to be blank

DJANGO ADMIN takes the written model for visualization, not the applied migrations

is_full_time = models.BooleanField(
    null = True,
) ---> applies a checkbox


choices - use a sequence consisting of iterables of exactly two items to create choices.
        A new migration is automatically created each time the list of choices changes.


Relationships in Django Models:

1.Many-to-One Relationship:
Requires two positional arguments:
- the class to which the model is related
- required on_delete option

class Department(models.Model):
...

class Employee(models.Model):
    ...
    department = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
    )

2.One-to-One Fields:
Most useful on the PK of an object when that object 'extends' another object in some way

class Address(models.Model):
    ...

class BusinessBuilding(models.Model):
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
    )


DELETE OPTIONS:
CASCADE:  ако изтрием депт, изтриваме вс емплоийс, които са били в него
RESTRICT: не можем да изтрием dept, ако в него има хора
SET_NULL: ако изтрием dept, set-ваме на null департмента на хората, които са били там(follow rules below:
department = models.ForeignKey(
    Department,
    on_delete = models.SET_NULL,
    null = True,
)
'''
# TODO: check enum
