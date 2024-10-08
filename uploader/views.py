from django.shortcuts import render
from .models import UploadedImage
from .forms import UploadImageForm

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            images = UploadedImage.objects.all()
            return render(request, 'upload_image.html', {'form': form, 'images': images})
    else:
        form = UploadImageForm()
        images = UploadedImage.objects.all()
    return render(request, 'upload_image.html', {'form': form, 'images': images})

# Create your views here.
