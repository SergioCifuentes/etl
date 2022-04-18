from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .models import Conection
from etls.etl import start
# Create your views here.
def home(request):  
    if request.method == 'GET':
        return render(request, 'home.html')
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
    