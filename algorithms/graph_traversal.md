
# Graph Traversal

**🎯 Find your way out of the labyrinth.**

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

Write a function that will walk the maze (the graph) until the exit (`X`) is reached.

## Hints

You can proceed in a similar way to *tree traversal*:

* create a list of the nodes to visit
* create a list of already visited nodes
* visit a node and add its neighbours to the list of nodes to visit
* experiment with what changes in the order of output when you implement the list as a stack or queue

*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
