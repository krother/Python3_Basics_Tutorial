
# matplotlib

## What is matplotlib?

`matplotlib` is a Python module for creating diagrams.


## Exercises

### Exercise 1

Run the code to create a line plot:

    from pylab import figure, plot, savefig

    xdata = [1, 2, 3, 4]
    ydata = [1.25, 2.5, 5.0, 10.0]
    
    figure()
    plot(xdata, ydata, "r-")
    savefig('simple_plot.png')

### Exercise 2

Run the code to create a pie chart:

    from pylab import figure, title, pie, savefig

    names = ['Emily', 'Hannah', 'Madison', 'Ashley', 'Sarah']
    count = [25952,23073, 19967, 17995, 17687]
    explode = [0.0, 0.0, 0.0, 0.05, 0.05]

    colors = ["#f0f0f0", "#dddddd", "#bbbbbb", "#999999", "#444444"]

    def get_percent(value):
        '''Formats float values in pie slices to percent.'''
        return "%4.1f%%" % (value)

    figure(1)
    title('frequency of top 5 girls names in 2000')
    pie(count, explode=explode, labels=names, shadow=True,
        colors=colors, autopct=get_percent)
    savefig('piechart.png', dpi=150)

### Exercise 3

Run the code to create a bar plot:

    from pylab import figure, title, xlabel, ylabel, xticks, bar, \
                      legend, axis, savefig

    nucleotides = ["A", "G", "C", "U"]

    counts = [
        [606, 1024, 759, 398],
        [762, 912, 639, 591], 
        ]

    figure()
    title('RNA nucleotides in the ribosome')
    xlabel('RNA')
    ylabel('base count')

    x1 = [2.0, 4.0, 6.0, 8.0]
    x2 = [x - 0.5 for x in x1]

    xticks(x1, nucleotides)

    bar(x1, counts[1], width=0.5, color="#cccccc", label="E.coli 23S")
    bar(x2, counts[0], width=0.5, color="#808080", label="T.thermophilus 23S")

    legend()
    axis([1.0, 9.0, 0, 1200])
    savefig('barplot.png')

### Exercise 4

Write a program creating a line plot for the frequency of one name over several years.

## Where to learn more?

You can find example diagrams and code in the matplotlib gallery on [matplotlib.org/gallery.html](http://matplotlib.org/gallery.html).