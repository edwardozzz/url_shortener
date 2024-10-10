from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import ShortenedURL
from .forms import URLForm
import string, random

def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            short_url = generate_short_url()
            new_url = form.save(commit=False)
            new_url.short_url = short_url
            new_url.save()
            return redirect('link_list')
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form})

def link_list(request):
    links = ShortenedURL.objects.all()
    return render(request, 'shortener/link_list.html', {'links': links})

def redirect_to_original(request, short_url):
    url = get_object_or_404(ShortenedURL, short_url=short_url)
    return HttpResponseRedirect(url.original_url)
