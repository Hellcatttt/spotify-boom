from django.shortcuts import render
from django.http import JsonResponse
from playlist.models import Playlist
from playlist.models import Playlist, Track

def main(request):
    context = {
    }
    return render(request, "main.html", context)
    
def about(request):
    context = {
        "id": 6,
    }
    return render(request, "playlist.html", context)

def sign_in(request):
    context = {
        "id": 6,
    }
    return render(request, "sign_in.html", context)


def register_user(request):
    name = request.GET.get("mail")
    Playlist.objects.create(name=name)
    data = {
    }
    return JsonResponse(data)

def upload_track_page(request):
    context = {
    }
    return render(request, "create_track.html", context)

def upload_track(request):
    song_name = request.POST.get("song_name")
    print(song_name)
    artist = request.POST.get("artist")
    
    
    track = Track.objects.create(
        name=song_name,
        artist=artist,        )
    if request.FILES.get('file'):
        track.file = request.FILES.get('file')
        track.save()
    data = {
        "ok":"VSE POLUCHILOSЬ"
    }
    return JsonResponse(data)

def getplaylist(request):
    tracks = Track.objects.all()
    data_music = []
    for i in range(0, len(tracks)):
        track = tracks[i]
        data_music.append([
            track.artist, 
            track.name, 
            track.file.url
             ])
    data = {
        "data_music":data_music,
    }
    return JsonResponse(data)
