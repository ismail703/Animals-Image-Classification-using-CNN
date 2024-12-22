from django.shortcuts import render
from .forms import ImageForm
from .predict import *



def index(request):
    return render(request, 'index.html')

def marine(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            img_obj = form.instance
            predicted_class = predict_marine(img_obj.image.path)

            return render(request, 'marine.html', {'form': form, 'img_obj': img_obj, 'prediction': predicted_class})
    else:
        form = ImageForm()    
        return render(request, 'marine.html', {'form': form})


def replite(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            img_obj = form.instance
            predicted_class = predict_replite(img_obj.image.path)

            return render(request, 'replite.html', {'form': form, 'img_obj': img_obj, 'prediction': predicted_class})
    else:
        form = ImageForm()    
        return render(request, 'replite.html', {'form': form})
    
def bird(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            img_obj = form.instance
            predicted_class = predict_bird(img_obj.image.path)

            return render(request, 'birds.html', {'form': form, 'img_obj': img_obj, 'prediction': predicted_class})
    else:
        form = ImageForm()    
        return render(request, 'birds.html', {'form': form})

def wild(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            img_obj = form.instance
            predicted_class = predict_wild(img_obj.image.path)

            return render(request, 'wild.html', {'form': form, 'img_obj': img_obj, 'prediction': predicted_class})
    else:
        form = ImageForm()    
        return render(request, 'wild.html', {'form': form})
    
def unknown(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            img_obj = form.instance
            predicted_class = predict_category(img_obj.image.path)

            return render(request, 'unknown.html', {'form': form, 'img_obj': img_obj, 'prediction': predicted_class})
    else:
        form = ImageForm()    
        return render(request, 'unknown.html', {'form': form})
