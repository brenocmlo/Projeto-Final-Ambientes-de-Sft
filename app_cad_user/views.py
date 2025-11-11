from django.shortcuts import render, redirect
from .models import Usuario  

def inicial(request):
    return render(request, 'usuarios/inicial.html')

def usuario(request):
    if request.method == 'POST':
        novo_user = Usuario()
        novo_user.nome = request.POST.get('nome')
        novo_user.idade = request.POST.get('idade')
        novo_user.save()
        return redirect('listagem_user')  

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/listagem.html', usuarios)