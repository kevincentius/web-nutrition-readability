    
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score



if __name__ == '__main__':
    np.set_printoptions(threshold=999999)
    
    # load data
    load = np.loadtxt('word_freq_histogram_10')
    y = load[::, 0:1:] # first column is label
    sw = load[::, 1:2:] # second column is sample weight
    x = load[::, 2::] # remaining 10 columns are input features (histogram values)
    
    # train vs test
    y_train = y[0::2]
    sw_train = sw[0::2]
    x_train = x[0::2]
    y_test = y[1::2]
    sw_test = sw[1::2]
    x_test = x[1::2]
    
    print(sw_train)
    
    # linear regression model
    regr = linear_model.Ridge(alpha=0.01)
    regr.fit(x_train, y_train, np.reshape(sw_train, [-1]))
    #regr.fit(x_train, y_train)
    
    a_train = regr.predict(x_train)
    print(np.hstack((y_train, a_train)))
    
    a_test = regr.predict(x_test)
    print(np.hstack((y_test, a_test)))
    
    # smart? guess
    y_avg_test = np.repeat(np.average(y_test), len(y_test))
    #y_avg_test = np.repeat(np.sum(np.multiply(y_test, sw_test)) / np.sum(sw_test), len(y_test))
    print(np.average(y_test), np.sum(np.multiply(y_test, sw_test)) / np.sum(sw_test))
    print(np.sum(sw_test))
    
    #print('STUPID MSE', mean_squared_error(y_test, y_avg_test, sw_test))
    #print('TRAIN MSE', mean_squared_error(y_train, a_train, sw_train))
    #print('TEST MSE', mean_squared_error(y_test, a_test, sw_test))
    print('STUPID MSE', mean_squared_error(y_test, y_avg_test))
    print('TRAIN MSE', mean_squared_error(y_train, a_train))
    print('TEST MSE', mean_squared_error(y_test, a_test))
    print('coef: ', regr.coef_)
