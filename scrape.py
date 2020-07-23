from bs4 import BeautifulSoup
import requests


source = requests.get('https://finance.yahoo.com/calendar/splits?from=2020-07-12&to=2020-07-18&day=2020-07-14').text
print(source.prettify())
soup = BeautifulSoup(source, 'lxml')

article = soup.find('simpTblRow Bgc($hoverBgColor):h BdB Bdbc($finLightGrayAlt) Bdbc($tableBorderBlue):h H(32px) Bgc(white) ')
