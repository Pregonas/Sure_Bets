from code.tennis.oddspedia import tennis_match
from code.tennis.oddspedia_life import live_tennis_match
from code.tennis_table.odds_tennis_table import tennis_table
from code.tennis_table.odds_live_tennis_table import live_tennis_table
from code.basket.basket_life import basket_life
from code.basket.basket import basket
from code.voleibol.voleibol import voleibol
from code.voleibol.voleibol_life import voleibol_life
from code.esports.esports import esports
from code.esports.esports_life import esports_life
from code.dards.dards import dards
from code.dards.dards_life import dards_life
from code.futbol_america.futbol_america_life import futbol_america_life
from code.futbol_america.futbol_america import futbol_america
from code.baseball.baseball import baseball
from code.baseball.baseball_life import baseball_life
from code.arts_marcials.arts_marcials import arts_marcials
from code.billar.billar import billar
from code.fut_australia.fut_australia import fut_australia
import time
from code.timer import timer

t = 0
while t < 60:
    timer()
    tennis_match()
    tennis_table()
    basket()
    dards()
    voleibol()
    esports()
    futbol_america()
    baseball()
    arts_marcials()
    billar()
    fut_australia()
    # live_tennis_match()
    # baseball_life()
    # futbol_america_life()
    # esports_life()
    # voleibol_life()
    #basket_life()
    #dards_life()
    #live_tennis_table()
    time.sleep(300)

    t = t + 1
