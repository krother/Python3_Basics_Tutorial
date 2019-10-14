
# Graphen abschreiten

**🎯 Finde den Weg aus dem Labyrinth.**

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

Schreibe eine Funktion, die das Labyrinth (den Graphen) abschreitet, bis der Ausgang (`X`) erreicht ist.

## Hinweise

Du kannst ähnlich wie bei der *Baumsuche* vorgehen:

* erstelle eine Liste der zu besuchenden Knoten
* erstelle eine Liste mit bereits besuchten Knoten
* besuche einen Knoten und füge seine Nachbarn der Liste zu besuchender Knoten hinzu
* experimentiere, was sich an der Reihenfolge der Ausgabe ändert, wenn Du die Liste als Stack oder als Queue implementierst
