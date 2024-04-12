from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Score

@login_required
def snake(request):

    scores = Score.objects.all().order_by('-point')

    return render(request, 'games/snake.html', {'scores': scores})




