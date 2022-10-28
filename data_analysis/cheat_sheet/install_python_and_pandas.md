
# How to Install Python and pandas?

On this page, I describe a beginner-friendly Python/pandas setup.

---

## 1. Install Anaconda

**Anaconda** is a one-stop installation that contains all Python packages for this course and an editing environment.

- go to [https://www.anaconda.com/](https://www.anaconda.com/) to download Anaconda for your system (the free version)
- follow the instructions

## 2. Start Jupyter

- from the **Anaconda Navigator**, start the Jupyter Notebook.
- Jupyter will run as a HTTP server in the background
- From the overview page, create a new Python3 notebook with the button **New** (top-right)

## 3. Write Python Code

Type the code:

    :::python3
    from seaborn import sns

    df = sns.load_dataset('penguins')
    df

Execute the code with the **‘play’** button on top or press **Shift-Enter**.

A few keyboard shortcuts that speed up your work in Jupyter:

- Shift + Enter : execute a cell
- Escape + A or Escape + B : insert a cell
- TAB : autocompletion (great for long functions and file names)
- Shift + TAB : context sensitive help

