from django.views import View
from django.shortcuts import render, redirect
from . import my_functions 
from . import my_objects

def titleName(name: str):
            fixName = name.title()
            return fixName

class HomePageView(View):
    def get(self, request):
        myName='ALEX GRIMIT'
        
        newName = titleName(myName)

        names=["AleX","AbBy","kate","ERIC"]

        newNames = my_functions.title_names(names)

        car1 = my_objects.Car(color='blue',sound='honk',make='Nissan',model='Pathfinder',year='2022')
        car2 = my_objects.Car(color='grey',sound='BEEEP',make='Toyota',model='Prius',year='2023')
        motorcycle1 = my_objects.Motorcycle(color='red',sound='honk honk',make='Honda',model='Activa',year='2024')

        the_context={'hi':'Hello World!',
                     'origName':myName,
                     'name':newName,
                     'origNames':names,
                     'names_list':newNames,
                     'car1':car1,
                     'car2':car2,
                     'motorcycle1':motorcycle1}
        return render(request,'my_app/index.html',the_context)