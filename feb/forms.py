from django.forms import ModelForm
from feb.models import Dosen
from feb.models import Staff
from feb.models import Mahasiswa
from django import forms

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = '_all_'

        widgets = {
            'NIP' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'Tanggal_Lahir' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Alamat_Rumah' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
        }

class FormStaff(ModelForm):
    class Meta:
        model = Staff
        fields = '_all_'

        widgets = {
            'Nama' : forms.NumberInput({'class':'form-control'}),
            'NIP' : forms.TextInput({'class':'form-control'}),
            'Tanggal_Lahir' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Unit' : forms.TextInput({'class':'form-control'}),
            'Alamat_Rumah' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
        }

class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '_all_'

        widgets = {
            'NIM' : forms.NumberInput({'class':'form-control'}),
            'Nama' : forms.TextInput({'class':'form-control'}),
            'Tanggal_Lahir' : forms.TextInput({'class':'form-control'}),
            'Email' : forms.TextInput({'class':'form-control'}),
            'Fakultas' : forms.TextInput({'class':'form-control'}),
            'Prodi' : forms.TextInput({'class':'form-control'}),
            'Foto' : forms.TextInput({'class':'form-control'}),
        }