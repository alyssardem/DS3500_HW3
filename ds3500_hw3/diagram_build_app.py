"""
importing downloaded files and running visualizations
Melissa and Alyssa
"""

from diagram_build import Build
import pprint as pp
import sankey as sk


def main():

    # initialize framework
    tt = Build()

    # register the text files
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/bbc1', 'UK1')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/bbc2', 'UK2')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/moscow_times1', 'RUS1')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/moscow_times2', 'RUS2')  # , parser=tp.json_parser)
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/global_times1', 'CH1')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/global_times2', 'CH2')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/npr1', 'US1')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/npr2', 'US2')

    # produce the visualizations
    tt.sankey()
    tt.group_chart()
    tt.ind_chart()


if __name__ == '__main__':
    main()