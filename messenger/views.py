from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Message
from .forms import MessageForm

class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "messenger/inbox.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "messenger/message_detail.html"
    context_object_name = "mensaje"

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.is_read:
            obj.is_read = True
            obj.save()
        return obj

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = "messenger/message_form.html"
    success_url = reverse_lazy("inbox")

    def form_valid(self, form):
        form.instance.sender = self.request.user
        messages.success(self.request, "Mensaje enviado correctamente.")
        return super().form_valid(form)
