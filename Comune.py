import json
import random
import numpy as np

class Comune:

    def __init__(self, name = None):
        self.name = name
        #self.position?
        #self.descritpion?
        self.owned_by = None
        self.conquered = []
        self.adjacents = []
        # assign random color
        self.color = random_color()

    def conquer(self, other):
        self.conquered.append(other)
        other.owned_by = self
        for com in other.conquered:
            com.owned_by = self
            self.conquered.append(com)

        
        self.conquered = list(set(self.conquered))
        other.conquered = []

        self.adjacents.extend(other.adjacents)
        self.adjacents = list(set(self.adjacents))
        other.adjacents = []

        # if len(other.conquered) == 0:
        #     self.conquered.append(other)
        #     other.owned_by = self
        #     try:
        #         self.adjacents.remove(other)
        #     except ValueError:
        #         pass
        #     return
        # if other == self:
        #     print("ORCODIO")
        #     return

        # other.updateOwner(self)
        # self.conquered = list(set(self.conquered))

    def updateOwner(self, new_owner):
        if len(self.conquered) == 0:
            return
        for com in self.conquered:
            com.updateOwner(new_owner)
            new_owner.conquered.extend([com])
            new_owner.conquered = list(set(new_owner.conquered))
            self.conquered = []
            try:
                new_owner.adjacents.remove(self)
            except ValueError:
                pass
        for c in new_owner.conquered:
            print("--------------A:"+c.name)
    
    def getAdjacents(self):
        # updatedAdj = []
        # for conq in self.conquered:
        #     updatedAdj.extend(conq.getAdjacents())
        # self.adjacents.extend(list(updatedAdj))
        self.adjacents = list(set(self.adjacents)-set([self])-set(self.conquered))
        # assert self not in self.adjacents
        return self.adjacents

class Provincia:

    def __init__(self):
        self.name = "Sondrio"
        self.loadAdjacencyTable()
        self.loadComuni()

    def loadAdjacencyTable(self):
        #load (centralized) adjacency table AS A DICTIONARY OF LISTS
        with open('./resources/adjacencies.json') as json_file: 
            data = json.load(json_file)
        self.adjacency_table = data

    def loadComuni(self):
        #initialize two comuni list, onw to be updated and the other maintining the starting state
        self.comuni = {}
        self.default_comuni = {}
        #create a Comune object for each of the comuni in the keys list 
        for name_comune in self.adjacency_table.keys():
            self.comuni[name_comune] = (Comune(name_comune))
            self.default_comuni[name_comune] = self.comuni[name_comune]

        for name_comune in self.adjacency_table.keys():
            for adj_name in self.adjacency_table[name_comune]:
                self.comuni[name_comune].adjacents.append(self.comuni[adj_name])
        # DEBUG
        # assert len(self.comuni) == len(self.adjacency_table.keys())
        # for comune in self.comuni:
        #     print(comune)

    def getRandomComuneAndTarget(self):

        while True:
            attacker = self.comuni[random.choice(list(self.comuni.keys()))]
            target = attacker
            #non dovrei neanche checkarlo
            #while attacker.owned_by is not None:
            #    attacker = attacker.owned_by
            #print("Selected attacker: "+attacker.name)
            #print("Adiacenze:")
            #for bcomune in attacker.getAdjacents():
            #    print(bcomune.name+", ", end="")
            try:
                target = random.choice(attacker.getAdjacents())
            except IndexError:
                # VITTORIA DEL COMUNE SCELTO COME ATTACKET
                # perché non avere nessuno nelle adiacenze significa avere conquistato tutti
                return attacker, True
                # ciao = attacker.name
                # while  len(ciao)!=0:
                #     self.printBattleStats(ciao)
                #     ciao = input()
            while attacker.owned_by is not None:
                attacker = attacker.owned_by
            #print("Selecting target...")
            #print("A possible target is: "+ target.name + "OWNED by: "+str(target.owned_by))
            while target.owned_by is not None:
            #    print("OWNED by: "+target.owned_by.name)
                target = target.owned_by
            
            if attacker != target:
                break

        return attacker, target

    def printBattleStats(self,nome):
        attacker = self.comuni[nome]
        print("Conquistati da "+ attacker.name + ":" + str(len(attacker.conquered)))
        for bcomune in attacker.conquered:
            print(bcomune.name+", ", end="")
        print("Adiacenze:")
        for bcomune in attacker.adjacents:
            print(bcomune.name+", ", end="")
        print("")

    def getRandomComune(self):
        return self.comuni[random.choice(list(self.comuni.keys()))]

    def battle(self, attacker, attacked):
        # select a winner of the battle (NOW: RANDOMLY)
        winner = self._selectWinner(attacker,attacked)
        loser = attacked.name if winner == attacker.name else attacker.name
        # update the adjacencies and the attributes of the two involved Comuni
        #self.adjacency_table[winner].extend(self.adjacency_table[loser])
        # remove duplicates
        #self.adjacency_table[winner] = list(set(self.adjacency_table[winner]))
        # replace loser with winner in the adjacency list
        #for adj in self.adjacency_table.keys():
        #    if loser in self.adjacency_table[adj]:
        #        self.adjacency_table[adj].remove(loser)
        #        if winner not in self.adjacency_table[adj]:
        #            self.adjacency_table[adj].append(winner)        

        # remove loser from the Provincia adj list and Comuni list
        # set the loser comune as defeated and add it to the conquered list of the winner
        self.comuni[winner].conquer(self.comuni[loser])
        # print(winner + " VINCE.")
        # print("ECCALLAH:")
        # ciao = input()
        # while  len(ciao)!=0:
        #     self.printBattleStats(ciao)
        #     ciao = input()
        self.default_comuni[loser]=self.comuni.pop(loser)
        #assert loser not in list(self.comuni.keys())
        #self.adjacency_table[loser]

        #DEBUG
        #print(self.comuni.keys())
        #print(self.adjacency_table)
        #print(self.comuni[winner].conquered)

        return winner, False

    def _selectWinner(self, attacker, attacked):
        # first implementation: choosing the winner randomly
        # return random.choice([attacker, attacked]).name
        
        # more decent implementation: counting how many Comuni one controls
        # and assign a probability of win according to those number
        atkr = len(attacker.conquered)
        atkd = len(attacked.conquered)
        sum_conq = atkr+atkd
        return np.random.choice([attacker,attacked],p=[atkr/sum_conq,atkd/sum_conq]).name if sum_conq != 0 else random.choice([attacker, attacked]).name


    def insurge(self, insurgent, other):
        # put the insurgent comune back in the comuni list
        self.comuni[insurgent.name] = insurgent
        # remove insurged comune from the owner's owned list
        other.conquered.remove(insurgent)
        # insurgent is no more owned by anyone
        insurgent.owned_by = None
        # restore insurgent adjacencies
        insurgent.adjacents = []
        for com_name in self.adjacency_table[insurgent.name]:
            try:
                insurgent.adjacents.append(self.comuni[com_name])
            except KeyError:
                pass
            insurgent.adjacents.append(other)
            insurgent.adjacents = list(set(insurgent.adjacents))
        return insurgent, False

    def getAllComuniNames(self):
        return list(self.adjacency_table.keys())

    def getComuneByName(self, name):
        return self.default_comuni[name]

class NoComuniConqueredError(Exception):
            pass

def random_color():
    rgbl = [random.randrange(255), random.randrange(255), random.randrange(255)]
    return '#%02x%02x%02x' % tuple(rgbl)

