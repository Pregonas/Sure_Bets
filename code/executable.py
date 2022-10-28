from code.tennis.oddspedia import tennis_match
from code.timer import timer
import time

t = 0
while t < 60:
    timer()
    tennis_match()
    
    time.sleep(300)

    t = t + 1
