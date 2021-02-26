# The Guerrabot of Sondrio

**guerrabot-sondrio** is a website which lets you spectate and run through the simulation of a war between the villages of the province of Sondrio, Italy.
The simulation of the progression of the war is visualized on an interactive map. You can see the simulation from day one to the end of the war

The website is hosted on Heroku and you access it [here](http://guerrabot-sondrio.herokuapp.com/guerrabot/).

## How does the simulation work?

The simulation is already generated and stored on the server, since this website was originally thought to be used as a support for a bigger project which didn't come to a realization.

The simulation runs by events, each event can be thought of as a day. On day one, the initial configuration is given: all the villages are under control of themselves.
Then, every day, a battle between two randomly-selected adjacent villages is simulated, deciding the winner of the battle with a probability based on the number of villages the battlers have conquered in the previous days.
When a village wins, it takes control of the loosing village and of all its conquered ones. The simulation ends when a village has conquered all the province of Sondrio
It is generated (by the means of a few Python scripts) as GeoJSON files, which contain

## Current State of the Project
