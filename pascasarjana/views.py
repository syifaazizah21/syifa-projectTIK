from django.shortcuts import render

# Create your views here.
def prodipasca(request):
    judul = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Teknik Kimia"]

    konteks = {
        'title': judul,
    }
    return render(request, 'pascasarjana.html', konteks)
