from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

JOB_TYPE = [
    ("full time","full time"),
    ("part time","part time"),
]
# Create your models here.
class job (models.Model):
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    descrition =models.TextField(max_length=1000,default='descrition')
    published_at =models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=1)
    experiance=models.IntegerField(default=1)
    catagory=models.ForeignKey('Categ',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='jobs/')
    slug=models.SlugField(blank=True,null=True)
    
    def save (self,*args,**kyarges):
        self.slug = slugify(self.title)
        super(job,self).save(*args,**kyarges)
    
    def __str__(self):
        return self.title
    
class Categ (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name   


class Applay (models.Model):
    job= models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    website=models.URLField()
    cv=models.FileField(upload_to='Applay/')
    cover=models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
    
      

   