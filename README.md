## works cited
derived from the 'Pong' project by Clear Code on Youtube. original source code found here: https://github.com/clear-code-projects/Pong_in_Pygame

## deviation(s) from original code:
* 2-player support: left player uses W/S, right player uses up arrow/down arrow <br>
* serving, like in tennis: after each round/when the ball is out of play, it resets in the middle and is triggered again by the space bar. instructions are included <br>
* win condition: when player1 or player2 hits 5 points, both scores reset to 0 <br>
* no countdown timer <br>
* player colors different <br>
* ball does not begin immediately once loaded in <br>

## edge cases to work on
* (SOLVED) the space bar can be used to reset the ball while still in play <br>
* (SOLVED) instructions don't reappear after the first point is scored <br>
* (SOLVED) var 'counter' created and working. purpose: to increment speed each time rally += 5

## nice to haves
* game finished/over screen once win condition is satisfied <br>