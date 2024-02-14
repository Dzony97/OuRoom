from django.shortcuts import render

def main_room(request):
    return render(request, 'rooms/mainroom.html')

def ouroom(request):
    return render(request, 'rooms/ouroom.html')

def games(request):
    return render(request, 'rooms/games.html')

def profile(request):
    return render(request, 'rooms/profile.html')
