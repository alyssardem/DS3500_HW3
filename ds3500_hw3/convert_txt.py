import urllib.request
from bs4 import BeautifulSoup


def convert_txt(url: object, textfile_name: object, txt_name: object) -> object:
    """ converts urls of news articles into txt info files and txt content files
    url - website link
    textfile_name - name to give txt info file
    txt_name - name to give txt content file """
    # retrieves given url and saves it into project folder
    urllib.request.urlretrieve(url, "C:/Users/ardem/classes/ds3500_hw3/" + textfile_name)

    # opens, reads, and saves content
    f = open("C:/Users/ardem/classes/ds3500_hw3/" + textfile_name, "r", errors="ignore")
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    f = open("C:/Users/ardem/classes/ds3500_hw3/" + txt_name, "w")

    # traverse paragraphs from soup
    for data in soup.find_all("p"):
        sum = data.get_text()
        f.writelines(sum)

    # close the file and return the txt files
    f.close()

    return f

# Convert Russia articles to txt
russia_article1 = convert_txt(
    "https://www.themoscowtimes.com/2023/02/22/muscovites-shrug-as-russia-marks-one-year-of-ukraine-war-a80281",
    'textfile1_russia.txt', 'moscow_times1')

russia_article2 = convert_txt(
    "https://www.themoscowtimes.com/2023/02/22/heineken-denies-claim-it-broke-promise-to-exit-russian-market-a80309",
    'textfile2_russia.txt', 'moscow_times2')

# Convert UK articles to txt
uk_article1 = convert_txt(
    "https://www.bbc.com/news/world-europe-56720589",
    'textfile1_uk.txt', 'bbc1')

uk_article2 = convert_txt(
    "https://www.bbc.com/news/world-us-canada-64727302",
    'textfile2_uk.txt', 'bbc2')

# Convert US articles to txt
# us_article1 = convert_txt(
#     "https://www.nytimes.com/2023/02/24/world/europe/ukraine-russia-war-anniversary.html",
#     'textfile1_us.txt', 'ny_times1')

# us_article2 = convert_txt(
#     "https://www.nytimes.com/2023/02/18/opinion/ukraine-biden.html",
#     'textfile2_us.txt', 'ny_times2')

# Convert China articles to txt
china_article1 = convert_txt(
    "https://www.globaltimes.cn/page/202302/1285962.shtml",
    'textfile1_china.txt', 'global_times1')

china_article2 = convert_txt(
    "https://www.globaltimes.cn/page/202302/1285842.shtml",
    'textfile2_china.txt', 'global_times2')

