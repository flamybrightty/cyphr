from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.urls import reverse
from PIL import Image
import io
from django.conf import settings
from stegano import lsb
from django.utils.http import urlencode

def stego(request):
    return render(request, "stego/stego.html")

def instruction(request):
    return render(request, "stego/instruction.html")

def hide(request):
    if request.method == 'POST':
        if 'image' in request.FILES and 'text' in request.POST:
            image_file = request.FILES['image']
            text = request.POST['text']
            image = Image.open(image_file)
            
            text_utf8 = text.encode('utf-8')
            text_utf8_str = text_utf8.decode('latin-1')
            
            secret_image = lsb.hide(image_file, text_utf8_str)
            
            image_io = io.BytesIO()
            secret_image.save(image_io, format='PNG')
            image_content = ContentFile(image_io.getvalue())
            
            image_name = f'secret_{image_file.name}'
            image_path = default_storage.save(f'images/{image_name}', image_content)
            
            result_url = reverse('stego:result') + '?' + urlencode({'image_path': image_path})
            
            return redirect(result_url)
        else:
            return render(request, "stego/hide.html", {'error': 'Необходимо загрузить изображение и ввести текст.'})
    
    return render(request, "stego/hide.html")

def extract(request):
    return render(request, "stego/extract.html")

def extract_result(request):
    if request.method == 'POST' and 'image' in request.FILES:
        image_file = request.FILES['image']
        
        hidden_text = lsb.reveal(image_file)
        
        hidden_text_utf8 = hidden_text.encode('latin-1').decode('utf-8')
        
        return render(request, "stego/extract_result.html", {'hidden_text': hidden_text_utf8})
    
    return redirect('stego:extract')

def result(request):
    image_path = request.GET.get('image_path')
    image_url = f'{settings.MEDIA_URL}{image_path}'
    return render(request, "stego/result.html", {'image_url': image_url})
