# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request) :
    menu_data = Menu.objects.all().order_by('name')
    context = {'menu': menu_data}
    return render (request,'menu.html',context)


def display_menu_items(request,pk=None):
    menu_item = ""
    imgSrc = ""
    if pk :
        menu_item = Menu.objects.get(pk = pk)
        imgSrc =  "img/menu_items/"+f"{menu_item.name}"+".jpg"
        print(imgSrc)
    return render (request,'menu_item.html',context={"menu_item":menu_item,'imgSrc':imgSrc})