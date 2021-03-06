from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Performance, Movie

def home(request):
    #dictionary to be passed into the tepmlate render object.
    Performance_array = Performance.objects.all()
    Movie_array = Movie.objects.all()
    Performance_dictionary = {'performance': Performance_array[0].date}
    random_dictionary = {'testing': Movie_array[0].name}
    #gets template from Template folder
    template = get_template('home.html')
    #fills in template tags with corresponing text from dicitonary
    html = template.render(Context(random_dictionary))
    return HttpResponse(html)

def merch(request):
    return render(request, 'merch.html')

def tickets(request):
    Movie_array = Movie.objects.all()
    Performance_array = Performance.objects.all()
    pass_in_dictionary = {'Movie': Movie_array, 'Performance': Performance_array}
    template = get_template('tickets.html')
    html = template.render(Context(pass_in_dictionary))
    return HttpResponse(html)
    #return render(request, 'tickets.html')

def upcoming_performances(request):
    Performance_array = Performance.objects.all()
    Performance_dictionary = {'Performance': Performance_array}
    template = get_template('upcoming_performances.html')
    html = template.render(Context(Performance_dictionary))
    return HttpResponse(html)

def home_nontest_v(request):
    return render(request, 'home_nontest_v.html')
	
def location(request):
	return render(request, 'location.html')

def Performance_1(request):
    return Performance_helper(1)

def Performance_2(request):
    return Performance_helper(2)

def Performance_3(request):
    return Performance_helper(3)

def Performance_4(request):
    return Performance_helper(4)

def Performance_helper(id_num):
    Performer = Performance.objects.get(id=id_num)
    template = get_template('Performance.html')
    html = template.render(Context({'p' : Performer}))
    return HttpResponse(html)



#how to add entry to database:
    #1. from CMD "python manage.py shell"
    #2. from polls.models import Performance, Movie (or whatever table you want to work on)
    #3. new_addition = Performance(name="balh", date="12/12/1212", etc for all the fields)
    #4. new_addition.save() grats you added an entry to the database

#how to remove entry from the database:
    #1. from CMD "python manage.py shell"
    #2. from polls.models import Performance, Movie (or whatever table you want to work on)
    #3. new_array = Performance.objects.all()
    #4. new_array (this will list out all the elements in the array, find the one you want to delete)
    #5. new_array[3].delete() (this assumes you want to delete the fourth entry in the Performance)

#how to add table to the database:
    #1. Open polls\models.py
    #2. Create a new model (each model acts as a table)
    #3. from CMD "python manage.py makemigrations"
    #3. from CMD "python manage.py check"
    #4. STOP if you have any errors
    #5. "python manage.py migrate"
#---------------- -------------------------------------------------------------------------------------------
#python manage.py flush  
#deletes database, re-populates as well

#python manage.py dumpdata polls
#dumps data from the application

#python manage.py dumpdata polls > polls_data.json 
#to dump into this specific file name, or else if polls_data.json is not specified, it will just dump into the promt 

#python manage.py dumpdata --indent 2 
#shows all data in the current databases; the indent is to keep things neat and readable

#python manage.py loaddata 
#reloads everything in polls_data.json
