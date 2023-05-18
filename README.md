# Fantasy-Football-Player-Rankings
This repository contains a Python script for calculating fantasy football player rankings based on provided statistics. The script loads player season statistics from a JSON file, applies specific equations for each player position, and ranks the players accordingly. It also calculates team scores based on the scores of players in certain positions.

## Prerequisites:
* Python 3.x
* pandas library
* scikit-learn library

## Installation

### Clone this repository:
`git clone https://github.com/your-username/your-repo.git`

### Install the required libraries:
`pip install pandas scikit-learn`

## Usage

Ensure that the `PlayerSeasonStats.json` file is present in the same directory as the script.

Run the script:
`python fantasy_rankings.py`

The script will print the player rankings for each position and the team scores.


## Results
The script generates rankings for the following player positions:
* WR (Wide Receiver)
* QB (Quarterback)
* RB (Running Back)
* TE (Tight End)
* K (Kicker)
* DT (Defensive Tackle)
* DE (Defensive End)
* CB (Cornerback)
* S (Safety)

For each position, the top 35 players based on their scores are displayed, along with the last 5 scores. Additionally, the team scores are calculated based on the scores of players in the DT, DE, CB, and S positions.







