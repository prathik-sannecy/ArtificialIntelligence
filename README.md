# Gothello Project Documentation
Bart massey

This is general documentation on the Gothello Project.  You
can visit http://pdx-cs-ai.github.io/gothello-project (or
the [index.md](index.md) here) for information on the
assignment for my AI course.

Gothello is
a small-board game that combines aspects of
[Othello](https://en.wikipedia.org/wiki/Reversi) (also known
as Reversi) and
[Go](https://en.wikipedia.org/wiki/Go_%28game%29).
Gothello is designed to be reasonably easy to explore, yet
give some insight into more complicated games.

## What's Here

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

## How To Try It Out

Check out the source repos for Gthd and Grossthello
and follow the instructions there to build the server and
client. 

Now open three terminals. On the first terminal go to the
Gthd directory and type `java Gthd 0`. On the second and
third terminals go to the Grossthello directory. On the
second terminal, type

        java Grossthello white localhost 0 3

On the third terminal, type the same thing except `white`
instead of `black`. You should then see a badly-played game
of Gothello running.

See the source and docs in the various repos for further
information.
