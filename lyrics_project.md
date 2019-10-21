
# The Lyrics Project

![Eminem](eminem_word_cloud.jpg)

*frequent words in songs of Eminem*

## Goal

In this project we will **predict artists from song lyrics**.

Our program shall learn to name a possible artist for made-up sentences like:

* *"we will dance and have a good time"*
* *"I want you to know, yeah, that I still love you so"*
* *"the little bags of dope, there was a pile of coke"*

The project consists of five parts:

1. Download a list of links for one artist
2. Parse the song links
3. Download song lyrics
4. Parse song lyrics
5. Classification using the *Naive Bayes*-approach


## Links

[https://pudding.cool/2017/05/song-repetition/index.html](https://pudding.cool/2017/05/song-repetition/index.html)

# Part 1: Download a list of links

## Task 1.1

Visit the website [azlyrics.com](http://www.azlyrics.com). Pick your favourite artist (anyone else than **Madonna**, **Eminem** or **Beatles**, we already have those).

Copy the URL.

## Task 1.2

Create a Python script `download.py`.

## Task 1.3

Use the `requests` module to download the page with songs of that artist.

For this to work, we need to pretend that Python is a web browser. Use the lines:

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get(url, headers=headers)

## Task 1.4

Save the downloaded page in a HTML file.

#### Hint:

If the page contains special characters (you get some strange encoding error), open the file for writing with:

    f = open(filename, 'w', encoding='utf-8')

# Part 2: Parse the song links

## Task 2.1

Create a new Python file `parse_song_links.py`.

## Task 2.2

Read the HTML file downloaded in Task 1.4 as a single string.

## Task 2.3

Examine the HTML file in a text editor. Find out, where the song links are in the file and how the program might recognize these.

## Task 2.4

Write a program that collects all links to songs from the HTML document in a list, e.g.:
    [
     'madonna/frozen.html',
     'madonna/burningup.html',
     ..
    ]

Possible approaches:

* `string.find`
* `string.split`
* Position in the string and slicing (if the position is always the same)
* Regular Expressions (via [regexone.com/](https://regexone.com/) and [regex101.com/](https://regex101.com/))

#### Hinweis:

If the file contains special characters, you need to read it with:

    f = open(dateiname, 'r', encoding='utf-8')

## Task 2.5

Write all links to the screen and check whether the program is working correctly.


# Part 3: Download song lyrics

## Task 3.1

Create a directory in which you will write lyrics for individual songs.

## Task 3.2

Remove all spaces and special characters from the song title to obtain a filename.

Add the suffix `.html` to the filename.

## Task 3.3

Take **the first song from your list** and create the full URL to the lyrics.


## Task 3.4

Download the lyrics of a *single* song and write it to a text file.

Again, use the `headers` parameter as above.

## Task 3.6

Use the `time` module to wait 90 seconds after downloading a single song:

    import time
    time.sleep(90)

**THIS IS THE MOST IMPORTANT STEP. IF YOU OMIT THIS, IT MAY HAPPEN THAT THE SERVER BLOCKS THE ENTIRE CLASS. IF IN DOUBT, ASK.**

## Task 3.7

Download the first 20 songs.

## Task 3.8

Check before downloading if a file already exists:

    import os
    if os.path.exists()

Only download files that do not exist yet.

# Part 4: Parse song lyrics

*You can work on these tasks whily your program is still busy downloading files.*

## Task 4.1

Create a new Python script `songs_einlesen.py`

## Task 4.2

Output the names of all lyrics using the `os` module:

    import os
    for filename in os.listdir(PATH):
        print(filename)

## Task 4.3

Inspect one of the lyrics HTML documents in a tet editor. Find out where the lyrics begin and end.

## Task 4.4

Read a song file into a single string. Use the `read()` function:

    text = open(filename).read()

Cut the songtext from the HTML code. The `text.find()` method is quite helpful here.

## Task 4.6

Read all songs into a list of strings

# Part 5: Prediction

Now we will apply a standard recipe (see [http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html](http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html)).

## Task 5.1

Create a new Python script `prediction.py`.

Use or import the previously written code to read lyrics.

## Task 5.2

Prepare the data for prediction by collecting the song lyrics in `X`, and the names of the artists in `y`:

    X = madonna + eminem
    y = ['madonna'] * len(madonna) + ['eminem'] * len(eminem)

Make sure that X and y have the same length.

## Task 5.3

Import a few things from `scikit-learn`:

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.pipeline import Pipeline
    from sklearn import model_selection

## Task 5.4

Split the dataset into training and test data. Use 0.2 for `TEST_RATIO`:

Xtrain, Xtest, ytrain, ytest = \
    model_selection.train_test_split(X, y, test_size=TEST_RATIO)

## Task 5.5

Build the model:

    model = Pipeline([
        ('vectorizer', CountVectorizer(min_df=3, ngram_range=(1, 1))),
        ('tfidf_transformer', TfidfTransformer()),
        ('bayes_model', MultinomialNB(alpha=1.0)),
    ])
    model.fit(Xtrain, ytrain)

## Task 5.6

Inspect the number of vectorized words:

    vect = model.named_steps['vectorizer']
    print(len(vect.vocabulary_))

## Task 5.7

Evaluate the model:

    print("Accuracy test set: ", model.score(Xtest, ytest))

Compare the model for training and test data. How do you interpret the outcome?

## Task 5.8

Tweak the parameter `alpha`. How does the prediction change?

## Task 5.9

Perform a 10-fold cross-validation:

    print(model_selection.cross_val_score(model, X, y,
    cv=10, scoring='accuracy'))


## Task 5.10

Perform a prediction on new data:

    model.predict("take the 8mile road in detroit")

## Task 5.11

Extract distinctive words for both artists:

    import numpy as np
    names = np.array(model.named_steps['vectorizer'].get_feature_names())

    coef = model.named_steps['bayes_model'].coef_
    coef = coef.reshape((len(names),))

    # Top 20 words for 1st artist
    indices = (-coef).argsort()[:20].tolist()
    print(names[indices])

    # Top 20 words for 2nd artist
    indices = (coef).argsort()[:20].tolist()
    print(names[indices])

## Task 5.12

Try different hyperparameters:

* vary the amount of test data
* vary `min_df` in `CountVectorizer`
* use the option `stop_words='english'` in the  `CountVectorizer`
* vary `ngram_range` in `CountVectorizer`
