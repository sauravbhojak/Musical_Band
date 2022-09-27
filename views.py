from atexit import register
from django.http import HttpResponse
import email
from multiprocessing import context
from random import randint
import re
from tkinter import Place
from tokenize import Name
from urllib import request
from django.shortcuts import render,redirect
from .utils import *
from app.models import Admin, Artist, Book_show, Contact, Highlight, Myvideos, Team, User, event, feedback_data, followers
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils import timezone
from pytz import timezone
import datetime
import math

from pytz import timezone
# Create your views here.

@csrf_exempt
def Indexpage(request):
    vid = ''
    if 'email' in request.session:
        events = event.objects.all().order_by('-id').values()
        fol = followers.objects.all()
        vid1 = Myvideos.objects.get()
        vid = vid1.video
        print('vid--------------------->',vid)
        all_fol = len(fol)
        context = {'all_event':events,'unfollower':'kai pan','all_fol':all_fol,'vid':vid}
        email = request.session['email']
        
        followers_email = followers.objects.filter(Email=email)
        print('follow-unfollow---------------------------->',followers_email)
        if followers_email:
            context = {'all_event':events,'follower':'kai pan','all_fol':all_fol,'vid':vid}
            if request.POST:
                fol = followers.objects.get(Email=email)
                fol.delete()
                context = {'all_event':events,'unfollower':'kai pan','all_fol':all_fol,'vid':vid}
                return render(request,'app/index.html',context)
            else:
                return render(request,'app/index.html',context)
        else:     
            print("Second Else-------------------->")
            context = {'all_event':events,'unfollower':'kai pan','all_fol':all_fol,'vid':vid}
            if request.POST:
                print("Create object--------------------->")
                context = {'all_event':events,'follower':'kai pan','all_fol':all_fol,'vid':vid}
                dt = datetime.datetime.now()
                print("Date:----------------------------->",dt)
                fol = followers.objects.create(Email=email, created_at=dt)
                return render(request,'app/index.html',context)
            else:
                return render(request,'app/index.html',context)

        # else:
        #     return render(request,'app/index.html',context)
    else:
        events = event.objects.all()
        print("Place-------------------------->",events)
        context = {'all_event':events,'unfollower':'kai pan','vid':vid}
        return render(request,'app/index.html',context) 
    
    

def Admin_index(request):
    if 'email' in request.session:
        dt = datetime.datetime.now()
        ti = dt.time()
        DT = dt.date()
        now = ti.strftime("%H:%M:%S")
        follow  = followers.objects.all().order_by('-id').values()
        show    = Book_show.objects.last()
        contact = Contact.objects.last()
        feed    = feedback_data.objects.all().order_by('-id').values()
        user = User.objects.all().order_by('-id').values()
        print("User------------------>",user)

        follow_user = td_data(follow)
        follow_users = follow_user[0]
        follow_time = follow_user[1]
        feed = feed[0]

        context = {'DT':follow_time,'follow':follow_users,'show':show,'contact':contact,'feed':feed,'user':user}
        
        return render(request,'app/admin/index.html',context)
    else:
        return render(request,'app/admin/login.html')

# def ago(t1,t2):
#     t1 = datetime.strptime(t1, "%H:%M:%S")
#     t2 = datetime.strptime(t2, "%H:%M:%S")
#     ago_time = t1-t2
#     return ago_time

def td_data(nam):
    print(nam)
    ago_time = ""
    data = []
    dt = datetime.datetime.now()
    DT = dt.date()
    now = dt.strftime("%H:%M:%S")
    
    
    for i in nam:
        if DT==i['created_at'].date():
            t2F = i['created_at'].time()
            t2f = t2F.strftime("%H:%M:%S")
            t1 = datetime.datetime.strptime(now, "%H:%M:%S")
            t2 = datetime.datetime.strptime(t2f, "%H:%M:%S")
            ago_time = t1-t2
            data.append(i)
        else:
            pass
    return data,ago_time





def aboutus(request):
    return render(request,'app/about.html')

def admin_reg(request):
    return render(request,'app/admin/register.html')

def loginpage(request):
    return render(request,'app/admin/login.html')

def ad_register(request):
    Fname = request.POST['fname']
    email = request.POST['email']
    psw = request.POST['psw']
    cpsw = request.POST['cpsw']
    
    user = Admin.objects.filter(Email=email)
    
    if user:
            message = "User Already Register!"
            return render(request, "app/admin/login.html",{'msg':message})
    else:
        if psw == cpsw:
            otp = randint(1000000,9999999)
            newuser = Admin.objects.create(
                    Email=email, Password=psw, OTP=otp)
            newartist = Artist.objects.create(
                user_id=newuser, Firstname=Fname)
            email_subject = "Tutor Finder : Account Verification"
            # sendmail(email_subject,'mail_template',email,{"name":Fname,'otp':otp,'link':'http://localhost:8000/enterprise/user_verify/'})
        
            return redirect("loginpage")    
        else:
            message = "Password & Confirm Password do not match"
            return render(request, "app/admin/register.html", {'msg': message})
        
