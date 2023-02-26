"""
framework for reading the txt files, adapting them, and running visualization programs
Melissa and Alyssa
"""

from collections import Counter, defaultdict
import random as rnd
import matplotlib.pyplot as plt
import sankey as sk
import pandas as pd


class Build:

    def __init__(self):
        # manage data about the different texts that
        # we register with the framework
        self.data = defaultdict(dict)

    @staticmethod
    def _default_parser(filename):
        """ creates a dict containing wordcount of every word in every article
        and overall numwords for every article
        filename - inputted files """
        file_obj = open(filename)
        file_data = file_obj.read()
        # create results cased on splitting and counting file_data and the length of the file_data
        results = {
            'wordcount': dict(Counter(file_data.split())),
            'numwords': len(file_data)
        }
        file_obj.close()
        return results

    def _save_results(self, label, results):
        """ Integrate parsing results into internal state
        label: unique label for a text file that we parsed
        results: the data extracted from the file as a dictionary attribute-->raw data
        """
        for k, v in results.items():
            self.data[k][label] = v

    def load_text(self, filename, label=None, parser=None):
        """ Register a document with the framework """
        if parser is None:  # do default parsing of standard .txt file
            results = Build._default_parser(filename)
        else:
            results = parser(filename)

        if label is None:
            label = filename

        # Save / integrate the data we extracted from the file
        # into the internal state of the framework

        self._save_results(label, results)

    def compare_num_words(self):
        """ creates a bar chart where each bar is an article
        and the height is that article's word count """
        num_words = self.data['numwords']
        for label, nw in num_words.items():
            plt.bar(label, nw)
        plt.show()

    def sankey(self):
        """ generates a sankey diagram by turning wordcount dict into a df
        and running the df through sankey.py """
        # creating an empty DataFrame containing columns for left, right, and width
        df = pd.DataFrame(columns=["articles", "words", "count"])

        # iterating through article, then wordcount
        for key, val in self.data['wordcount'].items():
            for k, v in val.items():
                # appending to df each wordcount and its value
                df.loc[len(df.index)] = [key, k, v]
        # removing any count in df that is less than 6
        df.drop(df.loc[df['count'] < 6].index, inplace=True)
        # removing any words in df with lengths less than 3
        df.drop(df.loc[df['words'].str.len() < 3].index, inplace=True)

        # generate sankey diagram
        sk.show_sankey(df, 'articles', 'words', 'count')

    def ind_chart(self):
        """ a for loop that returns a chart for every article """

    def group_chart(self):
        """ same kind of chart as ind_chart but combines all the articles into one chart """

