from bs4 import BeautifulSoup

import main

def test_filter_articles():
    soup = BeautifulSoup('<a></a>', features='html.parser')
    tags = [soup.a]
    assert list(main.filter_articles(tags)) == []
