from django.shortcuts import render

def home(request):
	return render(request, 'pages/home.html')


def about(request):
	return render(request, 'pages/about.html')

def help(request):
	return render(request, 'pages/help.html')

def contact(request):
	return render(request, 'pages/contact.html')

def how_it_works_page(request):
	return render(request, 'pages/how_it_works_page.html')
