from itertools import count
from django.http import JsonResponse
from django.shortcuts import redirect, render
from main_app.models import Company, Job , User, Job_list
from django.template.loader import render_to_string
import json

# Create your views here.
def login(request):
    request.session['page'] = "login"
    return render(request,'user/login.html')

def register(request):
    request.session['page'] = "register"
    return render(request,'user/register.html')

def post_login(request):
    if request.POST['email'] == "admin" and request.POST['password'] == "admin":
        request.session['fullname'] = "Admin!"
        request.session['page'] = "mainpage"
        return redirect('job_seeker')
    else:
        try:
            found1 = User.objects.get(
                        email=request.POST['email'],password=request.POST['password'])
            request.session['page'] = "mainpage"
            request.session['fullname'] = found1.firstname + " " + found1.lastname
            request.session['user_id'] = found1.id
            request.session['job_type'] = found1.job_type
            # request.session['city'] = found1.city
            # request.session['country'] = found1.country
            return redirect('mainpage')
        except Exception as e:
            print(str(e))
            try:
                found2 = User.objects.get(
                        username=request.POST['email'],password=request.POST['password'])
                request.session['fullname'] = found2.firstname + " " + found2.lastname
                request.session['page'] = "mainpage"
                request.session['user_id'] = found2.id
                request.session['job_type'] = found2.job_type
                # request.session['city'] = found2.city
                # request.session['country'] = found2.country
                return redirect('mainpage')
            except Exception as ee:
                try:
                    found3 = Company.objects.get(
                    email=request.POST['email'],password=request.POST['password'])
                    request.session['company_name'] = found3.company_name
                    request.session['page'] = "mainpage"
                    request.session['company_id'] = found3.company_id
                    return redirect('company_mainpage')
                except Exception as eee:
                    print(str(eee))     
                    return render(request,'user/login.html',{"validation2":"Username or Password is Incorrect."})
    

def post_register(request):
    username = request.POST.get('username')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    print(password)
    if password == confirm_password:
        users = User(
            username=username,
            firstname = firstname,
            lastname = lastname,
            email = email,
            password = password )
        users.save()
        request.session['page'] = "login"
        return render(request,'user/login.html',{"validation":"Successfully Registered. Login your account and search for jobs."})
    else:  
        return render(request,'user/register.html',{"validation":"Password does not match."})

def logout(request):
    request.session['page'] = "login"
    return render(request,'user/login.html')

#main_website

def main_page(request):
    request.session['page'] = "mainpage"
    jobs = Job.objects.all()
    return render(request,'user/mainpage.html',{"jobs":jobs})

