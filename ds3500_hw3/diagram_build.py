"""
framework for reading the txt files, adapting them, and running visualization programs
Melissa and Alyssa
"""

from collections import Counter, defaultdict
import random as rnd
import matplotlib.pyplot as plt
import sankey as sk
import pandas as pd
import plotly.express as px


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

    def generate_df(self):
        df = pd.DataFrame(columns=["articles", "words", "count"])

        # iterating through article, then wordcount
        for key, val in self.data['wordcount'].items():
            for k, v in val.items():
                # appending to df each wordcount and its value
                df.loc[len(df.index)] = [key, k, v]
        # for art in df['articles'].unique():
        #     print(art)
        #     for ind in df.index:
        #         row = df.loc(ind)
        #         print(row['articles'])
        #         if row[0].to_string() == art:
        #             if df[1].str.contains(row[1]):
        #                 df.replace(to_replace=(df['words'].str.contains(row[1])), value=row)
        #print(df)
        return df

    def generate_df2(self, df):
        time = ['year', 'year,', 'Monday', 'April,', 'April.', 'August,', 'February.', "February.I've", 'January',
                'January,', 'January.', 'Feb.', 'January.This', 'March.', 'May.', 'Tuesday.A', 'Tuesday,', 'October.',
                'September.', 'Tuesday', 'week', 'winter', 'time.', 'time', 'summer', 'spring.', 'spring', 'afternoon']
        location = ['world.', 'Western', 'West', 'Washington', 'US', "Ukraine's", 'NATO,', 'Munich,', 'Munich', 'Hong,',
                    'Moscow,', 'Moscow', 'Heng,', 'Global', 'Germany,', 'European', 'China', 'East', 'Chinese',
                    'China-Russia', "China's", 'Bulgarian', 'Bilhorod-Dnistrovskyi', 'Demydiv,', 'Dnipro', 'Dnipro,',
                    'Eastern', 'Europe', 'Izium', 'Izium.', 'Kharkiv', 'Kharkiv,', 'Kherson', 'Korenovsky',
                    'Kuzhukhar,', 'Kyiv', 'Kyiv,', 'Kuleba', 'Li', 'Kiev', 'Kyiv.', 'Luhanska,', 'Lviv', 'Lviv,',
                    'Mariupol', 'Moldovan,', 'Moshchun', 'Moshchun,', 'Mykolaiv', 'Poland', 'Roman', 'Russia,"',
                    'Russia,', 'Russia', "Russia's", 'Russian', 'Russian,', 'Soviet', 'Stanytsia', 'Ukraine.Last',
                    'U.S.', 'Ukraine,', 'Ukraine', 'Ukraine.', 'western', 'Western', 'Victoria,', 'village',
                    'southwest', 'northernmost', 'frontlines', 'farmhouse', 'eastern', 'downtown', 'country,',
                    'country', 'Russia-Ukraine', '"Russia', '"Ukraine', 'America,', 'Asian', 'Beijing-based']
        person = ['himself', 'his', "Wang's", 'Wang,', 'Wang', 'Vladimir', "Putin's", 'Putin', 'Joe', 'Minister',
                  'Dmytro', 'Blinken', 'Beliakova,', 'Anna', 'Artemchuk', 'Claire', 'Harbage', 'Ivan', 'Katerina',
                  'Kostenko', 'Koverznev,', 'President', 'Pavlenko', 'Patrushev,', 'Maksim.', 'Mordiukova', 'Mykhailo',
                  'Nadia', 'Nikolai', 'Pastuchenko', 'Paul', 'Pavlo', 'People', 'Peter', 'Rebenko', 'Thompson.',
                  'Tsyhanenko,', 'he',  'Volodymyr', 'Viktor', 'Ukrainians,', 'Ukrainians', 'Ukrainian', 'Antony',
                  'Biden', "Biden's"]
        war = ['zone', 'peace."', 'peace', 'death', 'casualties', 'ceasefire,', 'battlefield,"', 'battlefield,',
               'battle', 'artillery', 'ammunitions', 'ammunition,', 'allies', 'besieged', 'Howitzers.', 'Aid', 'attack',
               'forces', 'wars', 'war.This', 'war-damaged', 'warring', 'war,', 'war', 'units', 'teams', 'team',
               'tactics.', 'soldiers', 'soldier', 'Sandbags', 'Shelling', 'Soldiers', 'shell-shocked', 'rubble',
               'military', 'lieutenant', 'liberation', 'liberated', 'journalist-turned-soldier', 'invasion.',
               'invasion', 'rocket', 'resilience.In', 'resilience', 'conflict,', 'conflict', 'body', 'bodies']

        df2_data = [['CH1', 0, 0, 0, 0, 0], ['CH2', 0, 0, 0, 0, 0], ['RUS1', 0, 0, 0, 0, 0], ['RUS2', 0, 0, 0, 0, 0],
                    ['UK1', 0, 0, 0, 0, 0], ['UK2', 0, 0, 0, 0, 0], ['US1', 0, 0, 0, 0, 0], ['US2', 0, 0, 0, 0, 0]]
        df2 = pd.DataFrame(df2_data, columns=['articles', 'time', 'location', 'person', 'war', 'misc'])
        for ind in df.index:
            if df['words'][ind] in time:
                for ind2 in df2.index:
                    if df2['articles'][ind2] == df['articles'][ind]:
                        df2['time'][ind2] += df['count']
            elif df['words'][ind] in location:
                for ind2 in df2.index:
                    if df2['articles'][ind2] == df['articles'][ind]:
                        df2['location'][ind2] += df['count']
            elif df['words'][ind] in person:
                for ind2 in df2.index:
                    if df2['articles'][ind2] == df['articles'][ind]:
                        df2['person'][ind2] += df['count']
            elif df['words'][ind] in war:
                for ind2 in df2.index:
                    if df2['articles'][ind2] == df['articles'][ind]:
                        df2['war'][ind2] += df['count']
            else:
                for ind2 in df2.index:
                    if df2['articles'][ind2] == df['articles'][ind]:
                        df2['misc'][ind2] += df['count']
        return df2

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
        df = Build.generate_df(self)
        # removing any count in df that is less than 6
        df.drop(df.loc[df['count'] < 6].index, inplace=True)
        # removing any words in df with lengths less than 3
        df.drop(df.loc[df['words'].str.len() < 3].index, inplace=True)

        # generate sankey diagram
        sk.show_sankey(df, 'articles', 'words', 'count')

    def ind_chart(self):
        """ a for loop that returns a chart for every article """
        for art in range(8):
            df = Build.generate_df(self)
            df2 = Build.generate_df2(self, df=df)
            df2 = df2.iloc[[art], :].copy()
            df2 = df2.drop(['articles'], axis=1)
            df_bar = pd.DataFrame({'Terms': df2.columns, 'count': df2.loc[0]})
            print('df bar', df_bar)
            fig = px.bar(df_bar, x='Terms', y='count')
            fig.show()



    def group_chart(self):
        """ same kind of chart as ind_chart but combines all the articles into one chart """


        df = Build.generate_df(self)
        df2 = Build.generate_df2(self, df=df)
        df2 = df2.drop(['misc'], axis=1)


        fig = px.bar(df2, x='articles', y=['time', 'location', 'person', 'war'])
        fig.show()