import numpy as np
x=np.array(([2,9],[1,9],[3,6]),dtype=float)
y=np.array(([92],[86],[89]),dtype=float)
x=x/np.amax(x,axis=0)
y=y/100

def sigmoid(x):
    return 1/(1+np.exp(-x))
    
def derivation_sigmoid(x):
    return x*(1-x)
    
epoch=5000
lr=0.1
inputlayer_neurons=2
hiddenlayer_neurons=3
outputlayer_neurons=1

wb=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bb=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,outputlayer_neurons))
bout=np.random.uniform(size=(1,outputlayer_neurons))
for i in range(epoch):
    hinp1=np.dot(x,wb)
    hinp=hinp1+bb
    hlayer_act=sigmoid(hinp)
    outinp1=np.dot(hlayer_act,wout)
    outinp=outinp1+bout
    output=sigmoid(outinp)
    
    EO=y-output
    outgrad=derivation_sigmoid(output)
    d_output=EO*outgrad
    EH=d_output.dot(wout.T)
    hiddengrad=derivation_sigmoid(hlayer_act)
    d_hiddenlayer=EH*hiddengrad
    wout+=hlayer_act.T.dot(d_output)*lr
    wb+=x.T.dot(d_output)*lr
    
print("Inpput:\n" +str(x))
print("Actual:\n" +str(y))
print("Predicted:\n",output)

------------------------------------------------
OUTPUT:-

Inpput:
[[0.66666667 1.        ]
 [0.33333333 1.        ]
 [1.         0.66666667]]
Actual:
[[0.92]
 [0.86]
 [0.89]]
Predicted:
 [[0.89184048]
 [0.88433366]
 [0.89399225]]