def charts_page(request):
    return render(request,'app/admin/charts.html')

def password_page(request):
    return render(request,'app/admin/password.html')

def table_page(request):
    return render(request,'app/admin/tables.html')

def layout_1(request):
    return render(request,'app/admin/layout-sidenav-light.html')

def layout_2(request):
    return render(request,'app/admin/layout-static.html')

def Not_Found(request):
    return render(request,'app/admin/404.html')

def teams_page(request):
    return render(request,'app/admin/teams.html')

def register_user(request):
    if request.POST:
        u_name = request.POST['u_name']
        email = request.POST['email']
        pswd = request.POST['pswd']     
        user = User.objects.create(
            u_name = u_name,
            Email = email,
            Password = pswd,
        )
        context = {'user':'data'}
        return render(request,'app/login_user.html',context)
    else:
        return render(request,'app/register.html')

def logout_user(request):
    if "email" in request.session:
        del request.session['email']
        return redirect(login_user)
    else:
        return redirect(login_user)

def login_user(request):
    if 'email' in request.session:
        print("already iin ---------------------->")
        return redirect(Indexpage)
    else:
        if request.POST:
            email = request.POST['email']
            pswd = request.POST['pswd']
            try:
                data = User.objects.get(Email=email)
                print("data------------->",data.Password)
                print('successfully executed data part-------->')                
                if data:
                    if data.Password == pswd:
                        request.session['email'] = data.Email
                        print("email set to session---------------------->")
                        return redirect(Indexpage)
                    else:
                        context={"e_msg":"Invalid id or password"}
                        return render(request,"app/login_user.html",context)
                else:
                    print('Data not found')
            except:
                context={"e_msg":"invalid id or password"}
                return render(request,"app/login_user.html",context)
        else:
            return render(request,'app/login_user.html')
            

def event_page(request):
    if 'email' in request.session:
        all_events = event.objects.all()
        print(all_events)
        context_eve = {
            "all_event":all_events
            }
        if request.POST:    
            date = request.POST['date']
            day = request.POST['day']
            place = request.POST['place']
            new_event = event.objects.create(
                Date = date,
                Day = day,
                Place = place,
            )
            return render(request,'app/admin/event.html',context_eve)
        else:
            return render(request,'app/admin/event.html',context_eve)

def all_artist(request):
    if 'email' in request.session:
        artist = Team.objects.all()
        print('----------------------->',artist)
        return render(request,"app/admin/about_band.html",{'artist_data':artist})
    else:
        return redirect(loginpage)
    
def about_band(request):
    return render(request,'app/about_band.html')

def contact(request):
    if 'email' in request.session:
        if request.POST:
            dat = datetime.now()
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['sub']
            msg = request.POST['msg']
            
            contact_us = Contact.objects.create(
                Name = name,
                Email = email,
                Sub = subject,
                Msg = msg,
                created_at = dat
            )
            context={"msg":"Sent...!"}
            return render(request,'app/contact.html',context)
        else:
            return render(request,'app/contact.html')
    else:
        return render(request,"app/login.html")
        


@csrf_exempt
def ad_login(request):
    if 'email' in request.session:
        return redirect(Admin_index)
    else:
        if request.POST:
            email = request.POST['email']
            psw   = request.POST['psw']           
            try:
                data = Admin.objects.get(Email=email)
                print('successfully excuted data part')              
                if data:
                    if data.Password == psw:
                        request.session['email'] = data.Email
                        return redirect(Admin_index)
                    else:
                        context={"e_msg":"Invalid id or password"}
                        return render(request,"app/admin/login.html",context)
                else:
                    print('Data not found')
            except:
                context={"e_msg":"invalid id or password"}
                return render(request,"app/admin/login.html",context)
            
def logout(request):
    if "email" in request.session:
        del request.session['email']
        return redirect(loginpage)
    else:
        return redirect(loginpage)


def profile(request):
    
    if "email" in request.session:
        print('in session--------------->',request.session['email'])
        
        data = Admin.objects.get(Email=request.session['email'])
        cid = Artist.objects.get(user_id=data)
        context = { 
                   "data":data,
                   "cid":cid,
                   }
        return render(request,'app/admin/profile.html',context)
    else:
        print('not found')
        return render(request,'app/admin/myapp/login.html')
    
