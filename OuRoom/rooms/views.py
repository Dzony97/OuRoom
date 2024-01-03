from django.shortcuts import render

def main_room(request):

    return render(request, 'rooms/mainroom.html')
