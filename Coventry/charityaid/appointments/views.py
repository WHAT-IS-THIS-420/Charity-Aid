from django.shortcuts import HttpResponse, render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipiant, Appointment
from .froms import RecipiantForm, AppointmentForm

@login_required
def view_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments/view_appointments.html', {'appointments': appointments})

@login_required
def schedule_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('view_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/schedule_appointment.html', {'form': form})

@login_required
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated!')
            return redirect('view_appointments')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'appointments/edit_appointment.html', {'form': form})


#Create your views here.
def index(request):
    return HttpResponse('it works')
#render  recipiant list
def recipiants_list(request):
    recipiants = Recipiant.objects.all()
    return render(request, 'appointments/recipiant_list.html',{'recipiants':recipiants})

#get one recipiant detials
def recipiants_detail(request, id):
    recipiant = get_object_or_404(Recipiant,id=id)
    return render(request,'appointments/recipiant_detail.html',{'recipiant':recipiant})

#edit recipiant details
def recipiants_edit(request, id):
    recipiant = get_object_or_404(Recipiant,id=id)
    if request.method == 'POST':
        form = RecipiantForm(request='POST',instance=recipiant)
        if form.is_valid():
            form.save()
            return redirect('recipiant_detail',id=recipiant.id)
    else:
        form = RecipiantForm(instance=recipiant)
    return render(request, 'appointments/recipiant_edit.html', {'form':form})
        
#delete a recipiant
def recipiants_delete(request, id):
    recipiant = get_object_or_404(Recipiant, id=id)
    if request.method == 'POST':
        recipiant.delete()
        return redirect('recipiant_list')
    return render(request, 'appointments/recipiant_confirm_delete.html',{'recpiant':recipiant})

