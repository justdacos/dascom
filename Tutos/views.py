from django.shortcuts import render

def home(request):
	return render(request, 'pages/home.html')


def about(request):
	return render(request, 'pages/about.html')

def help(request):
	return render(request, 'pages/help.html')
