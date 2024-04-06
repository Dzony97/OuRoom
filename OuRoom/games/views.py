from django.shortcuts import render

def snake(request):
    return render(request, 'games/snake.html')
