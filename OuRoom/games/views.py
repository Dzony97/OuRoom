from django.shortcuts import render

def snake(request):
    return render(request, 'games/snake.html')

def paper_games(request):
    return render(request, 'games/paper.html')