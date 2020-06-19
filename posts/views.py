from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User, auth
from .filters import OrderFilter
import json
from django import forms
import datetime
from django.utils import timezone
from django.utils.timezone import utc
from .forms import UserProfileForm


# Create your views here.
def posts(request):
    #posts = Post.objects.filter(author_id=request.user).order_by('updated')
    posts = Post.objects.order_by('updated')
    #selected_mentors = Post.objects.order_by().values_list('mentor', flat=True).distinct('mentor')
    return render(request, 'all_posts.html', {'posts': posts})

"""
def selectPost(request):
    #selected_mentors = Post.objects.order_by().values_list('mentor', flat=True).distinct('mentor')
    #print(selected_mentors)

    if request.method == 'POST':
        quothree = request.POST['quothree']
        print(quothree)
        #selected_posts = Post.objects.filter(mentor=mentor).order_by('updated')
        #if selected_posts == None:
        print("no mentors")
            #posts = Post.objects.order_by('updated')
            #return render(request, 'all_posts.html', {'posts': posts})
        #    return redirect('all_posts.html')
        #else:
        return render(request, 'all_posts.html')
    else:
        #posts = Post.objects.filter(author_id=request.user).order_by('updated')
        posts = Post.objects.order_by('updated')
        return render(request, 'all_posts.html', {'posts': posts})

def addMentor(request):
    if request.POST:
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save(commit=False)
            return redirect('all_posts.html')
    else:
        return redirect('home.html')
        
    return render(request, 'all_posts.html', {'profile_form': profile_form})
"""

def writePost(request):

    #selected_mentors = Post.objects.order_by().values_list('mentor', flat=True).distinct('mentor')
    #print(selected_mentors)

    if request.method == 'POST':
        quoone = request.POST['quoone']
        quotwo = request.POST['quotwo']
        quothree = request.POST['quothree']
        post = Post(quoone=quoone, quotwo=quotwo, quothree=quothree, seen = 0, author_id=request.user.pk)
        post.save()
        print('Post created')
        return redirect('all_posts')
        """
        if request.POST['mentor'] == "":
            mentor = request.POST['newmentor']
            post = Post(description=description, contenttype=contenttype, mentor=mentor, seen = 0, author_id=request.user.pk)
            post.save()
            print('Post created')
            return redirect('all_posts')
        else:
            mentor = request.POST['mentor']
            post = Post(description=description, contenttype=contenttype, mentor=mentor, seen = 0, author_id=request.user.pk)
            post.save()
            print('Post created')
            return redirect('all_posts')
        """
    else:
        #selected_mentors = Post.objects.order_by().values_list('mentor', flat=True).distinct('mentor')
        return render(request, 'write_post.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

#class NameForm(forms.Form):
   # id = forms.IntegerField(label='id')


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})

def dailyPosts(request):

    if request.method == 'POST':
        #Formid = request.GET.get(id)
        #thePost = Post.objects.get(pk = Formid)
        #thePost.seen += 1
        #thePost.save()
        daily_posts = Post.objects.filter(author_id=request.user).order_by('seen','-updated')[:5]
        for post in daily_posts:
            print(post.id)
            post.seen += 1
            post.save()
        #id = request.GET.get('id')
        #post = Post.objects.get(id=post_id)
        #post.seen = post.seen + 1
        #post.save()
        print('Post updated')
        return redirect('all_posts')

    else:
        daily_posts = Post.objects.filter(author_id=request.user).order_by('seen','-updated')[:5]
        return render(request, 'daily_posts.html', {'daily_posts': daily_posts})
        
        #def find_daily_posts():
        #    return render(request, 'daily_posts.html', {'daily_posts': daily_posts})
        #schedule.every(3).seconds.do(find_daily_posts) 
        #while 1:
        #    schedule.run_pending()
        #    time.sleep(1)



        #print(request)
        #print(request.POST)
        #print(request.POST['id'])
        #post_id = NameForm(request.POST)
        #print(post_id.id)
        #body_unicode = request.body.decode('utf-8')
        #body = json.loads(body_unicode)
        #print(body)
