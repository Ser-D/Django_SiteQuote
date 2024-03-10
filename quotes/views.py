from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .utils import get_mongodb
from .forms import TagForm


def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quote_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quote_on_page})


def upload(request):
    return render(request, 'quotes/upload.html', context={})


def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', context={'form': TagForm()})
