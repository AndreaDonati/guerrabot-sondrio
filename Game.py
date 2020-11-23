import random
import numpy as np

from Comune import Comune
from Comune import Provincia
from Comune import NoComuniConqueredError

from GameStateHandler import GameStateHandler
#-----------------------------------------------------------#
#                        GAME SETUP                         #
#-----------------------------------------------------------#
sondrio = Provincia()
event_1 = "Attacco"
event_2 = "Insurrezione"
possible_game_events = [event_1, event_2]
possible_game_events_probabilities = [0.9,0.1]
gameStateHandler = GameStateHandler(sondrio)

def processGameEvent(event):
    if event == event_1:
        return processEvent1()
    elif event == event_2:
        return processEvent2()

def processEvent1():
    # select two random Comuni. One is the Comune which will attack,
    # and the other is the attacked Comune.
    selected_comune, target = sondrio.getRandomComuneAndTarget()
    if target == True:
        return selected_comune, True, ""
    outcome = selected_comune.name + " ATTACCA " + target.name + "."
    #print(outcome)
    # make the two comuni fight and get the winner
    winner, game_finished = sondrio.battle(selected_comune, target)
    outcome += " E "+ winner + " VINCE."
    print(winner + " VINCE.")
    return winner, game_finished, outcome

def processEvent2():
    # select two random Comuni. One is the Comune which will handle the Insurrezione,
    # and the other is the insurging Comune (previously conquered by the first Comune).
    selected_comune = sondrio.getRandomComune()
    try:
        print(selected_comune.name +" " +str(len(selected_comune.conquered)))
        insurging_comune = random.choice(selected_comune.conquered)
    except IndexError:
        raise NoComuniConqueredError
    outcome = insurging_comune.name + " INSORGE SU " + selected_comune.name + ", riconquistando il proprio territorio."
    print(outcome)
    # make the two comuni fight and get the winner
    insurgent, game_finished = sondrio.insurge(insurging_comune, selected_comune)
    outcome
    return insurgent, game_finished, outcome

#-----------------------------------------------------------#
#                         GAME LOOP                         #
#-----------------------------------------------------------#
while True:
    #select the event to be processed in this turn
    event = np.random.choice(possible_game_events, p=possible_game_events_probabilities)
    try:
        winner, game_finished, outcome = processGameEvent(event)
        # scrivo sul json e in qualche modo dico alla pagina di leggerlo
        gameStateHandler.save_state("")
    except NoComuniConqueredError:
        print("Impossible to insurge on a Comune which has not yet conquered other Comuni.")

    input()

    if game_finished:
        print(winner.name + " E' IL VINCITORE ASSOLUTO DEL MONDO WOW BRV")
        break