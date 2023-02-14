from typing import Generic
from django.shortcuts import render
from django.shortcuts import redirect,render,get_object_or_404
from django.template.loader import render_to_string
from artistapp.models import Detail,WorkDoneImages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from artistapp.forms import CreateUserForm
from artist import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _



def home(request):
    all_cards = Detail.objects.all()
    return render(request,"template/main-page.html",{'all_cards': all_cards})

def signin(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    # else:
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user.id  # Store user ID in session
            return redirect("/")
        else:
            messages.error(request, 'ERROR! login Invalid')
    context = {}
    return render(request,"template/signin.html", context)


def createsignin(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get('password1')
            password2 = request.POST.get("password2")    

            if form.is_valid():
                username = form.cleaned_data.get("username")
                email = form.cleaned_data.get('email')
                password1 = form.cleaned_data.get('password1')
                password2 = form.cleaned_data.get('password2')
                if User.objects.filter(username=username).exists():
                    messages.error('name', 'This name is already taken.')
                if User.objects.filter(email=email).exists():
                    messages.error('email', 'This email is already registered.')
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created '+ user)
                form.save()
                messages.success(request, "success, check your email to confirm")
                subject = "Your Artistmake Login Information"
                message = render_to_string('template/email_template.txt', {'username': username, 'password': password1})
                from_email = settings.EMAIL_HOST_USER
                to_list = [email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                return HttpResponseRedirect('signin')   
        else: 
            form = CreateUserForm()
        return render(request,"template/createsignin.html",{'form':form})

def signout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    logout(request)
    return redirect('home')

@login_required
def createcard(request):
    try:
        request.user.card.get()
        return redirect('my_card')
    except Detail.DoesNotExist:
        pass
    if request.method == 'POST':
        name = request.POST.get('name')
        town = request.POST.get('town')
        perfect_in = request.POST.get('perfect_in')
        years_of_experience = request.POST.get('years_of_experience')
        availability = request.POST.get('availability')
        pricing = request.POST.get('pricing')
        trained_at = request.POST.get('trained_at')
        image = request.FILES.get('image')
        additional_text = request.POST.get('additional_text')
        

        user = request.user
        detail = Detail.objects.create(    
            user=user,
            name=name,
            town=town,
            perfect_in=perfect_in,
            years_of_experience=years_of_experience,
            availability=availability,
            pricing=pricing,
            trained_at=trained_at,
            image=image,
            additional_text=additional_text)
        workpic = request.FILES.getlist('workdone')
        for wimage in workpic:
            WorkDoneImages.objects.create(detail=detail, workimage = wimage)
        return redirect('card_detail',detail_id=detail.id)
    return render(request,'template/cardcreate.html')



@login_required
def my_card(request):
    try:
        card = request.user.card.get()
    except Detail.DoesNotExist:
        return redirect('createcard')
    context = {
        'card': card,
    }
    return render(request, 'template/mycard.html', context)



def detail_view(request, detail_id):
    detail = get_object_or_404(Detail, pk=detail_id)
    images = WorkDoneImages.objects.filter(detail=detail)
    user = request.user
    is_following = False
    is_like = False
    if user.is_authenticated:
        if user in detail.followers.all():
            is_following = True
        if user in detail.likes.all():
            is_like = True
    context = {
        'detail': detail,
        'images': images,
        'is_following': is_following,
        'is_like': is_like,
        'request_user': request.user
    }
    return render(request, 'template/card_detail.html', context)



def like_dislike_detail(request, detail_id):
    detail = get_object_or_404(Detail, pk=detail_id)
    user = request.user
    if user in detail.likes.all():
        detail.likes.remove(user)
    else:
        detail.likes.add(user)
    return redirect('detail_view', detail_id=detail.id)



def follow_unfollow_detail(request, detail_id):
    detail = get_object_or_404(Detail, pk=detail_id)
    user = request.user
    if user in detail.followers.all():
        detail.followers.remove(user)
    else:
        detail.followers.add(user)
    return redirect('detail_view', detail_id=detail.id)







# def detail_view(request, detail_id):
#     detail = get_object_or_404(Detail, pk=detail_id)
#     user = request.user
#     is_following = False
#     if user.is_authenticated:
#         if user in detail.followers.all():
#             is_following = True
#     context = {'detail': detail, 'is_following': is_following}
#     return render(request, 'card_detail.html', context)


# def card_detail(request,detail_id):
#     detail = Detail.objects.get(id=detail_id)
#     images = WorkDoneImages.objects.filter(detail=detail)
#     context = {
#         'detail': detail,
#         'images': images,
#         'request_user': request.user
#     }

#     return render(request,'template/card_detail.html',context)
   
  