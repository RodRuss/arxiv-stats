#!/usr/bin/pythona

from arxiv_search import *
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rc('font', size=15)

if __name__ == '__main__':

    query1 = 'ti:bitcoin+OR+abs:bitcoin'
    query2 = 'ti:blockchain+OR+abs:blockchain'
    results1 = search_query(query1, max_results=500)
    results2 = search_query(query2, max_results=500)

    print(get_number_of_results(results1))
    print(get_number_of_results(results2))

    fig, axes = plt.subplots(1, 2)
    plot_histogram(results1, axes[0])
    plot_histogram(results2, axes[1])
    for ax in axes:
        ax.set_ylim(0, 350)
    plt.show()
   

