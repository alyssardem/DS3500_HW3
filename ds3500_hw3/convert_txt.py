import urllib.request
from bs4 import BeautifulSoup

# # Russia Articles
# urllib.request.urlretrieve("https://www.themoscowtimes.com/2023/02/22/muscovites-shrug-as-russia-marks-one-year-of-ukraine-war-a80281",
#                            "C:/Users/ardem/classes/ds3500_hw3/textfile1_russia.txt")
# urllib.request.urlretrieve("https://www.themoscowtimes.com/2023/02/22/heineken-denies-claim-it-broke-promise-to-exit-russian-market-a80309",
#                            "C:/Users/ardem/classes/ds3500_hw3/textfile2_russia.txt")
#
# file_r1 = open("C:/Users/ardem/classes/ds3500_hw3/textfile1_russia.txt", errors="ignore")
# file_r2 = open("C:/Users/ardem/classes/ds3500_hw3/textfile2_russia.txt", errors="ignore")
#
# contents_r1 = file_r1.read()
# contents_r2 = file_r2.read()
#
# soup_r1 = BeautifulSoup(contents_r1, 'html.parser')
# soup_r2 = BeautifulSoup(contents_r2, 'html.parser')
# f_r1 = open("C:/Users/ardem/classes/ds3500_hw3/textfile1_russia.txt", "w")
# f_r2 = open("C:/Users/ardem/classes/ds3500_hw3/textfile2_russia.txt", "w")
#
# # traverse paragraphs from soup
# for data in soup_r1.find_all("p"):
#     sum_r1 = data.get_text()
#     f_r1.writelines(sum_r1)
#
# for data in soup_r2.find_all("p"):
#     sum_r2 = data.get_text()
#     f_r2.writelines(sum_r2)
#
# f_r1.close()
# f_r2.close()


def convert_txt(url: object, textfile_name: object, txt_name: object) -> object:
    urllib.request.urlretrieve(url, "C:/Users/ardem/classes/ds3500_hw3/" + textfile_name)
    f = open("C:/Users/ardem/classes/ds3500_hw3/" + textfile_name, "r", errors="ignore")
    contents = f.read()
    soup = BeautifulSoup(contents, 'html.parser')
    f = open("C:/Users/ardem/classes/ds3500_hw3/" + txt_name, "w")

    # traverse paragraphs from soup
    for data in soup.find_all("p"):
        sum = data.get_text()
        f.writelines(sum)

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

