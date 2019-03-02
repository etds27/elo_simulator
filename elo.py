#!/usr/bin/python3

import math
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from operator import itemgetter

class Player:
    def __init__(self, elo,skill,id):
        self.elo = elo
        self.skill = skill
        self.id = id
        #print(elo,skill,id)

total_games=0
better_player=0
better_elo=0

def match(player1,player2):
    p1 = 1.0 / (1 + 10 ** ((player2.elo - player1.elo ) / 400) )
    p2 = 1 - p1
    rand = random.randint(0,100)
    skilldiff = (player1.skill - player2.skill) / float(1000)

    #print( p1,p2,player1.elo,player2.elo)
    if rand - skilldiff < p1 * 100:
        player1.elo += 32 * (1 - p1)
        player2.elo += 32 * (0 - p2)
    elif rand - skilldiff > p1 * 100:
        player1.elo += 32 * (0 - p1)
        player2.elo += 32 * (1 - p2)
    else:
        player1.elo += 32 * (0.5 - p1)
        player2.elo += 32 * (0.5 - p2)


    #print(float(better_player/total_games),float(better_elo/total_games))


    #print( p1,p2,player1.elo,player2.elo)
    #print()

    #time.sleep(3)
    #print(rand,skilldiff,player1.elo,player2.elo)


skill = np.array([])
playerlist1 = []
for i in range(0,10000):
    skills =  0 #random.randint(-10000,10000)
    playerlist1.append(Player(1000,skills,i))
    skill = np.append(skill,skills)

num_of_matches = int(len(playerlist1) / 2)

#playerlist1 = []
playerlist2 = []
elo = np.array([])
skill = np.array([])

plt.ion()
fig = plt.figure()
splt = plt.subplot(111)
fig.show()

all = []

for i in range(0,1000):
    #for i in range(0,50):
    #    skills = random.randint(-150,150)
    #    playerlist2.append(Player(1000,skills,len(playerlist2) + 1))
    #    skill = np.append(skill,skills)
    #num_of_matches = int(len(playerlist2) / 2)
    #playerlist1 = playerlist2
    for j in range(num_of_matches):
        p1 = playerlist1.pop(random.randrange(len(playerlist1)))
        p2 = playerlist1.pop(random.randrange(len(playerlist1)))
        #print(p1.id,p2.id)
        playerlist2.append(p1)
        playerlist2.append(p2)

        match(p1,p2)
        elo = np.append(elo,p1.elo)
        elo = np.append(elo,p2.elo)

        all.append([p1.elo,p1.skill,p1.id])
        all.append([p2.elo,p2.skill,p2.id])

    splt.cla()
    playerlist1, playerlist2 = playerlist2, []

    n, bins = np.histogram(elo,bins=200)
    #n2, bins2, patches = splt.hist(skill,bins=100, facecolor='blue')
    #y,binEdges=np.histogram(data,bins=100)
    bincenters = 0.5*(bins[1:]+bins[:-1])
    plt.plot(bincenters,n,'r--')
    #plt.plot(bins, y, 'r--')
    #print (elo)
    plt.xlabel('Rating')
    plt.ylabel('People')
    plt.title('Histogram of Elo')
    #plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([min(elo), max(elo), 0, 300])
    plt.grid(True)

    fig.canvas.draw()
    #time.sleep(.1)

    #print(np.sort(elo))
    for play in sorted(all, key=itemgetter(1)):
        print("Elo: %f | Skill %i | Id: %i" % (play[0],play[1],play[2]))
        pass
    elo = []
    all=[]
