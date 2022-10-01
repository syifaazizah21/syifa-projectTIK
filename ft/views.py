from django.shortcuts import render

# Create your views here.
def prodift(request):
    judul = ["Teknik Elektro", "Teknik Industri", "Teknik Kimia", "Teknik Mesin", "Teknik Metalurgi", "Teknik Sipil"]

    konteks = {
        'title': judul,
    }
    return render(request, 'ft.html', konteks)
