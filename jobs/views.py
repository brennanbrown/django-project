from django.shortcuts import render, get_object_or_404
from django.db import OperationalError

from .models import Job

# Create your views here.
def home(request):
    try:
        jobs = Job.objects.all()
        return render(request, 'jobs/home.html', {'jobs': jobs})
    except OperationalError:
        # Handle case where database tables don't exist
        return render(request, 'jobs/home.html', {'jobs': []})

def detail(request, job_id):
    try:
        job_detail = get_object_or_404(Job, pk=job_id)
        return render(request, 'jobs/detail.html', {'job':job_detail})
    except OperationalError:
        # Handle case where database tables don't exist
        return render(request, 'jobs/detail.html', {'job': None})
