from django.views import generic
from .sentiment import Sentiment
from .forms import TextFieldForm
from .models import InputText
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView

from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .sentiment import Sentiment, TopWordsRetriever
from .models import SentAnalysis


    
class SentimentDelete(DeleteView):
    model = InputText
    
    def get_success_url(self):
        return reverse('sent_list')
    
    
class SentimentUpdate(UpdateView):
    model = InputText
    form_class = TextFieldForm
    template_name = "sentiment/index.html"
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        # create a instance for Sentiment()
        try:
            sent = SentAnalysis()
            ins = Sentiment(self.object.content)
            sent.inputText = self.object
            sent.totalWords =  int(ins.totalWords())
            sent.totalSentences = int(ins.totalSentences())
            topFive = ins.topFiveWords()
            topCleaned = ins.topFiveWordsCleaned()
            topWords = ",".join("(%s,%s)" % tup for tup in topFive)
            topWCleaned = ",".join("(%s,%s)" % tup for tup in topCleaned)
            sent.topFiveWordsCleaned = topWCleaned
            sent.topWords = topWords
            sent.stopWords = int(ins.stopwordsCounter())
            sent.slug = self.object.slug
            sent.ratioTotalStopwords = float(ins.ratioTotalWordStopWord())
            sent.avWordsSentence = float(ins.avWordsPerSentence())
            sent.save()
        except:
            print("Error")
        return super(SentimentUpdate, self).form_valid(form)


class SentimentCreate(CreateView):
    form_class = TextFieldForm
    template_name = "sentiment/index.html"
    #model = InputText
    #fields = ['title', 'content']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = slugify(self.object.title)
        self.object.save()
        # create a instance for Sentiment()
        try:
            sent = SentAnalysis()
            ins = Sentiment(self.object.content)
            sent.inputText = self.object
            sent.totalWords =  int(ins.totalWords())
            sent.totalSentences = int(ins.totalSentences())
            topFive = ins.topFiveWords()
            topCleaned = ins.topFiveWordsCleaned()
            topWords = ",".join("(%s,%s)" % tup for tup in topFive)
            topWCleaned = ",".join("(%s,%s)" % tup for tup in topCleaned)
            sent.topFiveWordsCleaned = topWCleaned
            sent.topWords = topWords
            sent.stopWords = int(ins.stopwordsCounter())
            sent.slug = self.object.slug
            sent.ratioTotalStopwords = float(ins.ratioTotalWordStopWord())
            sent.avWordsSentence = float(ins.avWordsPerSentence())
            sent.save()
        except:
            print("Error")
        return super(SentimentCreate, self).form_valid(form)
    
#    def form_valid(self, form):
#        self.object = form.save(commit=False)
        
#        self.object.slug = slugify(self.object.title)
#        print(self.object.title)
#        print(self.object.content)
#        self.object.save()
#        return super(SentimentCreate, self).form_valid(form)
    
class SentimentDetail(DetailView):
    template_name = 'sentiment/detail.html'
    model = InputText
    
    
    def get_context_data(self, **kwargs):
       
       
        context = super(SentimentDetail, self).get_context_data(**kwargs)
        try:
            qrsAnalysis = SentAnalysis.objects.get(slug=self.object.slug)
            topW = TopWordsRetriever(qrsAnalysis.topWords)
            words, num = topW.topWords()
            #topCl = TopWordsRetriever(qrsAnalysis.topFiveWordsCleaned)
            #wC, nC = topC1.topWords()
            context['stopWords'] = qrsAnalysis.stopWords
            context['totalWords'] = qrsAnalysis.totalWords
            context['averageWPS'] = int(qrsAnalysis.avWordsSentence)
            context['totalSentences'] = qrsAnalysis.totalSentences
            context['ratioWS'] = int(qrsAnalysis.ratioTotalStopwords)
            context['word1'] = words[0]
            context['word2'] = words[1]
            context['word3'] = words[2]
            context['word4'] = words[3]
            context['word5'] = words[4]
            context['num1'] = num[0]
            context['num2'] = num[1]
            context['num3'] = num[2]
            context['num4'] = num[3]
            context['num5'] = num[4]
            
            topCL = TopWordsRetriever(qrsAnalysis.topFiveWordsCleaned)
            wC, nC = topCL.topWords()
            
            
            context['wC1'] = wC[0]
            context['wC2'] = wC[1]
            context['wC3'] = wC[2]
            context['wC4'] = wC[3]
            context['wC5'] = wC[4]
            context['nC1'] = nC[0]
            context['nC2'] = nC[1]
            context['nC3'] = nC[2]
            context['nC4'] = nC[3]
            context['nC5'] = nC[4]
            
        except:
            pass
        #print(context)
        return context
    
    
    
    
class SentimentList(ListView):
    template_name = 'sentiment/list.html'
    model = InputText
    
    def get_queryset(self, *args, **kwargs):
        qs = super(SentimentList, self).get_queryset(*args, **kwargs).order_by("-created")
        return qs