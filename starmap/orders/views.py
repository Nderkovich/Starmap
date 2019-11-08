from django.shortcuts import render, get_object_or_404
from map_generator.models import Starmap
from .forms import OrderPdfForm, OrderPicForm
from .models import OrderPic, OrderPdf


# Create your views here.
def order_pdf(request):
    if request.method == 'POST':
        print(request.session['starmap_id'])
        map = get_object_or_404(Starmap, id=request.session['starmap_id'])
        form = OrderPdfForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.map=map
            order.save()
    else:
        form = OrderPdfForm()
    return render(request,'orders/order/order_pdf.html', {'form': form})

def order_pic(request):
    if request.method == 'POST':
        map = get_object_or_404(Starmap, id=request.session['starmap_id'])
        form = OrderPicForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.map=map
            order.save()
    else:
        form = OrderPicForm()
    return render(request, 'orders/order/order_pic.html', {'form': form})



