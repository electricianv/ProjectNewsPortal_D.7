from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from .forms import NewsForm, ArticleForm


def news_list(request):
    # Get all news articles (filter by category if needed)
    news = Post.objects.filter(categoryType=Post.NEWS)

    # Paginate news articles (10 per page)
    paginator = Paginator(news, 10)

    # Get the page number from the request (default to 1)
    page_number = request.GET.get('page', 1)

    # Get the specific page of news articles
    page_obj = paginator.get_page(page_number)

    # Context data to pass to the template
    context = {'page_obj': page_obj}

    return render(request, 'news_list.html', context)


# Create your views here.
class NewsCreateView(CreateView):
    model = Post
    form_class = NewsForm
    template_name = 'news/news_form.html'

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleCreateView(CreateView):
    model = Post
    form_class = ArticleForm
    template_name = 'articles/article_form.html'

    def form_valid(self, form):
        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    model = Post
    form_class = NewsForm
    template_name = 'news/news_update_form.html'

    def form_valid(self, form):
        return super().form_valid(form)


class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'news/news_confirm_delete.html'
    success_url = '/news/'  # Redirect after deletion


class ArticleUpdateView(UpdateView):
    model = Post
    form_class = ArticleForm
    template_name = 'articles/article_update_form.html'

    def form_valid(self, form):
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'articles/article_confirm_delete.html'
    success_url = '/articles/'  # Redirect after deletion
