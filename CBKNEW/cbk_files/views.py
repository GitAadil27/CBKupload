from django.http import HttpResponse
from django.shortcuts import render
from .forms import FileUploadForm, BanqueMisrUploadForm
from .external_validation import compare_6_7, compare_1A_C2, compare_1A_1B, compare_1B_1B1, compare_4B_7, compare_5A_5B_5C, compare_4A_5A, compare_4B_5B
from .misr_validation import misr_fixes
import os

# City Monthly File Upload
def upload_file(request):
    bm_form = BanqueMisrUploadForm()  # Initialize Banque Misr form
    if request.method == 'POST' and 'upload_file' in request.POST:
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            files = [
                request.FILES['file1A'], request.FILES['file1B'], request.FILES['file1B1'],
                request.FILES['fileC2'], request.FILES['file4A'], request.FILES['file4B'],
                request.FILES['file5A'], request.FILES['file5B'], request.FILES['file5C'],
                request.FILES['file6'], request.FILES['file7']
            ]
            output_total1 = process_part1(files)
            return render(request, 'upload.html', {'output': output_total1, 'form': form, 'bm_form': bm_form})
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form, 'bm_form': bm_form})

# Process City Monthly files
def process_part1(files):
    output1 = compare_1A_1B(files[0], files[1])
    files[0].seek(0); files[1].seek(0)
    output2 = compare_1B_1B1(files[1], files[2])
    files[1].seek(0); files[2].seek(0)
    output3 = compare_1A_C2(files[0], files[3])
    files[0].seek(0); files[3].seek(0)
    output4 = compare_4B_7(files[5], files[10])
    files[5].seek(0); files[10].seek(0)
    output5 = compare_4A_5A(files[4], files[6])
    files[4].seek(0); files[6].seek(0)
    output6 = compare_4B_5B(files[5], files[7])
    files[5].seek(0); files[7].seek(0)
    output7 = compare_6_7(files[9], files[10])
    files[9].seek(0); files[10].seek(0)
    return [output1, output2, output3, output4, output5, output6, output7]

# Banque Misr File Upload
def banque_misr_upload(request):
    if request.method == 'POST' and 'banque_misr_upload' in request.POST:
        bm_form = BanqueMisrUploadForm(request.POST, request.FILES)
        if bm_form.is_valid():
            file = request.FILES['fileBM']
            # Process the file with misr_fixes function
            processed_file = misr_fixes(file)
            original_filename = os.path.splitext(file.name)[0]
            # Generate response for download
            response = HttpResponse(processed_file, content_type='text/plain')
            response['Content-Disposition'] = f'attachment; filename="{original_filename}"'
            return response
    else:
        bm_form = BanqueMisrUploadForm()
    return render(request, 'upload.html', {'bm_form': bm_form, 'form': FileUploadForm()})
