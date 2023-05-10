
Maze
====

Find a way out of the maze.

.. code:: python3

   maze = """
   ############
   #     # ##S#
   ### #      #
   ### ###### #
   ###   # ## #
   # ## ## ## #
   #    #     #
   #X##########""".strip().split('\n')
   
   x, y = (10, 1)
   target = (1, 7)
