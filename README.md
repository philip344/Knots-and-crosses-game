	Noughts and crosses Paper
My goal:
My goal is to make a program that can play noughts and crosses (tic tac toe) optimally. 
o	I cannot use any form of preprocessing.
o	It should run relatively fast.
o	It must be dynamic (it cannot be a series of if statements, this means it could be expanded to connect four more easily).
o	No external libraries should be used.
o	It must be my own idea (I cannot watch a video that details how to make a perfect tic tac toe script and take inspiration)

Algorithm:

The way I went about making my program was a simple idea, but everything is easier said than done.
Let us take a different game first. In this game two players alternate picking branches until we hit the base node of the tree in which that value is selected:
P1 goes first and wants the highest score possible.
P2 goes second and wants the lowest score possible. 
In this game one strategy/algorithm we can use to play optimally is called minimax (min max). This is when a player picks the instance in which he maximizes his results even if the opponent was to play the most detrimental move towards him. Maximizing the yield under the assumption that the opponent plays perfectly (the best move from the opponent’s perspective)
In this scenario that would entail player one picking node c. This is because it yields the best results when playing against a perfect opponent. The reason for this pick, would be because you would go to the base node and assign the node above the highest or lowest value depending on the turn. If the turn is the opponents at that level of the tree, then assign the lowest value to the parent node. However, if it is your turn at that level of the tree, assign the highest value.
Along with other limitations which I am sure I haven’t thought of one of the most major ones is of identical parental node values. For instance, if we were to change node b1’s value to 3. In this scenario node a and node b would be given the same value when it may be more beneficial to pick node b since the mistake the opponent could make may be more beneficial towards us. Moreover, another limitation is that this would not work for complex games where there are too many base nodes or in imperfect information games.
My method:

In my scenario I will have some function create a tree of all noughts and crosses positions and assign the ending nodes different values:
 1 for X winning. 
-1 for O winning 
0 for no one winning. 
Then these values will be escalated like in the above game and a script will pick whichever it finds appropriate depending on if the computer is X or O. If it is X, it will pick the highest value while if its O it will pick the lowest values.

Limitations of my application:

One reason this works is because there aren’t a lot of base nodes. However, in a game like go or chess with a lot of possible combination (moves) it would be impossible computationally to create this tree. Furthermore, in games such as poker which is an imperfect information game a different aproach must be taken to consider the unknown
Rotation:
To avoid having a huge tree I considered rotation. What does that mean? When playing noughts and crosses on the first move you have 9 different possible position (squares) you can play. When writing these out it is evident that they are extremely similar, and some are the same board position just rotated. This can be utilized since now instead of having 9 starting nodes and paths to follow there are only 3. This greatly reduces the size of the tree. Here is an example:
 				 
Further increase in efficiency

Another thing I did to increase efficiency, is I made the creation of the hash map and the escalation of the base node values happen at the same time. This avoids me having to go through the tree again just to escalate the values assigned to the nodes. 

Ve.1 and Ve.2

I had originally made this 2-3 weeks ago. However, when I ran it took too long. I know believe, it was reasonably fast (ish) and would have worked, but I forgot a simple if statement which drastically increased time. So, I then decided to redo everything using hash maps and making everything more efficient since I thought this high run time was because the gods of programming were punishing me for using linked lists. 

The tree:

The thing I frequently talk about above as “the tree” resembles a tree but it’s not really.
It takes a format as follows. One big hash map where each key is a board/position and each value of this, is a list with the first item being the node attributed to the position and the second another hash map of the possible iterations of the position:
