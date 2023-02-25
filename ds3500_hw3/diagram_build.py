"""
Core framework class for NLP Comparative Analysis
J. Rachlin
"""

from collections import Counter, defaultdict
import random as rnd
import matplotlib.pyplot as plt


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
            'wordcount': Counter(file_data.split()),
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



