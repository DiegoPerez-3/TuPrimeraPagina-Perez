from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import Q
from .models import Page
from .forms import PageForm

def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

class PageListView(ListView):
    model = Page
    template_name = "pages/page_list.html"
    context_object_name = "pages"

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(titulo__icontains=q) |
                Q(subtitulo__icontains=q) |
                Q(categoria__icontains=q)
            ).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q", "")
        context["has_pages"] = Page.objects.exists()
        return context

class PageDetailView(DetailView):
    model = Page
    template_name = "pages/page_detail.html"

class PageCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "pages/page_form.html"
    success_message = "Página creada exitosamente."

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "pages/page_form.html"
    success_message = "Página actualizada exitosamente."
    
    def test_func(self):
        page = self.get_object()
        return self.request.user == page.autor or self.request.user.is_superuser

class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("page_list")
    
    def test_func(self):
        page = self.get_object()
        return self.request.user == page.autor or self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, "Página borrada exitosamente.")
        return super().form_valid(form)
