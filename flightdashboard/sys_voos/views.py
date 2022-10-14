from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'sys_voos/index.html')

#esboco dos urls apenas para renderizar as paginas requeridas

def crud(request):
    return render(request, 'sys_voos/crud.html')

def gera_relatorio(request):
    return render(request, 'sys_voos/gera_relatorio.html')

def atualiza_status(request):
    return render(request, 'sys_voos/atualiza_status.html')


