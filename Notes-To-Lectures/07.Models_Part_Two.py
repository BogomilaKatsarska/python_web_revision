'''
1:18
django migrations runpython - to check for diff types of migrations


def show_all_departments(request):
    #objects = manager
    all_departments = Department.objects.all()
    context = {
        'departments': all_departments,
    }
return render(request, 'departments.html', context)

QuerySet(lazy structure) - used for structuring our SQL requests.
Не се изпълнява на момента (за това понякога го лист-ваме)
=> върху него можем да правим още заявки(ex: filter, order_by...)

employees_aged_35 = Employee.objects.filter(age=35)
employees_not_aged_35 = Employee.objects.exclude(age=35)
employees_with_id_one = Employee.objects.get(id=1) --> not lazy method
=> 'get' returns an object, not a QuerySet
print(Employee.objects.get(level=Employee.LEVEL_SENIOR))
=> Get returns a single object and throws when none or multiple results
employees2 = Employee.objects.filter(department__name = 'Engineering')

employee = Employee.object.first()
employee.delete() - immediately deletes obj

Class Meta: to insert model metadata in the model, use the inner-class Meta

class Employee(models.Model):
    year_of_employment = models.IntegerField()

    class Meta:
        ordering = ['-year_of_employment']

class AuditInfoMixin(models.Model):
    class Meta:
        abstract = True

class City(models.Model):
    class Meta:
        verbose_name_plural = 'cities'


SLUGS:
#TODO: check SEO = Search Engine Optimization

slugs = models.SlugField(
    unique=True,
    )

STEP 1: mark as NULL=TRUE,
STEP 2: make migrations + migrate
STEP 3: python manage.py makemigrations web --empty

'''