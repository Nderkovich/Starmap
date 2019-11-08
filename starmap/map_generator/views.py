from django.shortcuts import render, redirect
from .models import Starmap
from .forms import StarmapForm
from django.shortcuts import get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
def start_page(request):
    if request.method == 'POST':
        form = StarmapForm(request.POST)
        if form.is_valid():
            starmap = form.save()
            request.session['starmap_id'] = starmap.id
            if starmap.map_type == 1:
                return redirect('orders:order_pdf')
            elif starmap.map_type == 2:
                return redirect('orders:order_pic')
    else:
        form = StarmapForm()
    return render(request, 'star/main.html', {'form': form})

def pdf(request, order_id):
    order = get_object_or_404(Starmap, id=order_id)
    return render(request, 'star/pdf.html', {'order': order})