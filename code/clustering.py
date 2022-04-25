
import pandas as pd
import sys
from sys import argv
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.spatial import distance # euclidean distance
import time

start = time.time()
columns = ['object_id','X','Y']
path = sys.argv[1]
n = int(sys.argv[2])
eps = int(sys.argv[3])
minpts = int(sys.argv[4])
data = pd.read_csv(path, sep='\t',names=columns)


index_c = []
X_C = [] # build cluster
Y_C = [] # build cluster

def show_graph(x,y,s):
    if s == 8:
        plt.figure(figsize=[s, s])
    else:
        plt.figure(figsize=[s*3, s])
    plt.scatter(x, y, s=1, c='b')
    plt.xlabel("$X$", fontsize=15)
    plt.ylabel("$Y$", fontsize=15, rotation=0)
    plt.show()

def pick_point(object_id):
    while True:
        p = random.choice(object_id)  #get point from data randomly
        if p > -1:
            break
    return p

def Build_Cluster(cluster, px, py, index):
    global X_C
    global Y_C
    global index_c
    global object_id
    
    ''' Find Core point that satisfies distance(epsilon)'''
    
    # get distance from px to total points
    # get distance from py to total points
    # collect points in the diameter(eps)
    a = np.array([px,py])
    b = np.array([np.array([total_X[i],total_Y[i]]) for i in object_id])
    dist = get_distance(a,b)
    # filtering (choose only distance with <= eps)
    candidate_points = object_id[dist <= eps]
    candidate_points = candidate_points[candidate_points > -1]
    #candidate_points = [i for i, j in zip(object_id, dist) if j <= eps and i > -1]
    
    ''' draw the cluster with min points '''
    
    if len(candidate_points) >= minpts:
        candidate_points = set(candidate_points) - set(index_c)
        for i in candidate_points:
                index_c.append(i)
                X_C.append(total_X[i])
                Y_C.append(total_Y[i])
    #elif index > minpts:
        
        #return object_id
        #noise_data = list(set(candidate_points).difference(set(index_c)))
        #data = data.drop(data.index[[noise_data]])
        #print(len(candidate_points),':', len(noise_data), end=' ')
        
        
    index += 1
    if index < len(index_c):
        Build_Cluster(cluster, X_C[index], Y_C[index], index)
    elif index == 0:
        #print('noise',end=' ')
        remove_checked_data(candidate_points)
        p = pick_point(object_id)
        Build_Cluster(cluster, total_X[p], total_Y[p], index)
    else:
        return object_id

def get_distance(a,b):
    distance = np.sum((a-b)**2, axis = 1)
    distance = distance ** 0.5
    return distance

def remove_checked_data(index_c):
    for i in index_c:
        object_id[i] = -1
    return object_id

if __name__ == '__main__':
    total_X = list(data['X'])
    total_Y = list(data['Y'])
    object_id = np.array(data['object_id'])
    show_graph(total_X, total_Y, 8)
    i = 0
    size = object_id[object_id > -1].size
    while size > minpts:
        index = -1
        p = pick_point(object_id) #pick one
        Build_Cluster(i,total_X[p], total_Y[p],index)
        if len(index_c) >= minpts:
            print()
            i += 1
            print("cluster:",i,':', size)
            show_graph(X_C, Y_C, 2)
        object_id = remove_checked_data(index_c)
        X_C.clear()
        Y_C.clear()
        index_c.clear()
        size = object_id[object_id > -1].size
    print("execution time for Clustring :", str(round((time.time() - start),1)) +'s')
    
