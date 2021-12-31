# Pokemon Type Simulation

Inspired by the WolfeyVGC's video ([https://www.youtube.com/watch?v=8DQyRktcG00](youtube.com/watch?v=8DQyRktcG00)) about the best single and dual types in Pokemon, I wanted to create a simulation to determine programmatically which types are the best.

Overall, I'm satisfied with the results of the simulation as there is some overlap between the ranking mentioned in the video (especially including the honorable mentions) and the ranking I found.

The major difference was my simluation underrated the cost of having a 4x weakness and underrated the benefit of having an immunity.
This is because my simulation only simulated a single battle between two pokemon with the pokemon only using moves of their type(s) (aka STAB moves.
Thus, for example a Water/Ground pokemon who has a 4x weakness to Grass only gets punished by Grass pokemon. 

In a real battle, trainers would have access to multiple pokemon and pokemon with coverage moves (moves that are not their type). Both of these increase the chance of being punished for 4x weaknesses and underrate the benefit of having immunities.


Simulation's Top 5
1. Ground, Water
2. Flying, Ground
3. Ground, Fire
4. Steel, Flying
5. Flying, Water

Wolfey's Top 5 (with the simulation's ranking in parenthesis)
1. Fairy, Steel (14)
2. Ghost, Normal (38)
3. Fairy, Ground (8)
4. Fairy, Water (11)
5. Flying, Ground (2)
