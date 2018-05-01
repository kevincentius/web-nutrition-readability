import numpy as np

if __name__ == '__main__':
    a = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    
    print(a)
    print(a.T[1::].T)
    
    b = np.ones([3, 3])
    b[:,:2:] = (a[:,1::])
    print(b)
    pass