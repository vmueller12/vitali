import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import re

#example_sent = "This is a sample sentence, showing off the stop words filtration."

class Sentiment(object):
    
    
    def __init__(self, text):
        self.stopwords = stopwords.words('english')
        self.sentence = text
        self.words = word_tokenize(self.sentence)
        self.sent_split = sent_tokenize(self.sentence)
        self.remove_char = [' ',',','.',',','!','?',':']
        self.filter_words = [w for w in self.words if w not in self.remove_char]
        self.all_words = nltk.FreqDist(self.filter_words)
        self.all_words_cleaned = nltk.FreqDist([wc for wc in self.filter_words if wc not in self.stopwords])
            
    
    def stopwordsCounter(self):
        counter = 0
        for w in self.words:
            if w in self.stopwords:
                counter +=1
        return counter
    
    
    def totalWords(self):
        return len(self.words)
    
    
    def totalSentences(self):
        return len(self.sent_split)
    
    
    def avWordsPerSentence(self):
        words_per_sent = []
        for words in self.sent_split:
            words = [w for w in word_tokenize(words) if w not in self.remove_char]
            words_per_sent.append(len(words))
        return (sum(words_per_sent)/float(self.totalSentences()))
    
    
    def topFiveWords(self):
        return self.all_words.most_common(5)
    
    def topFiveWordsCleaned(self):
        return self.all_words_cleaned.most_common(5)
    
    
    def wordCounterBySearchInput(self, searchWord):
        """Method has an string word as an input. It looks for the given word in the text
            and counts the frequency. It returns an integer value.
        """
        return self.all_words[searchWord]
 
    
    def ratioTotalWordStopWord(self):
        return (self.totalWords()/float(self.stopwordsCounter()))
    
    



class TopWordsRetriever(object):

    def __init__(self, text):

        self.text = text

    def topWords(self):
        regex = re.compile(r'\((.*?)\)')
        text = regex.findall(self.text)

        num = []
        words = []

        for i in text:
            num.append(i.split(",")[1])
            words.append(i.split(",")[0])

        return words, num
    
    def wordProcessing(self, con):
        
        new_text = con.replace('[','').replace(']','').replace("'",'').replace(',','')
        return word_tokenize(new_text)

        
    
        