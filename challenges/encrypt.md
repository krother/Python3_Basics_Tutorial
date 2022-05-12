
# Encryption

**🎯 Implement a simple block encryption algorithm.**

## Step 1: Message in plain text

Save the message to be encrypted as a string:

    :::python
    s = "TOP_SECRET_MESSAGE"

## Step 2: Format as a Table

Break the string into several lines of equal length.
Fill in blanks at the end:

    :::text
    TOP_S
    ECRET
    _MESS
    AGE__

## Step 3: Encryption Key

Use a key to sort the columns in a new order. With the key `21403` you get:

    :::text
    POST_
    RCTEE
    EMS_S
    EG_A_

## Step 4: Merge Columns

Merge the columns one after the other to a new string. This is the final encrypted message:

    :::text
    POST_RCTEEEMS_SEG_A_

## Extra Challenges:

* Get text that someone else coded.
* Decrypt the message with the key.
* Crack the code without the key!


*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
