from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from apps.shopping_cart.models import Order
from apps.accounts.models import Profile
from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.accounts.models import User



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


@login_required
def user_update(request, id, slug):
    if request.user.id == id:
        user = User.objects.get(id=id)
        form = CustomUserChangeForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect("success")
        return render(request, 'accounts/update.html', {'form':form})
    else:
        return render(request, 'accounts/forbidden.html')


@login_required
def user_detail(request, id, slug):
    if request.user.id == id:
        user = get_object_or_404(User, id=id)
        context = {'user':user}
        return render(request, 'accounts/user_detail.html', context)
    else:
        return render(request, 'accounts/forbidden.html')



@login_required
def user_delete(request, id, slug):
    user = get_object_or_404(user = request.user)
    user.delete()
    return redirect("success")


@login_required
def my_profile(request, **kwargs):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    context = {
        'my_orders': my_orders
    }

    return render(request, "accounts/profile.html", context)




