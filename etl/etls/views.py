from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

from .forms import DBForm
from .models import Conection
from etls.etl import start
# Create your views here.
def home(request):  
    if request.method == 'GET':
        dbs=Conection.objects.all()
        return render(request, 'home.html',{'dbs': dbs})
        print("get")
    else:
        
        print("enter")
        # conection=Conection(name="x",database=1,user='postgres',
        #                     password='database123',host='localhost',databaseName='test',
        #                     port=5432)
        conection=Conection.objects.get(name="x")
        conection.save()
        print(conection)
        file=request.FILES['formFile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        
        
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        start(conection,uploaded_file_url)
        
        return render(request, 'home.html')
def create_db(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DBForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DBForm()

    return render(request, 'dbConection.html', {'form': form})
    