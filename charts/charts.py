import matplotlib.pyplot as plt
def generate_pie_chart():
    """
    Generates a pie chart using the matplotlib library in Python.

    Example Usage:
    generate_pie_chart()

    Inputs:
    None

    Outputs:
    None

    Code Analysis:
    - Initializes two lists: `labels` and `values`, which represent the labels and corresponding values for the pie chart.
    - Creates a figure and an axis object using the `plt.subplots()` function.
    - Calls the `ax.pie()` method with the `values` and `labels` as arguments to generate the pie chart.
    - Uses the `plt.savefig()` function to save the generated chart as an image file named 'pie.png'.
    - Calls the `plt.close()` function to close the figure and free up system resources.
    """
    labels = ['A','B','C']
    values = [10,30,60]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()