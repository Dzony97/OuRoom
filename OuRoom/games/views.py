import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Score

@login_required
def snake(request):

    scores = Score.objects.all().order_by('-point')

    return render(request, 'games/snake.html', {'scores': scores})

@require_POST
def submit_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        score = data.get('score')
        user = request.user if request.user.is_authenticated else None
        if user:
            player_username = user.username
            new_score = Score(player=user, point=score, player_username=player_username)
            new_score.save()
            return JsonResponse({'status': 'success', 'message': 'Wynik został zapisany.'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Użytkownik nie jest zalogowany.'}, status=400)

