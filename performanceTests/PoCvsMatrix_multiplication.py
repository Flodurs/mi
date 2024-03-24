import numpy as np
import time


import sys
sys.path.insert(0, "../")
import net


#Test Result: Matrix Multiplication is 30-50 times faster (and increasingly better with higher connection numbers


nodeNum = 1000

n = net.net(nodeNum,nodeNum**2)



cons = np.zeros((1000,1000))
input = np.zeros(1000)












def testMatrixMultiplication():
    t0 = time.time()
    for x in range(1000):
        output = np.matmul(cons,input)
    t1 = time.time()
    print(t1-t0)
    
    
def testNetStep():
    t0 = time.time()
    for x in range(1000):
        n.step()
    t1 = time.time()
    print(t1-t0)
    

testMatrixMultiplication()
testNetStep()