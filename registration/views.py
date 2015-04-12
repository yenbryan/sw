from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from registration.forms import AccountForm, ProfileUserCreationForm
from registration.models import Profile


def view_profiles(request):
    profile_list = Profile.objects.all()
    paginator = Paginator(profile_list, 10)
    page = request.GET.get('page')
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        profiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        profiles = paginator.page(paginator.num_pages)
    return render(request,'profile/profiles.html', {
        'profiles': profiles
    })

    # contact_list = Contacts.objects.all()
    # paginator = Paginator(contact_list, 25) # Show 25 contacts per page
    #
    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     contacts = paginator.page(paginator.num_pages)
    #
    # return render_to_response('list.html', {"contacts": contacts})






def view_profile(request, username):
    profile = get_object_or_404(Profile, username=username)
    followings = profile.follows.all()
    exist = True
    if request.user.is_authenticated==False:
        exist = request.user.follows.filter(username=username).exists()
    # profile_image =
    # profile = Profile.objects.get(username=username)
    return render(request, 'profile/dashboard.html', {'profile': profile,
                                                      'exist': exist,
                                                      'followings': followings})


def register(request):
    if request.method == 'POST':
        form = ProfileUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.send_email("welcome {}".format(user.username), "Thank you for signing up")
            return redirect("login")
    else:
        form = ProfileUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def follow(request,follow):
    if request.method == 'GET':
        try:
            profile = Profile.objects.get(username=follow)
            request.user.follows.add(profile)
            return render(request, 'profile/dashboard.html', {'profile': profile})
        except Profile.DoesNotExist:
            pass

    profiles = Profile.objects.all()
    return render(request,'profile/profiles.html', {
        'profiles': profiles
    })
# def account(request):
#     account_form = AccountForm()
#     return render(request,'registration/account.html', {
#         'account_form': account_form
#     })

@login_required
def my_profile(request):
    followings = request.user.follows.all()
    if request.method == 'POST':
        account_form = AccountForm(request.POST)
        if account_form.is_valid():
            account_form.save(request)
    else:
        account_form = AccountForm({'first_name': request.user.first_name,
                                    'last_name': request.user.last_name,
                                    'email': request.user.email,
                                    'username': request.user.username})
    return render(request,'registration/account.html', {
        'account_form': account_form,
        'followings': followings
    })


def splash_index(request):
    profiles = Profile.objects.all()
    return render(request, 'splash_index.html', {'profiles': profiles})

#
# def social_new_user(request):
#     return render(request, 'splash_index.html', {'profiles': profiles})
#     pass