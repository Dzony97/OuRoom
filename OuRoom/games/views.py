from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def snake(request):
    return render(request, 'games/snake.html')

