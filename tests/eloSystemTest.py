import sys
sys.path.insert(0, "../")

import eloSystem

eloSys = eloSystem.eloSystem(5)


    
eloSys.printElos()

eloSys.matchPlayed(1,2,1)
eloSys.matchPlayed(1,2,0)


eloSys.printElos()