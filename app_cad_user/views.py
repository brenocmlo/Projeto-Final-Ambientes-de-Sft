from django.shortcuts import render

def inicial(request):
        return render(request, 'usuarios/inicial.html')
    def usuario(request):
        novo_user = Usuario()
        novo_user.nome = request.POST.get('nome')
        novo_user.idade = request.POST.get('idade')
        novo_user.save()
        usuarios = {
            'usuarios': Usuario.objects.all()
        }
        return render(request, 'usuarios/listagem.html', usuarios)