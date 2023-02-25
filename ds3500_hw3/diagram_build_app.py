
from diagram_build import Build
#import textastic_parsers as tp
import pprint as pp


def main():

    # initialize framework
    tt = Build()

    # register some text files
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/bbc1', 'UK1')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/bbc2', 'UK2')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/moscow_times1', 'RUS1')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/moscow_times2', 'RUS2') #, parser=tp.json_parser)
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/global_times1', 'CH1')
    tt.load_text('C:/Users/ardem/classes/ds3500_hw3/global_times2', 'CH2')

    # produce some visualizations
    pp.pprint(tt.data)
    tt.compare_num_words()





if __name__ == '__main__':
    main()