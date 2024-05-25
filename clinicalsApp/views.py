from django.shortcuts import render

from clinicalsApp.forms import ClinicalDataForm
from clinicalsApp.models import Patient, ClinicalData
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect

# Create your views here.
class PatientsListView(ListView):
    model=Patient


class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('home')
    fields = ('lastName','firstName', 'age', 'gender')


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('home')
    fields = ('lastName','firstName', 'age', 'gender')


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('home')


def addClinicalData(request,**kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'clinicalsApp/clinicaldataform.html', {'form': form, 'patient':patient})


def analyseClinicalData(request, **kwargs):
    data = ClinicalData.objects.filter(patient_id = kwargs['pk'])
    responsedate = []
    for eachEntry in data:
        if eachEntry.vitalsName == 'hw':
            heightandweight= eachEntry.vitalsValue.split('/')
            if len(heightandweight) > 1:
                feetToMeters = float(heightandweight[0]) * 0.4536
                weight = float(heightandweight[1])
                BMI = (weight)/(feetToMeters * feetToMeters)
                bmiEntry = ClinicalData()
                bmiEntry.vitalsName = 'BMI'
                bmiEntry.vitalsValue = BMI
                responsedate.append(bmiEntry)
        responsedate.append(eachEntry)

    return render(request, 'clinicalsApp/generateReport.html', {'data': responsedate})