def edit_profile(request):
    if "email" in request.session:
        if request.POST:
            data = Admin.objects.get(Email = request.session['email'])    
            cid  = Artist.objects.get(user_id=data)
            if cid:
                firstname = request.POST["fname"]
                contact   = request.POST["contact"]
                dob       = request.POST["dob"]
                gender    = request.POST["gender"]
                role      = request.POST["role"]
                if "pic" in request.FILES:
                    cid.profile_pic = request.FILES["pic"]
                    cid.save()
                context ={
                        's_msg' : "Successfully Profile Updated",
                        'cid' : cid,
                        "data": data,
                    }
                cid.Firstname = firstname
                cid.Contact  = contact
                cid.DOB = dob
                cid.gender = gender
                cid.Role = role
                cid.save()
                return render(request,"app/admin/profile.html",context)
            else:
                return redirect(profile)
        else:
            return redirect(profile)
    else:
        return render(request,'app/admin/login.html')
    
def photos(request):

    if "email" in request.session:
        if request.POST:
            pass
        else:
            return redirect(profile)
    else:
        return render(request,'app/admin/login.html')
    
def add_artits(request):
    if "email" in request.session:
        if request.POST:
            firstname = request.POST["name"]
            aka       = request.POST["aka"]
            contact   = request.POST["contact"]
            Description = request.POST["description"]
            dob       = request.POST["dob"]
            role      = request.POST["role"]
            profile_pic = request.FILES["pic"]
            context ={
                    's_msg' : "Successfully Done",
                }
            newartist = Team.objects.create(
                        Name           = firstname, 
                        As_known_as    = aka,
                        Descricription = Description,
                        Role           = role,
                        Contact        = contact,
                        DOB            = dob,
                        profile_pic    = profile_pic
                        )
            return redirect('about_band')
        else:
            return redirect(teams_page)
    else:
        return render(request,'app/admin/teams.html')
    
def Delete_artitst(request,pk): 
    if 'email' in request.session:
        ddata = Team.objects.get(id=pk)
        ddata.delete()
        return redirect('all_artitst')
    else: 
        return redirect(loginpage)
    

def feedback(request):
    if 'email' in request.session:
        if request.POST:           
            feedback = request.POST['feedback']
            da = datetime.datetime.now()  
            u_id = User.objects.get(Email=request.session['email'])
            em = u_id.Email
            print("u_id----------------->",em)
            feedbacks = feedback_data.objects.create(
                Email = em,
                Feedback = feedback,
                created_at = da
            )
            context = {'msg':'Successfully Sent Your Feedback..!',
                       'email':em}
            return render(request,'app/feedback.html',context)
        else:
            return render(request,'app/feedback.html')
    else:
        return redirect(login_user)
    
    
def all_feedback(request):
    if 'email' in request.session:
        data = feedback_data.objects.all()
        context = {'data':data}
        return render(request,'app/admin/feedback.html',context)
    else:
        return redirect(loginpage)
    
    
    
def all_followers(request):
    if 'email' in request.session:
        follor = followers.objects.all().order_by('-id').values()
        
    return render(request,'app/admin/followers.html',{'data':follor})
    
    

def book_show(request):
    if 'email' in request.session:
        if request.POST:
            details = request.POST['details']
            # email = request.POST['email']      
            u_id = User.objects.get(Email=request.session['email'])
            em = u_id.Email
            print("u_id----------------->",em)
            dt = datetime.datetime.now()
            bool_details = Book_show.objects.create(
                Email = em,
                Details = details,
                created_at = dt 
            )
            context = {'msg':'Successfully Sent Your Show Booking Request..!',
                       'email':em}
            return render(request,'app/book-show.html',context)
        else:
            return render(request,'app/book-show.html')
    else:
        return redirect(login_user)    


def all_show(request):
    if 'email' in request.session:
        shows = Book_show.objects.all().order_by('-id').values()
        return render(request,'app/admin/all_shows.html',{'data':shows})

def add_video(request):
    if 'email' in request.session:
        if request.POST:
            videos = Myvideos.objects.create(
                title=request.POST['title'],
                video = request.POST['video']
                )
            return render(request,'app/admin/add_video.html')
        else:
            return render(request,'app/admin/add_video.html')



def test(request):
    obj = Team.objects.filter(Role='Drummer')
    print('OBJ-------------------------->',obj)
    for i in obj:
        print(i.Name,i.Role)
    return HttpResponse("<h1>Hello See in CMD::::::::---------------></h1>")


