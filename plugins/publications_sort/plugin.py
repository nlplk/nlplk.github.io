from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup
from copy import deepcopy
from multisort import cmp_func

PUBLICATION_PAGE_NAME = 'Research Publications'
tag_pub_year = 'pub-year'
tag_pub_title = 'pub-title'

class PublicationsSortPlugin(BasePlugin):

  def on_page_content(self, html, page, config, files):
      if page.title == PUBLICATION_PAGE_NAME:
          soup = BeautifulSoup(html, 'html.parser')
          year_tags = soup.find_all('publication')

          sorted_years = sorted(year_tags, key=cmp_func(PublicationsSortPlugin.sort_by_year_name))
          new_sorted_years = deepcopy(sorted_years)

          for i in range(0, len(year_tags)):
            year_tags[i].replace_with(new_sorted_years[i])

          return str(soup)

  def sort_by_year_name(pub_a, pub_b):
    if pub_a is None: return -1
    if pub_b is None: return 1

    year_a: int = int(pub_a.find(tag_pub_year).string if pub_a.find(tag_pub_year) else -1)
    year_b: int = int(pub_b.find(tag_pub_year).string if pub_b.find(tag_pub_year) else -1)

    if year_a == year_b: 
      title_a: str = pub_a.find(tag_pub_title).string if pub_a.find(tag_pub_title) else 'z'
      title_b: str = pub_b.find(tag_pub_title).string if pub_b.find(tag_pub_title) else 'z'

      if title_a > title_b:
         return 1
      else:
         return -1

    elif year_a > year_b:
       return -1
    else:
       return 1
