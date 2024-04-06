from main import Article


def test_article_creation():
    assert Article(url="foo", title="bar") == ("foo", "bar")
