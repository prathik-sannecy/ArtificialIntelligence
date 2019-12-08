Project: Gothello  
Class: PSU CS 441/541 - Artificial Intelligence (Fall 2019)  
Author: Prathik Sannecy  
Email: prathik@pdx.edu  
Date: 12/5/19

This project provides a player to play the game Gothello (Gothello description can be found here: https://github.com/pdx-cs-ai/gothello-project/blob/master/README.md). It connects to the Gothello Game Server, and can play as either the 'white' or 'black' player.

The way that the program works is that it first connects to the Gothello Game server, and tells it whether it is the 'black' player or the 'white' player. The Gothello game server keeps track of the game, and this program (client) communicates with it to figure out whether it is the client's turn, and what move the opponent has made. If it is the client's turn, it will send over the move it wants to make to the game server.

This program also keeps track of the game, and updates its own copy of the state of the board at every turn (both itself, and the opponent's). Based on this state, it will decide what its next move should be. It uses a MiniMax algorithm to figure out the move that will lead to a state (after a certain number of moves) that is the worse possible one for the opponent (and thus the best for this program). The number of moves to predict a future state is called the 'depth', and is specified by the user running the program.

The way this program decides how good (or bad) a state is by a simple comparison of its own stones vs the opponent's. Basically, it tries to maximize the number of its own stones, while minimizing the number of stones of the opponent. Also, all other things being equal, this program gives a preference to spots in the middle, since these are harder to completely surround.

Since the program is written in Python, it runs slower than the Grossthello (https://github.com/pdx-cs-ai/gothello-grossthello) player written in Java. In general, when I played this Grosthello program versus the Java Grossthello version, this version usually won when both players used search depth 3 (won 4 out of 5 games), but lost when both players used search depth 4 (lost 4 out of 5 games). With a depth larger than 4, this program would hang.

To evaluate this program, I played this program against itelf, against a 'dummy' player that made random moves (https://github.com/pdx-cs-ai/gothello-libclient-python3/blob/master/gthrandom.py), and the Java Grossthello program. When I played it against itself, ensured that it ties every game since both sides know exactly what move the opponent will do (same algorithm), and will try to counter it. When I played it against the random player, I ensured that this program won every time. Finally, I played this program against the Java Grossthello player to see how well it would perform against an actual strategic opponent (see analysis in the above paragraph).

From this project, I learned how to write a program using AI to play a game similar to humans would (if not better). In general, I don't think humans would be able to predict 3 or 4 moves into the future, so I'm sure that this program would be able to beat many people. Because of this, I now understand why computers are able to beat some of the best in games like chess. Also, in terms of AI techniques, I learned how to implement the MiniMax function with depth limited search, and how increasing the depth exponentially increases memory usage and computation time.

In the future, I would like to try the following:
1. Write the program in C, so that it runs faster and can use a larger depth
2. Use a better heuristic. The difference in the number of stones (described above) is a very simple heuristic, but can be improved. For example, stones in different positions may be worth more (and thus have a larger weight) than stone in other positions.
3. Keep a list of states near the end of the game that show what move I should do next to guarantee a win. Then, if I ever reach one of these states, I can just follow the list to win the game.

To run this program (automatically runs on server number 0):
1. Run the Gothello Game Server (https://github.com/pdx-cs-ai/gothello-gthd): java Gthd 0
2. Run this Gothello player: python3 GothelloRun.py [white|black] [search depth]  
Example: python3 GothelloRun.py white 3
3. Run the opponent. Can be either this same program, the random player (see above), or the Java Grossthello player (see above)  

The output is sent to stdout from the Gothello Game Server.
