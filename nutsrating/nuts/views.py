from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser, OrehusChange
from .forms import OrehusForms, UserLoginForm, UserRegisterForm, UserSettingsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, login
from django.contrib import messages


def leader_board(request):
    title = 'Доска рейтинга'
    return render(request, 'leaderboard.html', {"title": title})


@login_required
def add_rating(request):
    title = 'Добавить рейтинг'
    if request.method == 'POST':
        user_form = OrehusForms(request.POST)
        if user_form.is_valid():
            user = CustomUser.objects.get(unchanged_name=user_form.cleaned_data['orehus_user'])
            rating_was = user.rating
            user.rating = user.rating + user_form.cleaned_data['operation']
            user.save()  # Сохранение изменений в базе данных
            rating_new = user.rating
            comment = user_form.cleaned_data['comment']
            orehus_user = user_form.cleaned_data['orehus_user']
            operation = user_form.cleaned_data['operation']
            OrehusChange.objects.create(comment=comment, operation=operation, orehus_user=orehus_user,
                                        who_changed=request.user.username, rating_was=rating_was, rating_new=rating_new)
            return redirect('leadboard')
    else:
        user_form = OrehusForms()
    return render(request, 'addrating.html', {"title": title, "user_form": user_form})


def rating_history(request):
    title = 'История рейтинга'
    return render(request, 'ratinghistory.html', {"title": title})


def user_profile(request, profile_id):
    get_user_history = OrehusChange.objects.filter(orehus_user=profile_id)
    orehus_user = CustomUser.objects.get(pk=profile_id)
    print(get_user_history)
    return render(request, 'user_profile.html', {"orehus_user": orehus_user, "get_user_history": get_user_history})


def user_settings(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserSettingsForm(request.POST)
            if form.is_valid():
                user_pk = request.user.pk
                print(user_pk)
                get_current_user = CustomUser.objects.get(pk=user_pk)
                CustomUser.objects.filter(pk=user_pk).update(first_name=form.cleaned_data['first_name'])
                CustomUser.objects.filter(pk=user_pk).update(user_vk_url=form.cleaned_data['user_vk_url'])
                CustomUser.objects.filter(pk=user_pk).update(user_zodiac=form.cleaned_data['user_zodiac'])
                CustomUser.objects.filter(pk=user_pk).update(birth_date=form.cleaned_data['birth_date'])
                print(get_current_user)
                return render(request, 'personality.html', {"form": form})
        else:
            form = UserSettingsForm()
            user_pk = request.user.pk
            print(user_pk)
        return render(request, 'personality.html', {"form": form})
    else:
        redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    title = 'ВходВОрешник'
    if request.user.is_authenticated:
        return redirect('ratinghistory')
    else:
        if request.method == 'POST':
            form = UserLoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('ratinghistory')
        else:
            form = UserLoginForm()
        return render(request, 'login.html', {"form": form, "title": title})


def user_register(request):
    if request.user.is_authenticated:
        return redirect('ratinghistory')
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Success registration')
                return redirect('login')
            else:
                messages.error(request, 'Registration errors')
        else:
            form = UserRegisterForm()
        return render(request, 'register.html', {"form": form})


def handling_404(request, exception):
    return render(request, '404.html',{"title": "Not Found"}, status=404)