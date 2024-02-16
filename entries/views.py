from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,

    CreateView,
    UpdateView,
    DeleteView,
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

# ---------------------------------------------
# CRUD operations 
    
# class EntryCreateView(CreateView):
#     model = Entry
#     # define which model fields should be displayed in the form
#     fields = ["title", "content"]
#     # reverse_lazy() is basically a method to retrieve the url by its name 
#     success_url = reverse_lazy("entry-list")

# class EntryUpdateView(UpdateView):
#     model = Entry
#     fields = ["title", "content"]

#     # get_success_url - just a general practice when you need to dynamically access to additional context 
#     # get_success_url() simply returns the value of success_url
#     def get_success_url(self):
#         return reverse_lazy(
#             "entry-detail",
#             {"pk": self.entry.id}
#         )

# class EntryDeleteView(DeleteView):
#     model = Entry
#     success_url = reverse_lazy("entry-list")    