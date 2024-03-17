from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Quote, Author, Tag
# from .utils import get_mongodb
from .forms import TagForm, QuoteForm, AuthorForm


def main(request, page=1):
    # db = get_mongodb()
    # quotes = db.quotes.find()
    quotes = Quote.objects.all().order_by('created_at')

    per_page = 10
    paginator = Paginator(quotes, per_page)
    quote_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quote_on_page})


def author_info(request, author_id):
    a = get_object_or_404(Author, id=author_id)
    return render(request, 'quotes/author_info.html', context={'author': a, })


def tag_info(request, tag, page=1):
    tag_name = get_object_or_404(Tag, name=tag)
    quotes = Quote.objects.all().filter(tags=tag_name)
    print(tag, quotes)

    per_page = 10
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.page(page)
    print(quotes_on_page, tag)
    return render(request, 'quotes/tag_info.html', context={"quotes": quotes_on_page, "tag": tag, "page": 1})


@login_required
def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST, request.FILES, instance=Tag())
        if form.is_valid():
            form.save()
            messages.success(request, f"Tag '{form.cleaned_data['name']}' has been added!")
            return redirect(to="quotes:add_tag")
        return render(request, "quotes/add_tag.html", {"form": form})
    return render(request, "quotes/add_tag.html", {"form": TagForm()})


@login_required
def tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to="quotes:index")
        else:
            return render(request, 'quotes/tag.html', {'form': form})
    return render(request, 'quotes/tag.html', {'form': TagForm()})


@login_required
def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"Author '{form.cleaned_data['fullname']}' has been added!")
            return redirect(to='quotes:add_author')
        else:
            return render(request, 'quotes/add_author.html', context={"form": form})
    return render(request, "quotes/add_author.html", context={"form": AuthorForm()})


@login_required
def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=Quote())
        if form.is_valid():
            quote = form.save()
            selected_tags = Tag.objects.filter(name__in=request.POST.getlist("tags"))
            for tag in selected_tags.iterator():
                quote.tag.add(tag)
            quote.save()
            messages.success(request, f"Quote has been added!")
            return redirect(to='quotes:add_quote')
        else:
            return render(request, "quotes/add_quote.html", context={"form": form})
    return render(request, "quotes/add_quote.html", context={"form": QuoteForm()})
