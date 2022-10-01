from django.shortcuts import render

# Create your views here.
def prodifeb(request):
    judul = ["Manajemen", "Akuntansi", "Ilmu Ekonomi Pembangunan"]

    konteks = {
        'title': judul,
    }
    return render(request, 'feb.html', konteks)
