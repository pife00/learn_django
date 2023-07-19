from django.shortcuts import render, get_object_or_404,redirect
from .models import Item
from django.contrib.auth.decorators import login_required

from .forms import newItemForm

def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        category=item.category, is_Sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/details.html', {
        'item': item,
        'related_items' :related_items
    })

@login_required
def new(request):
    if request.method == "POST":
        form = newItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:details',pk = item.id)
    else:
        form = newItemForm()
    return render(request, 'item/form.html',{
        'form':form
    })
    
    
    
