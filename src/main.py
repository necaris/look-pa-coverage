from typing import NamedTuple

import httpx
from bs4 import BeautifulSoup, element

NEWS_URL = "https://www.insuranceinsider.com/news"


class Article(NamedTuple):
    url: str
    title: str

    @classmethod
    def from_tag(cls, t: element.Tag):
        url = t.get("href")
        assert isinstance(url, str)
        return cls(url=url, title=t.text)


def find_links(p: BeautifulSoup):
    return p.find_all("a", {"class": "Link"})


def filter_articles(tags: list[element.Tag]):
    for t in tags:
        url = t.get("href")
        if (
            isinstance(url, str)
            and url.startswith("https://www.insuranceinsider.com/article")
            and not t.find("img")
            and t.text
        ):
            yield t


def render_table(items: list[NamedTuple]):
    fields = items[0]._fields
    print("\t".join(fields))
    print("-" * 40)
    for i in items:
        print("\t".join(getattr(i, f) for f in fields))


def main():
    res = httpx.get(NEWS_URL)
    soup = BeautifulSoup(res.text, features="html.parser")
    links = find_links(soup)
    article_links = filter_articles(links)
    articles = [Article.from_tag(t) for t in article_links]
    print(render_table(articles))


if __name__ == "__main__":
    main()
