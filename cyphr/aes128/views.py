from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from Crypto.Cipher import AES
import base64
import os

KEY = os.urandom(16)

def aes128(request):
    return render(request, 'aes128/aes128.html')

def instruction(request):
    return render(request, "aes128/instruction.html")

def cypher(request):
    if request.method == 'POST':
        text = request.POST['text']
        cipher = AES.new(KEY, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))

        encrypted_text = base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')
        return render(request, 'aes128/cypher_result.html', {'encrypted_text': encrypted_text})

    return render(request, 'aes128/cypher.html')

def cypher_result(request):
    return render(request, 'aes128/cypher_result.html')

def decypher(request):
    if request.method == 'POST':
        encrypted_text = request.POST['text']
        try:
            encrypted_data = base64.b64decode(encrypted_text)
            nonce = encrypted_data[:16]
            tag = encrypted_data[16:32]
            ciphertext = encrypted_data[32:]

            cipher = AES.new(KEY, AES.MODE_EAX, nonce=nonce)
            decrypted_text = cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')

            return render(request, 'aes128/decypher_result.html', {'decrypted_text': decrypted_text})
        except (ValueError, KeyError) as e:
            return HttpResponse(f'Error decrypting: {str(e)}')

    return render(request, 'aes128/decypher.html')

def decypher_result(request):
    return render(request, 'aes128/decypher_result.html')
