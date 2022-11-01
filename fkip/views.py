from django.shortcuts import render, redirect
from . models import Dosen, Mahasiswa, Staff
from fkip.forms import FormDosen, FormDosen, FormStaff, FormMahasiswa
from django.contrib import messages

def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()
    if request.method == "POST":
        dosen.hapus()
    
    return redirect('fkip')

def ubah_dosen(request, id_dosen):
    dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form':form,
            'dosen':dosen,
        }
    return render(request, template, konteks)

def ubah_staff(request, id_staff):
    staff = Staff.objects.get(id=id_staff)
    template = 'ubah-staff.html'
    if request.POST:
        form = FormStaff(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect('ubah_staff', id_staff=id_staff)
    else:
        form = FormStaff(instance=staff)
        konteks = {
            'form':form,
            'staff':staff,
        }
    return render(request, template, konteks)

def ubah_mahasiswa(request, id_mahasiswa):
    mahasiswa = Mahasiswa.objects.get(id=id_mahasiswa)
    template = 'ubah-mahasiswa.html'
    if request.POST:
        form = FormMahasiswa(request.POST, instance=mahasiswa)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbaharui!")
            return redirect(ubah_mahasiswa, id_mahasiswa=id_mahasiswa)
    else:
        form = FormMahasiswa(instance=mahasiswa)
        konteks = {
            'form':form,
            'mahasiswa':mahasiswa,
        }
    return render(request, template, konteks)

# Create your views here.
def prodifkip(request):
    judul = "S1 Pendidikan Matematika", "S1 Pendidikan Bahasa Inggris", "S1 Pendidikan Kimia", "S1 Pendidikan Non Formal"

    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()
    konteks = {
        'judul': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip.html', konteks)

def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-dosen.html', konteks)

def tambah_staff(request):
    if request.POST:
        form = FormStaff(request.POST)
        if form.is_valid():
            form.save()
            form = FormStaff()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-staff.html', konteks)
    else:
        form = FormStaff()

        konteks = {
            'form': form,
        }

    return render(request, 'tambah-staff.html', konteks)

def tambah_mahasiswa(request):
    if request.POST:
        form = FormMahasiswa(request.POST)
        if form.is_valid():
            form.save()
            form = FormMahasiswa()
            pesan = "Data berhasil disimpan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-mahasiswa.html', konteks)
    else:
        form = FormMahasiswa()

        konteks = {
            'form' : form,
        }

    return render(request, 'tambah-mahasiswa.html', konteks)