def search_job(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            data = request.GET.get('search')
            filter_data = request.GET.get('filter_data')
            if filter_data == "all":
                jobs = Job.objects.filter(job_title=data)
            else:
                jobs = Job.objects.filter(job_title=data,job_type=filter_data)
            variable = []
            for job in jobs:
                variable.append({
                    "job_title":job.job_title,
                    "city":job.city,
                    "country":job.country,
                    "skills":job.skills,
                    "job_id":job.job_id,
                })
            return JsonResponse({'data': variable})
        return JsonResponse({'data': 'Invalid request'}, status=400)

def filter_job(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'GET':
            filter_data = request.GET.get('filter_data')
            jobs = Job.objects.filter(job_type=filter_data)
            variable = []
            for job in jobs:
                variable.append({
                    "job_title":job.job_title,
                    "city":job.city,
                    "country":job.country,
                    "skills":job.skills,
                    "job_id":job.job_id,
                    "job_type":job.job_type,
                })
            return JsonResponse({'data': variable})
        return JsonResponse({'data': 'Invalid request'}, status=400)
        
def resume(request):
    user = User.objects.get(id=request.session['user_id'])
    data = {
        "username":user.username,
        "firstname":user.firstname,
        "lastname":user.lastname,
        "phone":user.phone,
        "gender":user.gender,
        "email":user.email,
        "skills":user.skills,
        "achievements":user.achievements,
        "job_type":user.job_type,
        "profile_picture":user.profile_picture,
    }
    print(user.profile_picture)
    request.session['page'] = "resume"
    return render(request,'user/resume.html',data)

def job_list(request):
    request.session['page'] = "job_list"
    job_list = Job_list.objects.all()
    return render(request,'user/job_list.html',{"job_list":job_list})

def alerts(request):
    request.session['page'] = "alerts"
    alert = Job.objects.all()
    return render(request,'user/alerts.html',{"alerts":alert})


#admin website
def job_seeker(request):
    request.session['page'] = "job_seeker"
    job_seekers = User.objects.all()
    return render(request,'admin/job_seeker.html',{"job_seekers":job_seekers})

def jobs(request):
    request.session['page'] = "jobs"
    jobs = Job.objects.all()
    return render(request,'admin/jobs.html',{"jobs":jobs})

def activity_logs(request):
    request.session['page'] = "activity_logs"
    return render(request,'admin/activity_logs.html')

def company(request):
    request.session['page'] = "company"
    company = Company.objects.all()
    return render(request,'admin/company.html',{"company":company,"job_seeker":job_seeker})


#Company
def company_register(request):
    return render(request,'company/register.html')

def company_mainpage(request):
    jobs = Job.objects.all()
    return render(request,'company/company_mainpage.html',{"jobs":jobs})

def post_company_register(request):
    company_name= request.POST.get('company_name')
    address = request.POST.get('address')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    if password == confirm_password:
        company = Company(
            company_name=company_name,
            address = address,
            email = email,
            password = password )
        company.save()
        request.session['page'] = "login"
        return render(request,'user/login.html',{"validation":"Successfully Registered. Login your account and post a job."})
    else:  
        return render(request,'company/register.html',{"validation":"Password does not match."})

#CRUDS
def edit_resume(request):
    user_id = request.GET.get('user_id')
    username = request.GET.get('username')
    firstname = request.GET.get('firstname')
    lastname= request.GET.get('lastname')
    gender = request.GET.get('gender')
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    skills = request.GET.get('skills')
    achievements = request.GET.get('achievements')
    job_type = request.GET.get('job_type')

    User.objects.filter(id=int(user_id)).update(username=username,firstname=firstname,lastname=lastname,gender=gender,
    phone=phone,email=email,skills=skills,achievements=achievements,job_type=job_type)
    request.session['job_type'] = job_type
    request.session['fullname'] = firstname + " " + lastname
    return redirect(request.META['HTTP_REFERER'])

def apply_job(request):
    job_id = request.GET.get('job_id')
    user_id = request.session['user_id']
    jobs = Job.objects.get(job_id=int(job_id))
    job_list = Job_list(
        full_name = request.session['fullname'],
        job_title=jobs.job_title,
        job_type=jobs.job_type,
        job_details=jobs.job_details,
        skills=jobs.skills,
        city=jobs.city,
        country=jobs.country,
        job_id_get=job_id,
        company_id=request.session['company_id'],
        user_id_get=user_id
        )
    job_list.save()
    
    return redirect(request.META['HTTP_REFERER'])

def delete_user(request):
    user_id = request.GET.get('user_id')
    User.objects.filter(id=user_id).delete()
    return redirect(request.META['HTTP_REFERER'])
def edit_job(request):
     job_id = request.GET.get('job_id')
     job_title= request.GET.get('job_title')
     skills = request.GET.get('skills')
     city = request.GET.get('city')
     country = request.GET.get('country')
     job_details= request.GET.get('job_details')
     job_type= request.GET.get('job_type')

     Job.objects.filter(job_id=job_id).update(job_title=job_title,skills=skills,city=city,country=country,job_details=job_details,job_type=job_type)
     return redirect(request.META['HTTP_REFERER'])

def edit_company(request):
     company_id = request.GET.get('company_id')
     company_name= request.GET.get('company_name')
     address = request.GET.get('address')

     Company.objects.filter(company_id=company_id).update(company_name=company_name,address=address)
     return redirect(request.META['HTTP_REFERER'])

def add_job(request):
     job_title= request.GET.get('job_title')
     skills = request.GET.get('skills')
     city = request.GET.get('city')
     country = request.GET.get('country')
     job_details= request.GET.get('job_details')
     job_type= request.GET.get('job_type')

     job = Job(job_title=job_title,skills=skills,city=city,country=country,job_details=job_details,job_type=job_type,company_id=request.session['company_id'])
     job.save()
     return redirect(request.META['HTTP_REFERER'])
def delete_job(request):
    job_id = request.GET.get('job_id')
    Job.objects.filter(job_id=job_id).delete()
    return redirect(request.META['HTTP_REFERER'])
def delete_job_list(request):
    job_id = request.GET.get('job_id')
    Job_list.objects.filter(job_id_get=job_id).delete()
    return redirect(request.META['HTTP_REFERER'])
def delete_company(request):
    company_id = request.GET.get('company_id')
    Company.objects.filter(company_id=company_id).delete()
    Job.objects.filter(company_id=company_id).delete()
    return redirect(request.META['HTTP_REFERER'])