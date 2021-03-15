from django.shortcuts import render, get_object_or_404,redirect
from .models import Book
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Q 


# Create your views here.
class HomeView(TemplateView):
    template_name = "ebook/home.html"

class BookList(ListView):
	queryset = Book.objects.filter(status=1).order_by('-uploaded_on')
	context_objects_name = 'book_list'
	template_name = 'ebook/book_list.html'
	#paginate_by = 6
	
	def get_queryset(self):
		query = self.request.GET.get('q','')
		book_list = Book.objects.filter(
			Q(title__icontains=query) | Q(content__icontains=query) | Q(slug__icontains=query) 
				)
		
		if book_list:
			return book_list
		else:
			messages.info(self.request,f'Your search -{query} did not match any documents.')
			return book_list
	
def book_detail(request, slug):
    template_name = 'ebook/book_detail.html'
    book = get_object_or_404(Book, slug=slug)
    context={'book':book}
    return render(request,template_name,context)



import os
from django.conf import settings
from django.http import HttpResponse, Http404


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/uploadfile")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404





