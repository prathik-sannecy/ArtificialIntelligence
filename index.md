# AI and Gothello
PSU CS 441/541 Final Project  
Due by *5:00PM* Tuesday, 10 December  
*Not accepted* late

The Official Final Project for this course is to take an AI
look at a board game of my invention, Gothello. Gothello is
a small-board game that combines aspects of
[Othello](https://en.wikipedia.org/wiki/Reversi) (also known
as Reversi) and
[Go](https://en.wikipedia.org/wiki/Go_%28game%29).
Gothello is designed to be reasonably easy to explore, yet
give some insight into more complicated games. (Building a
Go player is definitely not in scope for an introductory AI
course.)

The following resources are provided:

* Gothello [informal rules](game/gothello.md)

* Official Gothello
  [Game Server](http://github.com/pdx-cs-ai/gothello-gthd)

* Formal [Specification](spec/gothello-server.pdf) of the
  server, including a formal specification of the game
  rules.

* Gothello game server
  [Java client](http://github.com/pdx-cs-ai/gothello-libclient-java)
  library.

* Gothello game server
  [C/C++ client](http://github.com/pdx-cs-ai/gothello-libclient-c)
  library.

* [Grossthello](http://github.com/pdx-cs-ai/gothello-grossthello),
  a really simple Gothello player.

## Challenges

Here are a couple of things you might try:

* Implement a minimax Gothello player.  The required
  standard of quality for grading purposes is that you
  implement depth-limited minimax search. You can use number
  of pieces on each side as a heuristic. Your player must
  interface with the Official Game Server so that you can
  test it against other human players and programs in a
  refereed environment.

* Build a better evaluation function. Counting pieces on
  each side is not a great heuristic. You can do a fancy
  procedural evaluator, or you can build a machine learner.

  For those who want to learn an evaluator, I will make an
  evaluation dataset available as soon as possible. Better
  yet would be to construct your own dataset using
  Grossthello or some other player.

  It is acceptable to use machine learning libraries or
  tools. For runs that require remote resources, a graphics
  card, a week to complete, etc. I will be counting on you
  to accurately report what you did; it is unlikely that we
  will be able to reproduce it in these cases.
  
The project may be done individually or in two-person
teams. I will expect substantially more impressive results
for a team. A reasonable plan for a two-person team would be
to have one member build a minimax player and the other
build a solid evaluator for the player. Another good plan
would be to build a minimax player with one or more
additional features: iterative deepening for time control,
selective search, alpha-beta pruning, a transposition table,
etc.

If you have some non-Gothello project idea you are *really
passionate* about, please talk to me. I'd prefer that the
majority of the class work in this space, but I understand
that AI is big and exciting.

## Submission

What to turn in:

1.  A reasonable writeup describing your work.

    * What did you try to do?
    * How well did it work?
    * How did you evaluate your work?
    * What did you learn?
    * What would you like to try in the future?
    * How do I reproduce your work (compile, run test)?

2.  Your work products — code, data, test runs, etc.  Your
    code should be readable, well-engineered, modular, and
    maintainable. Make sure it is commented, well-formatted
    and clear, as at least parts of it *will* be read.

    All programs must be executable in the CS Linux
    environment. The programs may be written in any
    reasonable language. I have provided glue code and
    specifications for a library which programs can use to
    play on a server: I have also put the referee itself
    online.

How to turn it in: submit your work products (source code,
writeup, etc.) to the Moodle as a single ZIP archive. Please
do not include binaries or other executable code, your Git
repo, or other large files that can be generated on our end.
