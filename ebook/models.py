from django.db import models
from django.shortcuts import reverse

# Create your models here.
STATUS=(
	(0,'Draft'),
	(1,'Publish')
	)

class Book(models.Model):
	title = models.CharField(max_length=500,unique=True)
	slug = models.SlugField(max_length=500,unique=True)
	content = models.TextField()
	upload_book = models.FileField(upload_to='ebook/books')
	cover = models.ImageField(upload_to ='ebook/covers',default=True)
	status = models.IntegerField(choices=STATUS,default=0)
	uploaded_on = models.DateTimeField(auto_now_add=True) 
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering =['-uploaded_on']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('book-detail',kwargs={'slug':self.slug})

