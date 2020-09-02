#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse


#DataFlair
def index(request):
    shelf = Book.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})


def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        '''f = DataRangeForm(request.POST)
        if f.is_valid():
            c = f.save(commit = False)
            c.end_date = timezone.now()
            c.save()
        else:
            f = DataRangeForm()
            args = {}
            args.update(csrf(request))
            args['form'] = f

        return render(request, 'upload_form.html', {'form': f})'''


        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse('''Your Form is Wrong, Reload on <a href = "{{ url : 'index'}}">reload</a>''')
	#else:
    return render(request, 'book/upload_form.html', {'upload_form':upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form':book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')