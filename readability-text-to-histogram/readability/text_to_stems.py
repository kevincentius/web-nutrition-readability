# you have to first install the packages:
# python -m pip install textstat
# python -m pip install matplotlib
# python -m pip install numpy

from __future__ import division  # Python 2 users only

from nltk import word_tokenize
import nltk, re
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

class TextToStems(object):

    
    def __init__(self, remove_stopwords):
        self.remove_stopwords = remove_stopwords
        
    
    def __clean_text(self, text):
        # remove short in brackets such as (i), (ii), (iii), (a), (b), [1], [2], [3], {1}, {2}, {3}
        text = re.sub(r'\(.{1,3}\)|\[.{1,3}\]|\{.{1,3}\}', ' ', text)
        
        # split text into words
        words = word_tokenize(text)
        words = [token.lower() for token in words if token.isalpha()]
        
        return words
    
    
    def text_to_stems(self, text):
        words = self.__clean_text(text)
        
        # remove stopwords
        if self.remove_stopwords:
            stop_words = set(stopwords.words('english'))
            words = [t for t in words if not t in stop_words]
        
        # stemmer
        stemmer = nltk.stem.SnowballStemmer('english')
        stems = [stemmer.stem(t) for t in words]
        
        
        return stems
    
    
if __name__ == '__main__':
    stemmer = TextToStems()
    text = 'Executive Order 13423 Strengthening Federal Environmental, Energy, and Transportation Management The President Strengthening Federal Environmental, Energy, and Transportation Management By the authority vested in me as President by the Constitution and the laws of the United States of America, and to strengthen the environmental, energy, and transportation management of Federal agencies, it is hereby ordered as follows: Section 1. Policy. It is the policy of the United States that Federal agencies conduct their environmental, transportation, and energy-related activities under the law in support of their respective missions in an environmentally, economically and fiscally sound, integrated, continuously improving, efficient, and sustainable manner. Sec. 2. Goals for Agencies. In implementing the policy set forth in section 1 of this order, the head of each agency shall: (a) improve energy efficiency and reduce greenhouse gas emissions of the agency, through reduction of energy intensity by (i) 3 percent annually through the end of fiscal year 2015, or (ii) 30 percent by the end of fiscal year 2015, relative to the baseline of the agency�s energy use in fiscal year 2003; (b) ensure that (i) at least half of the statutorily required renewable energy consumed by the agency in a fiscal year comes from new renewable sources, and (ii) to the extent feasible, the agency implements renewable energy generation projects on agency property for agency use; (c) beginning in FY 2008, reduce water consumption intensity, relative to the baseline of the agency�s water consumption in fiscal year 2007, through life-cycle cost-effective measures by 2 percent annually through the end of fiscal year 2015 or 16 percent by the end of fiscal year 2015; (d) require in agency acquisitions of goods and services (i) use of sustainable environmental practices, including acquisition of biobased, environmentally preferable, energy-efficient, water-efficient, and recycled-content products, and (ii) use of paper of at least 30 percent post-consumer fiber content; (e) ensure that the agency (i) reduces the quantity of toxic and hazardous chemicals and materials acquired, used, or disposed of by the agency, (ii) increases diversion of solid waste as appropriate, and (iii) maintains cost-effective waste prevention and recycling programs in its facilities; (f) ensure that (i) new construction and major renovation of agency buildings comply with the Guiding Principles for  Federal Leadership in High Performance and Sustainable Buildings set forth in the Federal Leadership in High Performance and Sustainable Buildings Memorandum of Understanding (2006), and (ii) 15 percent of the existing Federal capital asset building inventory of the agency as of the end of fiscal year 2015 incorporates the sustainable practices in the Guiding Principles; (g) ensure that, if the agency operates a fleet of at least 20 motor vehicles, the agency, relative to agency baselines for fiscal year 2005, (i) reduces the fleet�s total consumption of petroleum products by 2 percent annually through the end of fiscal year 2015, (ii) increases the total fuel consumption that is non-petroleum-based by 10 percent annually, and (iii) uses plug-in hybrid (PIH) vehicles when PIH vehicles are commercially available at a cost reasonably comparable, on the basis of life-cycle cost, to non-PIH vehicles; and (h) ensure that the agency (i) when acquiring an electronic product to meet its requirements, meets at least 95 percent of those requirements with an Electronic Product Environmental Assessment Tool (EPEAT)-registered electronic product, unless there is no EPEAT standard for such product, (ii) enables the Energy Star feature on agency computers and monitors, (iii) establishes and implements policies to extend the useful life of agency electronic equipment, and (iv) uses environmentally sound practices with respect to disposition of agency electronic equipment that has reached the end of its useful life. '
    print(stemmer.text_to_stems(text))
