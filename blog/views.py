from django.shortcuts import render, get_object_or_404
from .models import Entry

# All blogentries
def list_view(request):
    all_entries = Entry.objects.all().order_by('date')[0:100]
    return render(request, 'frontend/blog.html', {"all_entries" :  all_entries})

def detail_view(request, id):
    entry = get_object_or_404(Entry, id=id)
    return render(request, 'frontend/blogpost.html', {"entry" :  entry})