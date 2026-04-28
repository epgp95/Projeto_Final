from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro

def lista_livros(request):
    livros = Livro.objects.all()

    search = request.GET.get("search")
    if search:
        livros = livros.filter(titulo__icontains=search) | livros.filter(autor__icontains=search)

    tipo = request.GET.get("tipo")
    if tipo:
        livros = livros.filter(tipo=tipo)

    ano = request.GET.get("ano")
    if ano:
        livros = livros.filter(ano=ano)

    utilizador = request.GET.get("utilizador")
    if utilizador:
        livros = livros.filter(proprietario__username__icontains=utilizador)

    min_preco = request.GET.get("min_preco")
    max_preco = request.GET.get("max_preco")
    if min_preco:
        livros = livros.filter(preco__gte=min_preco)
    if max_preco:
        livros = livros.filter(preco__lte=max_preco)

    status = request.GET.get("status")
    if status == "vendido":
        livros = livros.filter(vendido=True)
    elif status == "disponivel":
        livros = livros.filter(vendido=False)

    sort = request.GET.get("sort", "-created_at")
    if sort not in ["titulo", "-titulo", "autor", "-autor", "preco", "-preco",
                    "created_at", "-created_at", "stock", "-stock"]:
        sort = "-created_at"
    livros = livros.order_by(sort)

    return render(request, "livros/lista_livros.html", {"livros": livros})


def adicionar_livro(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        preco = request.POST.get("preco")
        stock = request.POST.get("stock") or 1
        tipo = request.POST.get("tipo")
        ano = request.POST.get("ano")
        if titulo and autor and preco:
            Livro.objects.create(titulo=titulo, autor=autor, preco=preco,
                                 stock=stock, tipo=tipo, ano=ano)
            return redirect("lista_livros")
    return render(request, "livros/livro_form.html")


def toggle_vendido(request, id):
    livro = get_object_or_404(Livro, id=id)
    livro.vendido = not livro.vendido
    livro.save()
    return redirect("lista_livros")


def livro_update(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        preco = request.POST.get("preco")
        stock = request.POST.get("stock") or 1
        tipo = request.POST.get("tipo")
        ano = request.POST.get("ano")
        if titulo and autor and preco:
            livro.titulo = titulo
            livro.autor = autor
            livro.preco = preco
            livro.stock = stock
            livro.tipo = tipo
            livro.ano = ano
            livro.save()
            return redirect("lista_livros")
    return render(request, "livros/livro_form.html", {"livro": livro})


def livro_delete(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == "POST":
        livro.delete()
        return redirect("lista_livros")
    return render(request, "livros/livro_delete.html", {"livro": livro})