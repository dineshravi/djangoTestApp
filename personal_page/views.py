from django.shortcuts import render
from django.http import HttpResponse
from personal_page import forms
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from personal_page import models
from django.shortcuts import redirect

# Create your views here.
def index (request):
	print "in index method"
	if request.COOKIES.get('admin') == 'dinesh':
		status = "Super User"
	else:
		status = "Open user"


	form = forms.SignInForm()
	post_list = models.Post.objects.all()
	return render (request,'personal_page/index.html',{'form': form, 'post_list':post_list,'status':status})


#Admin authentication block
@csrf_protect
def login (request):
	print "in login method"
	if request.method == 'POST':
		form = forms.SignInForm(request.POST)
		
		if form.is_valid():
		
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			if email == "dineshra@buffalo.edu":
				if password == "good123":

					response = redirect('personal_page.views.index')

					response.set_cookie('admin','dinesh')

					return response
	else:
		form = forms.SignInForm()

		return render (request, 'personal_page/index.html',{'form': form})

#Method to render a create page 
def create(request):
	print "in create method"
	name = request.COOKIES.get('admin')
	
	if name == 'dinesh':

		form_post = forms.CreatePost()	
		return render(request,'personal_page/create.html',{'form': form_post})
	else:
		return redirect ('personal_page.views.index')	

#Method which creates model instances based on Create Post Form input
@csrf_protect
def submit(request):
	print "in submit method"
	name = request.COOKIES.get('admin')
	
	if name == 'dinesh':

		form = forms.CreatePost(request.POST)

		if form.is_valid():

			title = form.cleaned_data['title']
			content = form.cleaned_data['content']

			models.Post.objects.create(title = title, content = content)

			return redirect ('personal_page.views.index')
				
			
		else:

			form = forms.CreatePost()
			return render (request,'personal_page/create.html',{'form':form})
	else:

		return redirect ('personal_page.views.index')


#Method which edits the existing posts
def edit(request, id=""):

	print "in edit method"
	name = request.COOKIES.get('admin')
	
	if name == 'dinesh':

		post = models.Post.objects.get(pk=id)
		form = forms.EditPost({'content':post.content, 'title':post.title})
		return render(request, 'personal_page/edit.html',{'post':post, 'form':form})
	else:
		return redirect ('personal_page.views.index')


#method to update the post
@csrf_protect
def update(request, id=""):
	post = models.Post.objects.get(pk=id)
	form = forms.EditPost(request.POST)

	if form.is_valid():

		title = form.cleaned_data['title']
		content = form.cleaned_data['content']

		post.title = title
		post.content = content

		post.save(update_fields=['title','content'])

		return redirect ('personal_page.views.index')
	
	else:

		return redirect ('personal_page.views.edit')


#method to delete post
def delete(request, id=""):

	print "in delete method"
	name = request.COOKIES.get('admin')
	
	if name == 'dinesh':
		print "cookie set"
		post = models.Post.objects.get(pk=id)
		post.delete()

		return redirect ('personal_page.views.index')
	else:
		print "cookie not set"
		return redirect ('personal_page.views.index')


#method to logout admin
def logout(request):
	print "in logout method"
	response = redirect ('personal_page.views.index')
	
	response.delete_cookie('admin')

	return response
