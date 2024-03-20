from django.shortcuts import render

# Create your views here.
from app.models import *

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


from django.views.generic import CreateView, UpdateView, DeleteView, FormView

class Template(TemplateView):
    template_name = 'first.html'


class Lists(ListView):
    model = stud
    template_name = 'first.html'
    context_object_name = 'studs'



class Details(DetailView):
    model = stud
    template_name = 'first.html'
    context_object_name = 'student'


from django.urls import reverse_lazy
from .models import *
from .forms import StudentForm

class StudentCreateView(CreateView):
    template_name = 'stud_form.html'
    model = stud
    fields = '__all__'
    success_url = reverse_lazy('Lists')

class StudentUpdateView(UpdateView):
    template_name = 'update_form.html'
    model = stud
    fields = ['name', 'age']
    success_url = reverse_lazy('Lists')

class StudentFormView(FormView):
    template_name = 'form_view.html'
    form_class = StudentForm
    success_url = reverse_lazy('Lists')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)