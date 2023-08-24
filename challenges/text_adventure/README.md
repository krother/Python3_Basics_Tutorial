
# Quest for the Dragon Egg

**🎯 Implement a text adventure.**

----

## The Story

![](images/dragon_egg.png)

Far, far away, in an hardly accessible landscape, the mystic dragon egg lies hidden..
Will you find the egg and awaken the life within?

* the dragon egg can be found on a lonely clearing
* to awaken the egg, you need a magic spell
* the spell is only known to a mage
* the mage lives in a tower behind the forest
* in the forest lives a bear that doesn't let anyone pass
* the bear, however, loves honey. Fortunately there is a beekeeper nearby.

OK, this is not the greatest plot ever written. If you have a better one, program it!

----

## Requirements

Write a game in which you can travel around between multiple rooms (clearing, tower, forest etc.).

* the world consists of at least four 'rooms'
* every room has a description
* you enter the room to which you want to go on the keyboard
* when you find the egg, the game ends with a final message

The game is entirely text-based.

----

## Example Output

    :::text
    Find the Dragon Egg
    ===================

    You are in your home town,
    a little trading spot on the desert border.

    There are paths leading to: desert, forest

    Where do you want to go? desert


    You are in the desert. The sun is burning.

    There are paths leading to: home, clearing, forest

    Where do you want to go? clearing


    On a hidden clearing you discover the dragon egg.

    Your quest has been successful!

----

## Step by Step

### Step 1: Create a project folder

* Create a new folder for this project
* Create a Python file `adventure.py`
* Open the file in an editor

----

### Step 2: The Basic Structure

Make the program produce a welcoming message.
You could use an output with multiple lines:

    :::python3
    print("""
    Find the Dragon Egg
    ===================

    Your quest starts.
    """)

At the end, the program congratulates the player to success:

    :::python3
    print("""
    On a hidden clearing you discover the dragon egg.

    Your quest has been successful!
    """)

During the project, you will insert more code between these two instructions.

**Execute the program and make sure it works.**

----

### Step 3: The Main Loop

The most important structural element of most games is the **main loop**.
In each round of the loop you can enter a command.
The game should end once you reach the final destination.

At the beginning it is unknown how many instructions the player will enter.
Therefore the number of loops is unknown.
In such situations a **conditional loop** with `while` is a good choice.

First you need to define a variable that contains the current location.
In Python you can use the name of the room as a string:

    :::python3
    room = "hometown"

As soon as you reach the room *"clearing"*, the game ends.
You can check that in the condition of the `while` loop:

    :::python3
    while room != "clearing":
        print(f"You are in {room}")
        room = input("Where would you like to go? ")

**Execute the program and make sure you can finish the game.**

----

### Step 4: Rooms

Your game does not have any rooms yet, so it is hard to tell where you are.

Write interesting descriptions of the rooms and print them
by adding `if` instructions like the following to the main loop:

    :::python3
    if room == "hometown":
        print("""
        You are in your home town.
        A small trading spot at the desert border.
        """)

You can replace the `print()` statement from the previous step with the `if` statement.

**Execute the program and make sure it works.**

----

### Step 5: Data Structure

Checking every room with a separate `if` statement is feasible if you have 4 rooms.
But imagine your game has 100 or more rooms – the program would become quite messy.

A better alternative is to **structure the room data**.
We will use a **dictionary** that contains descriptions of all rooms:

    :::python3
    descriptions = {
        "hometown": """You are in your home town...""",
        "desert": """...""",
    }

Define this dictionary at the beginning of the program.
Now you can replace all `if` statements by a single request to the dictionary.
The **key** is the `room` variable.

Add these commands to the `while` loop:

    :::python3
    print(descriptions[room])

and remove the `if` statements from step 4.

**Execute the program and make sure it works.**

----

### Step 6: Checks

At the moment the program is not checking whether a room you entered really exists.
If you enter a wrong room (or make a typo), the program stops with an error message.

Let's check the input to prevent that.

The following code matches the users input with the keys of the dictionary `descriptions`:

    :::python3
    target = input("Where do you want to go? ")
    if target in descriptions:
        room = target
    else:
        print("Stop! There is no such place.")

Find out where in the program these lines need to be inserted.

**Execute the program and make sure it works.**

----

### Step 7: Paths

Until now you could teleport from one room to any other.
That makes the game a bit boring.

* First, it is not clear which rooms you can go to.
* Second, you could enter "clearing", and the game ends right away.

The game would be a lot more interesting if only some rooms were connected.
For that, we need a second dictionary that contains the connections.
Each entry points from one starting room to one or more targets:

    :::python3
    paths = {
        "hometown": ["beekeeper", "forest"],
        "forest": ["hometown", "deser"],
        ...
    }

You need two entries to create paths in both directions.
If you leave one of them away, you also could create *one-way-streets*.

The paths for the current room could be displayed with the following line:

    :::python3
    print(paths[room])

or somewhat more nicely with:

    :::python3
    print(", ".join(paths[room]))

If you would like to extend the plausibility check, so that only the current paths are accessible, you need the following line:

    :::python3
    if target in paths[room]:
        ...

**Execute the program and make sure it works.**

----

### Step 8: Puzzles

An interesting adventure should also contain a few puzzles.
Here is how a puzzle could look like:

    :::text
    Where would you like to go? forest

    There is a BEAR in the forest!!! You run away.

    ...

    Where would you like to go? beekeeper

    You buy a pot of honey at the beekeeper.

    ...

    Where would you like to go? forest

    You leave the honeypot to the bear and carefully sneak through.

How to implement such a puzzle?

First you need a **state variable** that you define before the main loop, e.g.:

    :::python3
    honey = False

Second, you need to check in the main loop whether the state should change, and then change it, e.g.:

    :::python3
    if room == "beekeeper" and not honey:
        print("You buy a pot of honey at the beekeeper.")
        honey = True

Finally you need to check the state variable in the main loop to allow actions or prevent them:

    :::python3
    if target == "forest":
        if honey:
            print("You leave the honeypot to the bear and carefully sneak through.")
            honey = False  # you can use the honey only once
        else:
            print("There is a BEAR in the forest!!! You run away.")
            target = room   # player stays in the same place

----

### Final Remarks

It is not easy to place all statements in the right order.
A good idea is to run the program after each modification and to see what happens.

For sure you have many ideas what to include in your adventure.
