from django.shortcuts import render
from .models import Cd
from .forms import CdCreate
from django.http import HttpResponse
import logging #levele logowania: info, warning, critical, trace, error

# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info('hello world')
    cds = Cd.objects.all()
    return render(request, 'music/shop.html', {'cds': cds})

def upload(request):
    upload = CdCreate()
    if request.method == 'POST':
        upload = CdCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return render(request, 'music/shop.html')
        else:
            return HttpResponse("""Twoj formularz nie jest poprawny <a href="{{url:'index'}}">reload</a>""")
    else:
        return render(request, 'music/upload_form.html', {'upload_form': upload})

def update_cd(request, cd_id):
    cd_id = int(cd_id)
    try:
        cd_selection = Cd.objects.get(id = cd_id)
    except Cd.DoesNotExist:
        return redirect('index')
    cd_form = CdCreate(request.POST or None, instance = cd_selection)
    if cd_form.is_valid():
        cd_form.save()
        return redirect('index')
    return render(request, 'music/upload_form.html', {'upload_form': cd_form})


def delete_cd(request, cd_id):
    cd_id = int(cd_id)
    try:
        cd_selection = Cd.objects.get(id = cd_id)
    except Cd.DoesNotExist:
        return redirect('index')
    cd_selection.delete()
    return render(request, 'music/shop.html')