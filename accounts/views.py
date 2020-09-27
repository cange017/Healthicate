from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
# from .models import Room

#def fullcalendar(request):
#    return render(request, '../templates/fullcalendar.html')

def index(request):
    return render(request, '../templates/index.html')

def register(request):
    return render(request, '../templates/register.html')
    
class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request, '../templates/doctor.html')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return render(self.request, '../templates/doctor.html')


def login_request(request):
    if request.user.is_authenticated:
        return render(request, '../templates/doctor.html')
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return render(request, '../templates/doctor.html')
            else:
                form = AuthenticationForm(request.POST)
                messages.error(request,"Invalid username or password")
                return render(request, '../templates/login.html', {'form': form})
        else:
            messages.error(request,"Invalid username or password")
            form=AuthenticationForm()
            return render(request, '../templates/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, '../templates/index.html')

# def all_rooms(request):
#     rooms = Room.objects.all()
#     return render(request, 'chat/index.html', {'rooms': rooms})


# def room_detail(request, slug):
#     room = Room.objects.get(slug=slug)
#     return render(request, 'chat/room_detail.html', {'room': room})
