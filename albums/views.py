from django.shortcuts import render

def main(request):
    like = 0
    like = like + 1
    context = {
        "land_type":"about",
        "name": "arsen",
        "id": 6,
    }
    return render(request, "index.html", context)
    
def about(request):
    context = {
        "id": 6,
    }
    return render(request, "about.html", context)
    