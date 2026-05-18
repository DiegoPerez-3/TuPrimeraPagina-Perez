from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente. Ya puedes iniciar sesión.")
            return redirect("login")
        else:
            messages.error(request, "Hubo un error en el registro. Por favor revisá los datos.")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"

    def form_valid(self, form):
        messages.success(self.request, f"¡Bienvenido, {form.get_user().username}!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Usuario o contraseña incorrectos. Por favor intentá de nuevo.")
        return super().form_invalid(form)

@login_required
def profile_view(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)
    return render(request, "accounts/profile.html", {"user": request.user})

@login_required
def profile_edit_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Tu perfil ha sido actualizado exitosamente.")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    return render(request, "accounts/profile_edit.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })
