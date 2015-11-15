from nltk import word_tokenize
import pickle
from nltk.corpus import stopwords




class PosNegCounter(object):
    
    def __init__(self, content):
        
        # A List of negative Words
        open_file = open("pickle/negativeWordList.pickle", "rb")
        negList = pickle.load(open_file)
        open_file.close()
        
        open_file = open("pickle/swearing.pickle", "rb")
        swearing = pickle.load(open_file)
        open_file.close()
        
        
        # A list of positive words
        open_file = open("pickle/positiveWordList.pickle", "rb")
        posList = pickle.load(open_file)
        open_file.close()
        
        # contains english stopwords and other single characters
        open_file = open("pickle/all_removals.pickle", "rb")
        all_removals = pickle.load(open_file)
        open_file.close()
        

        self.posList = posList
        self.negList = negList
        self.swearingList = swearing
        self.all_removals = all_removals
        # spliting the text into words, removing all stopwords and characters.
        self.content = [w for w in word_tokenize(content) if w.lower() not in all_removals]
        self.total = len(self.content)
        
    
    def posNegCounter(self):
        pos = int(len([w for w in self.content if w in self.posList]))
        neg = int(len([w for w in self.content if w in self.negList]))
        return pos, neg
    
    def swearingCount(self):
        return len([w for w in self.content if w in self.swearingList])
    
    def positiveWords(self):
        return [w for w in self.content if w in self.posList]
    
    def negativeWords(self):
        return [w for w in self.content if w in self.negList]
    
    def swearingWords(self):
        return [w for w in self.content if w in self.swearingList]
    
    def ratioTotalWordsPosNeg(self):
        # returns a ratio total words / positive
        # and ration total words / negative
        pos, neg = self.posNegCounter()
        ratiopos = int(self.total/pos)
        rationeg = int(self.total/neg)
        return ratiopos, rationeg
    

class MachineLearningClass(object):
    
    def __init__(self, content):
        
        documents_f = open("pickle/documents.pickle", "rb")
        documents = pickle.load(documents_f)
        documents_f.close()

        word_features5k_f = open("pickle/word_features_3000.pickle", "rb")
        word_features = pickle.load(word_features5k_f)
        word_features5k_f.close()
        
        open_file = open("pickle/originalnaivebayes5k.pickle", "rb")
        classifier = pickle.load(open_file)
        open_file.close()
               
        open_file = open("pickle/MNB_classifier5k.pickle", "rb")
        MNB_classifier = pickle.load(open_file)
        open_file.close()
        
        open_file = open("pickle/BernoulliNB_classifier5k.pickle", "rb")
        BernoulliNB_classifier = pickle.load(open_file)
        open_file.close()

        self.documents = documents
        self.word_features = word_features
        self.classifier = classifier
        self.MNB_classifier = MNB_classifier
        self.BernoulliNB_classifier = BernoulliNB_classifier
        self.content = content
        
        
    def find_features(self):
        words = word_tokenize(self.content)
        features = {}
        for w in self.word_features:
            features[w] = (w in words)
        return features
        
    def mlAnalyser(self):
        first = self.classifier.classify(self.find_features())
        second = self.MNB_classifier.classify(self.find_features())
        third = self.BernoulliNB_classifier.classify(self.find_features())
        classifier_list = [first, second, third]
        return classifier_list#list of classifier
        
    
    def outputClassifier(self):
        # counts how many positive and negative outcomes and calculates the procentage
        # and outputs the category
        neg_counter = len([w for w in self.mlAnalyser() if w == 'neg'])
        pos_counter = len([w for w in self.mlAnalyser() if w == 'pos'])
        
        if pos_counter > neg_counter and pos_counter == 3:
            return [100, 'pos']
        
        elif pos_counter > neg_counter and pos_counter == 2:
            return [66, 'pos']
        
        elif neg_counter > pos_counter and neg_counter == 3:
            return [100, 'neg']
        
        elif neg_counter > pos_counter and neg_counter == 2:
            return [66, 'neg']
        
        else:
            return [0, 'error']



    

            
        
            

                


