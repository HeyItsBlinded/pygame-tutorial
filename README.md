## works cited
derived from the 'Pong' project by Clear Code on Youtube. original source code found here: https://github.com/clear-code-projects/Pong_in_Pygame

## deviation(s) from original code:
* 2-player support: left player uses W/S, right player uses up arrow/down arrow <br>
* serving, like in tennis: after each round/when the ball is out of play, it resets in the middle and is triggered again by the space bar <br>
* win condition: when player1 or player2 hits 5 points, both scores reset to 0
* no countdown timer

## edge cases to work on
* the space bar can be used to reset the ball while it is still in play (solved)

## nice to haves
* game finished/over screen once win condition is satisfied
* instructions disappear once ball is in play
* ball does not begin immediately once loaded in