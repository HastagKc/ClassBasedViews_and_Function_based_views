from .forms import StudentForm  # Make sure to import your form class
from django.shortcuts import render
from django.http import HttpResponse

from .forms import StudentForm

from django.views import View

# Create your views here.

# function based views


def myview(request):
    return HttpResponse('<h1>This response from function based view </h1>')

# class based view


class MyView(View):
    name = 'kshittiz'

    def get(self, request):
        # return HttpResponse('<h1>This response from class based view </h1>')
        return HttpResponse(f'My name is {self.name} from class based view ')

# how to pass contex in both function view and class based views

# first create with function based views


def homeview(request):
    context = {'view_data': 'funciton view'}
    return render(request, 'main/index.html', context=context)

# second context with class based view


class HomeClassView(View):
    context = {'view_data': 'class based view'}

    def get(self, request):
        return render(request, 'main/index.html', context=self.context)


# form in both function view and class based view
# function based view


def formview(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Use cleaned data from the form
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            message = form.cleaned_data['message']

            # Process the form data
            print(f"Name: {name}, Age: {age}, Message: {message}")

            # Redirect or render a success template
            return HttpResponse("Form submitted successfully!")

    else:
        form = StudentForm()

    return render(request, 'main/form.html', {'form': form})
