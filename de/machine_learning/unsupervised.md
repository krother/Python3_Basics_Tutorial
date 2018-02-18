# Unüberwachtes Lernen

Beim **unüberwachten Lernen** gibt es keine Trainingsdaten. Die richtigen Antworten sind nicht im Voraus bekannt. Es geht meist darum die Daten zu *clustern*, *die Anzahl der Dimensionen zu reduzieren* oder *Ausreißer zu finden*.

## k-means Clustering 

Beim **k-means Clustering** werden die Daten in exakt *k* Cluster eingeteilt. Der Mittelpunkt jedes Clusters wird so gewählt, dass die Entfernung jedes Datenpunktes zum Clustermittelpunkt minimal wird.

Das k-means Clustering ist eine robuste Method, deren Hauptnachteil darin besteht, dass Sie den richtigen Wert für *k* selbst finden müssen.

## Hauptkomponentenzerlegung

![Entenzerlegung](images/entenzerlegung.jpg)

*..entenzerlegung*

Die **Hauptkomponentenzerlegung (PCA)** transformiert die Daten so, dass deren wichtigste Eigenschaft durch eine Koordinate ausgedrückt wird, die zweitwichtigste Eigenschaft durch eine weitere Koordinate usw. Diese Eigenschaften nennt man **Hauptkomponenten**.

**Beispiel:** Bei Schiffen lassen sich viele Eigenschaften wie Länge, Breite, Tiefgang Bruttoregistertonnen usw. durch eine Eigenschaft, die Größe ausdrücken. Die nächstwichtige Eigenschaft könnte sein, ob das Schiff eher bauchig oder länglich ist.

Die Hauptkomponentenzerlegung hat den Vorteil, dass sich die Hauptkomponenten schnell und automatisch berechnen lassen. Mit wenigen Hauptkomponenten läßt sich oft einfacher weiter arbeiten (z.B. mit einem überwachten Verfahren). 

Der Nachteil ist, dass sich die Hauptkomponenten meist nicht leicht interpretieren lassen (anders als im Beispiel mit den Schiffen).


## Weitere Verfahren

Andere beliebte unüberwachte Lernverfahren sind andere **Clusterverfahren**, **Gaussian Mixture Models** und **unsupervised Neural Networks**. Siehe [Models for unsupervised learning on the skikit-learn page](http://scikit-learn.org/stable/unsupervised_learning.html#unsupervised-learning)
