from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save

from .sentiment import Sentiment






class InputText(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    slug = models.SlugField(unique=True)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("sent_detail", kwargs={'slug':self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(InputText, self).save(*args, **kwargs)
    


        

class SentAnalysis(models.Model):
    inputText = models.OneToOneField(InputText, primary_key = True)
    stopWords = models.IntegerField()
    totalWords = models.IntegerField()
    avWordsSentence = models.DecimalField(max_digits=1000, decimal_places=2)
    totalSentences = models.IntegerField()
    topWords = models.TextField()
    topFiveWordsCleaned = models.TextField()
    ratioTotalStopwords = models.DecimalField(max_digits=200, decimal_places=2)
    slug = models.SlugField()
    #ratioWordsSentences = models.DecimalField(max_digits=200, decimal_places=2)
    
    def __str__(self):
        return self.slug
    
    
class MachineLearning(models.Model):
    inputText = models.OneToOneField(InputText, primary_key = True)
    positiveWords = models.TextField()
    negativeWords = models.TextField()
    swearingWords = models.TextField()
    positiveCounter = models.IntegerField()
    negativeCounter = models.IntegerField()
    swearingCounter = models.IntegerField()
    ratioTotalWordsPositive = models.IntegerField()
    ratioTotalWordsNegative = models.IntegerField()
    naiveBayes = models.CharField(max_length = 5)
    mnb = models.CharField(max_length = 5)
    bernoulliNB = models.CharField(max_length = 5)
    confidence = models.IntegerField()
    totalCategory = models.CharField(max_length = 5)
    slug = models.SlugField()
    
    def __str__(self):
        return self.slug
    

    
    

    
   
    
   
    
    
    
    
