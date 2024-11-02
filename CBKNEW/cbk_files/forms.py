from django import forms

class FileUploadForm(forms.Form):
    file1A = forms.FileField(label='Select 1A')
    file1B = forms.FileField(label='Select 1B')
    file1B1 = forms.FileField(label='Select 1B1')
    fileC2 = forms.FileField(label='Select C2')
    file4A = forms.FileField(label='Select 4A')
    file4B = forms.FileField(label='Select 4B')
    file5A = forms.FileField(label='Select 5A')
    file5B = forms.FileField(label='Select 5B')
    file5C = forms.FileField(label='Select 5C')
    file6 = forms.FileField(label='Select 6')
    file7 = forms.FileField(label='Select 7')

class BanqueMisrUploadForm(forms.Form):
    fileBM = forms.FileField(label='Select Banque Misr File')
