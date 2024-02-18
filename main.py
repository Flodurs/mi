import trainer
import ladder
import tic
import os
import darwin
import net
# l = ladder.ladder()
# for i in range(9999):
    # print("----------\n")
    # l.playTournament() 
    # l.spreadTheWisdom()
    # os.system('cls' if os.name == 'nt' else 'clear')
    
d = darwin.darwin(5,5,5,5)
net = net.net(5,5)
net.printNetHash()
net.setFromGenoType(d.getGenoType(0))
net.printNetHash()
    




    


