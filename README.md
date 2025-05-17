Overview
This is a simple Flask web app that lets you search MLB players by name and view their stats like batting average, home runs, and RBIs. It also calculates potential payout based on betting odds and a bet amount you input.

Installation
Make sure you have Python installed.

Install Flask by running:

pip install flask

Run the app with:

python app.py

What the Website Has
Search bar to find MLB players by name.

Player stats displayed: batting average, home runs, RBIs.

Input box to enter a bet amount.

Potential payout calculated and shown based on player odds and your bet.

How to Use
Enter a player’s name in the search box.

Enter your bet amount.

Submit the form to see matching players, their stats, and your potential payout.

How Potential Payout is Calculated
The payout is calculated using the formula:
Potential Payout = Bet Amount × Player Odds
Player odds are predefined decimal odds associated with each player.

Players Included
The app currently includes these MLB players:
Aaron Judge, Freddie Freeman, Paul Goldschmidt, Jacob Wilson, Manny Machado, Will Smith, Brendan Donovan, Steven Kwan, Bobby Witt Jr., Shohei Ohtani, Jonathan Aranda, Alex Bregman, Pete Alonso, Fernando Tatis Jr., Jeremy Pena, CJ Abrams, Josh Smith, Josh Naylor, Trea Turner, Maikel Garcia, Kyle Stowers, Luis Arraez, Kerry Carpenter, Gavin Lux, Jose Ramirez, Bo Bichette, Geraldo Perdomo, Gleyber Torres, Jake Meyers, Vladimir Guerrero Jr., Hunter Goodman, Gavin Sheets, Francisco Lindor, Heliot Ramos, Jung Hoo Lee, Brice Turang, Corbin Carroll, Rhys Hoskins, Zach McKinstry, Pete Crow-Armstrong, Nico Hoerner, Andy Pages, Joey Bart, Austin Riley, Tyler Soderstrom, Keibert Ruiz, Mike Yastrzemski, Nick Castellanos, Riley Greene, J.P. Crawford, and many more.

