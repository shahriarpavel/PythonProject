from books.models import Book
from django.shortcuts import render, redirect

from .forms import BookForm


# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
            form = BookForm()
    return render(request,'form.html',{'form':form})


def update_book(request,b_id):
    book=Book.objects.get(pk=b_id)
    if request.method == 'POST':
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
    return render(request, 'form.html', {'form': form})

def delete_book(request,b_id):
    book = Book.objects.get(pk=b_id).delete()
    return redirect('/')