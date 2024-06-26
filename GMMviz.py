##-----------GNN_ND.py--------------------- 
#import sys 
#import pandas as pd 
#import math 
#import numpy as np 
#import random 
#from scipy.stats import multivariate_normal 
#import matplotlib.pyplot as plt 
#from scipy.stats import mode 
 
#def compute_gaussian_probab(x, mu, cov, d):  # d is the number of dimensions in data 
#    xmu = np.matrix(x - mu) 
#    exponent = np.exp(-0.5 * xmu*np.linalg.inv(cov)*xmu.T) 
#    denom = 1 / np.sqrt(((2*np.pi)**d) * np.linalg.det(cov)) 
#    res = denom * exponent 
#    #distribution = multivariate_normal(mu, cov) 
#    #res2 = distribution.pdf(x) 
#    return res 
 
#def E_Step(xdata,mu,cov,d, kc, phi, gamma): 
#    #-----------E step----------------- 
#    N = xdata.shape[0] 
#    for i in range(0,N): 
#        denom = 0 
#        for j in range(0,kc): 
#            denom = denom + (phi[j] * compute_gaussian_probab(xdata[i,:],mu[j],cov[j],d)) 
#        for k in range(0,kc): 
#            gamma[i,k] = (phi[k] * compute_gaussian_probab(xdata[i,:],mu[k],cov[k],d))/denom 
 
#def M_Step(xdata, mu, cov, d, kc, phi, gamma): 
#    #-----------M step----------------- 
#    N = xdata.shape[0] 
#    phi = np.mean(gamma,axis=0) 
#    sumgk = np.sum(gamma, axis=0) 
#    for k in range(0,kc): 
#        mu[k] = np.zeros((d)) 
#        for i in range(0,N): 
#            mu[k] = mu[k] + (xdata[i,:] * gamma[i,k]) 
#        mu[k] = mu[k]/sumgk[k] 
 
#    for k in range(0,kc): 
#        cov[k] = np.zeros((d,d)) 
#        for i in range(0,N): 
#            xmu = np.matrix(xdata[i,:] - mu[k]) 
#            cov[k] = cov[k] + ((xmu.T*xmu) * gamma[i,k]) 
#        cov[k] = cov[k]/sumgk[k] 
 
#def plot_iris(xdata, clusters): 
#    plt.figure(figsize=(10, 6)) 
#    plt.title('GMM Clusters for Car Dataset') 
#    plt.scatter( # since we  
#       xdata[:,0],  
#       xdata[:,2],  
#        c=clusters,
#        cmap=plt.cm.get_cmap('brg'), 
#        marker='.') 
#    plt.tight_layout() 
#    plt.show() 
 
#def main(): 
#    #---------------Iris Dataset------------- 
#    df = pd.read_csv('C:\\Users\\iansp\\OneDrive\\Documents\\Grad School\\Spring 2023\\Data Mining\\cardataset.csv') 
#    #---randomize data 
#    dfrandom = df #df.sample(frac=1, random_state=1119).reset_index(drop=True) 
#    # data read from a file is read as a string, so convert the first 4 cols to float 
#    df1 = dfrandom.iloc[:,0:6].astype(float) 
#    #---separate out the last column 
#    df2 = dfrandom.iloc[:,6] 
#    #---combine the 4 numerical columns and the last column that has the flower category 
#    #dfrandom = pd.concat([df1,df2],axis=1) 
     
#    xdata = df1.values 
#    xdata = xdata[:,0:6] 
#    print(xdata.shape) 
 
#    #--------------GMM N-D Algorithm----------------- 
#    kc = 3  # cluster count 
#    d = 6   # dimensionality of data 
#    N = xdata.shape[0] 
#    np.random.seed(42) 
#    mu = np.zeros((kc,d)) 
#    cov = np.zeros((kc,d,d)) 
 
#    #-----------initialization step------------ 
#    phi = np.full(kc,1/kc) 
#    random_row = np.random.randint(low=0, high=2000, size=kc) 
#    mu = np.array([xdata[row,:] for row in random_row ]) 
#    mean_data = np.mean(xdata,axis=0) # mean of entire data (column wise) 
#    xmu = np.matrix(xdata-mean_data) 
#    cov = np.array([xmu.T*xmu/N for k in range(kc)]) 
    
#    print(phi) 
#    print(mu) 
#    #print(cov) 
#    N = len(dfrandom) 
#    gamma = np.zeros((N,kc)) 
#    print(gamma.shape) 
 
#    num_iterations = 20 
#    for n in range(0,num_iterations): 
#        E_Step(xdata, mu, cov, d, kc, phi, gamma) 
#        M_Step(xdata, mu, cov, d, kc, phi, gamma) 
#        print('----------------iteration =',n) 
  
#    #---------final result-------- 
#    print(mu) 
#    print(gamma) 
#    print(phi) 

#    #-----compute accuracy-------- 
#    preds = [] 
#    for i in range(0,N): 
#        pred = np.argmax(np.multiply(gamma[i,:],phi)) 
#        preds.append(pred) 
#    print(preds) 
#    plot_iris(xdata, preds) 
 
#    cluster_assigned = [] 
#    # since GMM is unsupervised, class assignments to clusters may vary on each run 
#    cluster_assigned = [mode(preds[0:385])[0], mode(preds[385:454])[0], mode(preds[454:1664])[0], mode(preds[1664:1729])[0]]
#    acc = 0 
#    for i in range(0,N): 
#        if preds[i] == cluster_assigned[0] and i < 385: # first 385 members belong to class acc
#            acc = acc + 1 
#        if preds[i] == cluster_assigned[1] and i >=385 and i < 454: # next 50 are class 1 
#            acc = acc + 1
#        if preds[i] == cluster_assigned[2] and i >=454 and i < 1664: # next 50 are class 1 
#            acc = acc + 1 
#        if preds[i] == cluster_assigned[3] and i >= 1664 and i < 1729: # last 50, class 2 
#            acc = acc + 1  
         
#    print('accuracy =',acc/N*100) 
 
#if __name__ == "__main__": 
#    sys.exit(int(main() or 0)) 