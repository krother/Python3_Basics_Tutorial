
# Grundbegriffe

## Modellparameter

Die Parameter, die ein Modell beim Lernen automatisch einstellt.

## Hyperparameter

Die Parameter, die Du selbst auswählen musst.

## Overfitting

Overfitting bedeutet, dass das Modell die Daten zu detailliert beschreibt (d.h. es lernt die Daten auswendig). Ein Overfitting lässt sich daran erkennen, dass für unabhängige *Testdaten* die Vorhersage schlechter ist als für die Trainingsdaten. Overfitting lässt sich vermeiden, indem man **die Komplexität des Modells reduziert** oder **die Datenmenge erhöht**.

## Underfitting

Underfitting bedeutet, dass das Modell nicht alle Informationen in den Daten verwendet. Es vereinfacht zu stark. Du erkennst Underfitting daran, dass die *Trainingsdaten* nicht gut vorhergesagt werden. Underfitting kann vermieden werden, indem man **die Komplexität des Modells vergrößert**.

## Trainings- und Testdatensätze
Ein Standardansatz ist die Unterteilung der Daten in Trainings- und Testdaten (in der Regel 80% zum Trainieren). Die Testdaten werden nicht für den Aufbau des Modells verwendet, so dass Sie anschließend mit unabhängigen Daten analysieren können, wie gut das Modell wirklich ist.

**Die Testdaten sind erst ganz am Ende und einmalig zu verwenden, damit keine Rückkopplung auf das Modell stattfindet!**

## Testen mehrerer Modelle oder Hyperparameter
Wenn Du mehr als ein Modell evaluierst, ist es unbedingt zu empfehlen, zusätzliche **Validierungsdaten** zu verwenden, um eine Rückkopplung der Testdaten auf das Modell zu vermeiden.

## Kreuzvalidierung

Bei der N-fachen Kreuzvalidierung wird der Datensatz in N Untermengen gleicher Größe aufgeteilt. Bei jedem weiteren Lauf wird eine dieser Portionen als Testdaten verwendet, die restlichen als Trainingsdaten.
So können Sie die Robustheit Ihrer Daten überprüfen.

Es gibt mehrere Varianten dieser Idee (z.B. *Shuffle Split* und *Bootstrapping*).

## Bias

Eine systematische Abweichung (Verzerrung), die das Modell vornimmt.

## Gleichgewicht zwischen Bias und Varianz

In vielen Modellen stehst Du vor der Wahl, die **Varianz** Ihrer Vorhersagen zu senken, aber dafür ein höheres **Bias** in Kauf zu nehmen. Oder umgekehrt. Die Aufgabe eines Data Scientist ist, das für eine konkrete Anwendung optimale Gleichgewicht zu finden.

## Fluch der Dimensionalität

Der **Kurs der Dimensionalität** bezieht sich auf eine Eigenschaft hochdimensionaler Vektoren. Je mehr Dimensionen die Daten haben, desto spärlicher ist der mehrdimensionale Raum belegt. Geometrisch gesehen sind in einem hochdimensionalen Datensatz alle Punkte gleich weit voneinander entfernt.

Siehe [From Regression to Sparsity](http://scikit-learn.org/stable/tutorial/statistical_inference/supervised_learning.html#linear-model-from-regression-to-sparsity)
