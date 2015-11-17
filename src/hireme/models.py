from django.db import models

# Create your models here.
class Hire(models.Model):
    CONTRACT_CHOICE = (
        ('gc', 'General Contractor'),
        ('sc', 'Subcontractor'),
        ('st', 'Short Term Contract'),
        ('lt', 'Long Term Contract'),
        ('ct', 'Consultant'),        
    )
    
    PROJECT_CHOICE = (
        ('mw', 'Membership Website'),
        ('ec', 'Ecommerce'),
        ('ls', 'Landing & Sharing Page'),
        ('mc','Maintenance'),
        ('pw', 'Personal Website'),
        ('dw', 'Data Wrangling'),
        ('dp', 'Data Preprocessing'),
        ('dv', 'Data Visualization'),
        ('dp', 'Data Prediction'),
        ('rs', 'Recommender System'),
        ('sm', 'Something else...'),
    )
    DURATION_CHOICE = (
        ('1', '1 - 4 Weeks'),
        ('2', '1 - 8 Weeks'),
        ('3', '1 - 12 Weeks'),
        ('4', '6 Months'),
        ('5', '12 Months'),
        ('6', 'Undefined'),
    )
    
    WHEN_CHOICE = (
        ('1', 'ASAP'),
        ('2', '2 Weeks'),
        ('3', '1 Month'),
        ('4', 'Flexible'),
    )
    
    TECHNOLOGIES_CHOICE = (
        ('1', 'Django'),
        ('2', 'Wordpress'),
        ('3', "I don't know"),
    )
    
    
    project_name = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=True)
    budget = models.CharField(max_length = 100, blank=True)
    contract = models.CharField(max_length=2, choices=CONTRACT_CHOICE, blank=True)
    project = models.CharField(max_length=2, choices=PROJECT_CHOICE, blank=True)
    duration = models.CharField(max_length=1, choices=DURATION_CHOICE, blank=True)
    when = models.CharField(max_length=1, choices=WHEN_CHOICE, blank=True)
    technologies = models.CharField(max_length=1, choices=TECHNOLOGIES_CHOICE, blank=True)
    
    def __str__(self):
        return self.name
    
    
    
    
    