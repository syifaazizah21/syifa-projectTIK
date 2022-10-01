from django.shortcuts import render

# Create your views here.
def prodifh(request):
    judul = ["Ilmu Hukum"]

    konteks = {
        'title': judul,
    }
    return render(request, 'fh.html', konteks)
