
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.urls import reverse
from .models import job
from .form import Applyform,Addform
from django.contrib.auth.decorators import login_required
from .filters import JobFilter



# Create your views here.
def job_list(request):
    job_list=job.objects.all()
    
    myfilter=JobFilter(request.GET,queryset=job_list )
    job_list=myfilter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    context ={'jobs':page_obj , 'myfilter':myfilter}
    return render(request,'job/job_list.html',context)


def job_detail(request,slug):
    job_detail=job.objects.get(slug=slug)
    if request.method =='POST':
        form = Applyform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job= job_detail
            myform=form.save() 
    
    else:
        form = Applyform()
    
    context={'job':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)   
    
@login_required    
def add_job(request):
    if request.method =='POST':
        form = Addform(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner= request.user
            myform.save() 
            return redirect(reverse('jobs:job_list'))
    
    else:
        form = Addform()
    
    return render (request,'job/add_job.html',{'form':form})    