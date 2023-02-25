
from diagram_build import Build
#import textastic_parsers as tp
import pprint as pp


def main():

    # initialize framework
    tt = Build()

    # register some text files
    tt.load_text('bbc1.txt', 'UK1')
    tt.load_text('bbc2.txt', 'UK2')
    tt.load_text('moscow_times1.txt', 'RUS1')
    tt.load_text('moscow_times2.txt', 'RUS2') #, parser=tp.json_parser)
    tt.load_text('global_times1.txt', 'CH1')
    tt.load_text('global_times2.txt', 'CH2')

    # produce some visualizations
    pp.pprint(tt.data)
    tt.compare_num_words()





if __name__ == '__main__':
    main()