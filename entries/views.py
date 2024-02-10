from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
)

from .models import Entry


# inherit from ListView class 
class EntryListView(ListView):
    # specify which model should be used for retrieving the data to display in the view
    model = Entry
    # set entries in ascending order by date 
    queryset = Entry.objects.all().order_by("-date_created")

# inherit from DetailView class 
class EntryDetailView(DetailView):
    model = Entry