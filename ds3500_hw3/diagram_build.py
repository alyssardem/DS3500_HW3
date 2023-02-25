"""
Core framework class for NLP Comparative Analysis
J. Rachlin
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
        file_obj = open(filename)
        file_data = file_obj.read()
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
        num_words = self.data['numwords']
        for label, nw in num_words.items():
            plt.bar(label, nw)
        plt.show()

    def sankey(self):
        """ generates a sankey diagram by turning wordcount dict into a df and running the df through sankey.py """
        #     sk.make_sankey(stacked, "src", "targ", "vals")
        # df = pd.DataFrame.from_dict(self.data['wordcount'])
        # print(df)
        # print(list(df.columns))
        # print(df.index.values.tolist())
        # sk.make_sankey(df, list(df.columns), df.index.values.tolist())
        df = pd.DataFrame(columns=["articles", "words", "count"])
        for key, val in self.data['wordcount'].items():
            for k, v in val.items():
                # df2 = {'Name': 'Amy', 'Maths': 89, 'Science': 93}
                # df = df.append(df2, ignore_index=True)
                row = {'articles': key, 'words': k, 'count': v}
                df = df.append(row, ignore_index=True)
        sk.make_sankey(df, 'articles', 'words', 'count')


    def ind_chart(self):
        """ a for loop that returns a chart for every article """

    def group_chart(self):
        """ same kind of chart as ind_chart but combines all the articles into one chart """

