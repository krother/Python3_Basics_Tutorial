
# Das Problem des Handlungsreisenden

**🎯 Implementiere eine Lösung für das Traveling Salesman Problem**

Ein Handlungsreisender möchte N Städte besuchen und dabei eine möglichst kurze Strecke zurücklegt.

Schreibe ein Programm, das die Städte mit folgenden Koordinaten *besucht*:

    import random

    N = 10
    random.seed(42)
    x = [random.randint(1, 100) for i in range(N)]
    y = [random.randint(1, 100) for i in range(N)]

Eine Lösung könnte so aussehen:

    7 5 2 8 6 1 0 3 9 4

    gesamte zurückgelegte Strecke: 123.45


## Teilaufgaben

* Probiere eine *brute force*-Lösung aus, die alle Möglichkeiten ausprobiert. Warum ist diese Lösung nicht immer die beste?
* Werte die Laufzeit für unterschiedliche Werte von *N* aus.
* Schreibe eine *heuristische Lösung*
* Recherchiere das *Problem des Handlungsreisenden (Traveling Salesman Problem)*
* Recherchiere, was ein **NP-vollständiges Problem** ist
