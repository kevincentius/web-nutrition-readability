
from readability.stems_to_freqs import StemsToFreqs
from readability.text_to_stems import TextToStems
from readability.env import Environment
import os
import numpy as np

class HistogramGen:
    
    def generate_histogram(self,
            remove_stopwords = False,
            min_word_count = 50, # ignore texts that are shorter than this
            num_bins = 10,
            cat_ignore_list = ['poetry', 'read aloud poetry', 'drama']
    ):
        stemmer = TextToStems(remove_stopwords = remove_stopwords)
        counter = StemsToFreqs(remove_stopwords = remove_stopwords)
        
        np.set_printoptions(threshold=999999)
        data = np.reshape(np.array([]), [0, 2+num_bins])
        grade_pos = [0] # number of data for each grade
        
        for grade in Environment.grades:
            grade_dir = Environment.data_set_path + grade[1]
            for category in os.listdir(grade_dir):
                if category not in cat_ignore_list:
                    cat_dir = grade_dir + '/' + category
                    for filename in os.listdir(cat_dir):
                        filepath = cat_dir + '/' + filename
                        # exiting with clause will close the file
                        # without 'with' clause, the file will only be closed upon garbage collection
                        with open(filepath, 'r', encoding="utf-8") as file:
                            text = file.read()
                            stems = stemmer.text_to_stems(text)
                            if (len(stems) >= min_word_count):
                                freqs = counter.stems_to_freqs(stems)
                                hist = counter.freqs_to_histogram(freqs, num_bins)
                                total = np.sum(hist)
                                data = np.vstack((data, np.append([grade[0], total], hist/total)))
                                
                    #counter.plot_pow_hist(freqs, num_bins)
            grade_pos.append(len(data))
        
        # normalize class weights so that sum of sample weights in each class = 1
        for i in range(0, 6):
            grade_data = data[grade_pos[i]:grade_pos[i+1]:, 1:2:]
            grade_total_sw = np.sum(grade_data)
            print('grade', Environment.grades[i], len(grade_data), grade_total_sw)
            data[grade_pos[i]:grade_pos[i+1]:, 1:2:] /= grade_total_sw
        
        for i in range(0, 6):
            grade_data = data[grade_pos[i]:grade_pos[i+1]:, 1:2:]
            grade_total_sw = np.sum(grade_data)
            print('grade', Environment.grades[i], len(grade_data), grade_total_sw)
            
        np.savetxt('word_freq_histogram_10', data)
        print(len(data), 'data processed')
        #print(data)

if __name__ == '__main__':
    HistogramGen().generate_histogram()
    
    
