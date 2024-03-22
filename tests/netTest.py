import os
import darwin
import net


n = net.net(5,5)

for x in range(999):
    
    n.reset()
    n.setNode(0,1.0)

    for i in range(10):
        n.step()
        

    print(n.getNode(4))