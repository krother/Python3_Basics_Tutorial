
# Learning Goals: Data Analytics with pandas

After teaching pandas for quite some time, I wrote down a detailed list of teaching goals.
Feel free to use it to develop your own courses, syllabi and materials.

Although the goals were written specifically for the pandas/Python stack, most of the concepts are general and could be easily adapted.

## Datasets

There are a few public datasets that can be used for classroom projects:

* [US Babynames dataset](http://www.ssa.gov/oact/babynames/limits.html)
* [Global demographics from gapminder.org](https://www.gapminder.org/data/)
* [Daily temperature data from ecad.eu](https://www.ecad.eu/)
* [Classical paintings from 50 artists on Kaggle](https://www.kaggle.com/code/paultimothymooney/collections-of-paintings-from-50-artists/notebook) – analyze the colors used by different artists (an advanced project)


## The Python data analytics ecosystem

* describe core Python libraries for data analytics (pandas, numpy, matplotlib, seaborn)
* enumerate a few alternatives (plotly/dash, R, Matlab, Tableau, QlikSense)
* install a Jupyter based environment (preferably Anaconda)
* apply 7+ different keyboard shortcuts to edit cells
* edit and format Markdown cell in Jupyter
* add an image to a Markdown cell
* edit a math equation in a Jupyter cell

## pandas fundamentals

* define the parts of a DataFrame (index, columns, Series)
* distinguish DataFrames and Series
* describe the underlying data structure (numpy arrays for columns)
* describe common data formats and their usage
* read data from tabular formats (CSV, Excel, SQL and plain JSON)
* write data to tabular formats (CSV, Excel, SQL and plain JSON)
* create Series from Python lists
* create a DataFrame from Python nested lists and dictionaries
* create a numpy array and convert it into a DataFrame
* access the numpy values of a Series or DataFrame


## Debugging pandas

* inspect the shape of DataFrames
* inspect the data type of columns
* inspect the row/column index of a DataFrame
* inspect the datatype of row/column indices
* check a DataFrame for missing values
* inspect data errors in the original data by opening CSV files in a text editor
* debug order of execution bugs in Jupyter
* debug integer overflow bugs (255 + 1 with `uint8`)
* debug forgot header bugs when reading CSV
* debug index_col=0 bugs when reading CSV
* debug wrong separator bugs in CSV
* debug column-shift bugs in CSV
* debug incomplete column bugs in CSV
* debug mismatching null values (`None`, `none`, `'-'`, `NaN`, `-999.999` etc.)
* distinguish reference vs copy and describe why this is a super messy part of pandas
* fix reference vs. copy issues by `df.copy()`
* inspect file size before loading a file
* check memory usage of a dataframe
* explain floating-point precision issues

## Selecting Rows and Columns

* display the first / last rows
* select single rows and columns by index
* select single rows and columns by name
* select multiple rows and columns by index
* select multiple rows and columns by name
* select rows by boolean expressions
* select rows by Regex matchin a string column 
* select rows by timestamp ranges
* sort data by rows and columns


## Data Quality

* define tidy data (read the [Tidy Data paper by Hadley Wickham](https://vita.had.co.nz/papers/tidy-data.pdf))
* identify what data format is needed to answer a particular question
* identify what data format is needed to create a particular visualization
* check a column for missing values
* define what data type a column with NaN has
* inspect unique values in a categorical column
* unify similar values (e.g. 'cat', 'Cat', 'felis catus', 'kitty')
* impute missing categories by the most common value
* impute missing values by replacing a median (and explain why it is better than the mean)
* impute missing values by a group median
* create a binary column indicating that data was missing

## Edit columns

* add a new column to a DataFrame
* remove a column to a DataFrame
* convert data types of a column
* explain why adding rows is not on this list
* explain the inplace=True operation
* move a column into the index
* move the index into a column
* replace a column by a Python list
* create a new column by applying a custom Python function
* convert a count column to a percentage
* scale data to 0.0..1.0 or standard normal
* apply arithmetics on a column (e.g. to change m to mm)
* apply a log-transform on a column
* revert a log-transform by exp()
* decide whether a column should be log-transformed
* rename columns
* convert string columns to binary values

## Data Wrangling

* explain long and wide data formats
* convert long into wide format and vice versa
* explain what a MultiIndex is
* merge multiple DataFrames horizontally
* concatenate multiple DataFrames vertically
* describe potential pitfalls when joining DataFrames
* distinguish inner, outer and left/right joins
* create a boolean column comparing two columns
* explain why iterrows is not a great idea most of the time


## Aggregation

* sum over rows, columns and entire DataFrames
* calculate group means, sums and counts for a category
* calculate group means, sums and counts for multiple categories
* explain why you have to select a column that you are not interested in when using count
* enumerate aggregation functions (above plus sdev, min, max, median)
* implement simple aggregation functions from scratch
* explain why one should not group by scalars
* bin values by quantiles or equidistant bins
* distinguish aggregate and transform operations
* crosstabulate data by counts or sums
* apply custom functions in aggregation and transformation


## Time series data

* create timestamps from scratch using ranges and frequencies
* explain how timestamp integers work
* debug timestamp bugs resulting from timestamp integers being off scale
* import missing values in a time series by ffill, bfill or interpolation
* extract hour, day, minute, weekday etc. from a timestamp column
* calculate the diff of a time series
* revert the diff of a time series
* create a lag column
* resample a DataFrame with a timestamp index (upsample and downsample)
* apply a window function over time series data (rolling mean etc.)


## Anonymization and Ethics

* give examples why personal data needs to be protected
* use the faker library to replace personal data by dummy data 
* apply column functions to anonymize data
* discuss when anonymized data is really anonymous
* describe the main GDPR guidelines


## Descriptive Statistics

* calculate measures of centrality (mean, median)
* explain their differences, pros and cons
* calculate measures of spread (range, standard deviation, quartiles, percentiles)
* identify outliers
* check for normal distribution with a Q-Q-plot
* check the distribution of a column with a statistical test
* calculate correlation coefficients between columns and explain their meaning
* enumerate common distributions (uniform, normal, binomial, power law, poisson)
* explain the Central Limit Theorem
* explain stratification


## Data Visualization

* display and interpret histograms
* create bar plots, scatter plots, line plots but not pie charts
* label and annotate plots accordingly (see [scipy-lectures.org](https://scipy-lectures.org/intro/matplotlib/index.html))
* create plots from DataFrames with MultiIndexes
* apply common one-liners to aggregate and plot data
* create a heatmap from a crosstab
* distinguish good plots from misleading, ugly and wrong plots (see O'Reilly Datavis book)
* check plots for accessibility by persons with color impairment
* explain why it is not a good idea to invent your own color scheme
* distinguish bitmap and vector formats
* identify loss-free and loss in compressed image formats
* convert dpi and figure size to pixels and vice versa
* explain advantages and disadvantages of common image formats (png, jpg, gif, webp, tif)


## Engineering

* add the `.ipynb-checkpoints` directory to `.gitignore`
* inspect a Jupyter notebook on GitHub
* inspect a git diff on a Jupyter notebook
* deploy a notebook to a Jupyter server in the cloud (e.g. colab, pythonanywhere)
* describe why it is difficult to collaborate on a Jupyter notebook
* discuss options to collaboratively work on a notebook anyway
* discuss useful sizes of cells and entire notebooks
* export a Jupyter notebook to a standalone Python script
* clean up an exported Python script
* place key functions into an importable module to make a notebook smaller
* explain why running the import again does not help when you edited the module


## Advanced Topics

* Segmentation with K-Means
* Outlier Detection with GMMs or DBSCAN
* Dimensionality reduction for plotting with T-SNE
* plotting maps
* use streamlit for interactive visualization


## License

(c) 2022 Dr. Kristian Rother

Distributed under the conditions of the Creative Commons Attribution License 4.0. See [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/) for details.