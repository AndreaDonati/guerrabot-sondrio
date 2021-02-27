# The Guerrabot of Sondrio

<a href="http://guerrabot-sondrio.herokuapp.com/guerrabot/"><img src="https://github.com/AndreaDonati/guerrabot-sondrio/blob/master/misc/mock_image_province.JPG?raw=true" align="left" height="50%" width="50%" ></a>
<br />



**guerrabot-sondrio** is a website which lets you spectate and run through the simulation of a war between the villages of the province of Sondrio, Italy.
The simulation of the progression of the war is visualized on an interactive map. You can see the simulation from day one to the end of the war

The website is hosted on Heroku and you can access it [here](http://guerrabot-sondrio.herokuapp.com/guerrabot/).

<br />

<br />

<br />


<br />


## How does the simulation work?
The simulation is already generated and stored on the server, since this website was originally thought to be used as a support for a bigger project which didn't come to a realization.

The simulation runs by events, each event can be thought of as a day. On day one, the initial configuration is given: all the villages are under control of themselves.
Then, every day, a battle between two randomly-selected adjacent villages is simulated, deciding the winner of the battle with a probability based on the number of villages the battlers have conquered in the previous days.
When a village wins, it takes control of the loosing village and of all its conquered ones. The simulation ends when a village has conquered all the province of Sondrio

The simulation is generated (by the means of a few Python scripts) as GeoJSON files, which contain the state of the province each day together with a string identifying what happens on each day, e.g. "Chiuro ATTACCA Ponte in Valtellina. Chiuro VINCE" that means that the two villages Chiuro and Ponte in Valtellina battle and Chiuro comes out as winner taking over the Ponte in Valtellina territories.

## Current State of the Project

The website is far to be finished and complete, various features of visualization are missing or lacking consistency between web and mobile version. However, I think this is a good mockup of what I want the final product to be when it is complete.
