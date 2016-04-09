from django.shortcuts import render

def post_list(request): #request to zapytanie http
    return render(request, 'blog/post_list.html', {}) #tu w słowniku mogą być
    #rozne zmienne 
