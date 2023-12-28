from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup
from copy import deepcopy
from multisort import cmp_func

PUBLICATION_PAGE_NAME = 'Research Publications'
tag_pub_year = 'pub-year'
tag_pub_title = 'pub-title'
tag_pub_authors = 'pub-authors'


class PublicationsSortPlugin(BasePlugin):

  def on_page_content(self, html, page, config, files):
    if page.title == PUBLICATION_PAGE_NAME:
      soup = BeautifulSoup(html, 'html.parser')
      publication_tags = soup.find_all('publication')

      PublicationsSortPlugin.verify_no_duplicates(publication_tags=publication_tags)
      sorted_publication_tags = sorted(publication_tags, key=cmp_func(PublicationsSortPlugin.sort_by_year_name))
      new_sorted_publication_tags = deepcopy(sorted_publication_tags)

      for i in range(0, len(publication_tags)):
        publication_tags[i].replace_with(new_sorted_publication_tags[i])

      return str(soup)

  def sort_by_year_name(pub_a, pub_b):
    if pub_a is None: return -1
    if pub_b is None: return 1

    year_a: int = int(pub_a.find(tag_pub_year).string.strip() if pub_a.find(tag_pub_year) else -1)
    year_b: int = int(pub_b.find(tag_pub_year).string.strip() if pub_b.find(tag_pub_year) else -1)

    if year_a == year_b: 
      title_a: str = pub_a.find(tag_pub_title).string.strip() if pub_a.find(tag_pub_title) else 'z'
      title_b: str = pub_b.find(tag_pub_title).string.strip() if pub_b.find(tag_pub_title) else 'z'

      if title_a > title_b:
         return 1
      else:
         return -1

    elif year_a > year_b:
       return -1
    else:
       return 1
  
  def verify_no_duplicates(publication_tags):
    publication_set: set = set()
    for publication_tag in publication_tags:
      title: str = publication_tag.find(tag_pub_title).string.replace(' ','').replace(',','').replace('.','').lower()
      year: str = publication_tag.find(tag_pub_year).string.replace(' ','').lower()
      authors: str = publication_tag.find(tag_pub_authors).string.replace(' ','').replace(',','').replace('.','').lower()
        
      publication_set.add(title.join(year).join(authors))
    
    if(len(publication_set) != len(publication_tags)):
        raise RuntimeError('Duplicate publication entries found')
      



