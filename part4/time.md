
# time and datetime

The `time` module offers functions for getting the current time and date.

    import time
    s = time.asctime()
    i = time.time()

The `datetime` module helps you to represent dates and format them nicely:

    date = datetime.date(2015, 12, 24)
    date.strftime("%d.%m.%Y")
        
Dates can be converted to integer numbers:

    date = datetime.date(2015, 12, 24)
    number = date.toordinal()

and back

    datetime.date.fromordinal(7)
    
## Exercises

### Exercise 1

Print today's date and time of day in a custom format.

