from newsfeed.reporter.reporter import Reporter
import pytest
import time

@pytest.fixture(scope="session", autouse=True)
def reporter():
    print("\nTesting API Connection\n")
    start_time = time.process_time()
    reporter = Reporter(key='')
    print(time.process_time() - start_time, "seconds")
    return reporter

def test_get_sources(reporter):
    print("\nTesting Get Sources\n")
    start_time = time.process_time()
    test_sources = reporter.get_sources()
    #print(test_sources)
    print(time.process_time() - start_time, "seconds")
    assert(test_sources.get('status') == 'ok')
    assert(len(test_sources.get('sources')) > 0)

def test_get_top_headlines(reporter):
    print("\nTesting Get Top Headlines\n")
    start_time = time.process_time()
    test_top_headlines = reporter.get_top_headlines()
    #print(test_top_headlines)
    print(time.process_time() - start_time, "seconds")
    assert(test_top_headlines.get('status') == 'ok')
    assert(test_top_headlines.get('totalResults') > 0)

def test_search_with_keyword(reporter):
    print("\nTesting Search 'Apple'\n")
    start_time = time.process_time()
    test_search = reporter.search_articles("Apple")
    #print(test_search)
    print(time.process_time() - start_time, "seconds")
    assert(test_search.get('status') == 'ok')
    assert(test_search.get('totalResults') > 0)

def test_search_with_multiple_keywords(reporter):
    print("\nTesting Search 'Big Tech Mogul'\n")
    start_time = time.process_time()
    test_search = reporter.search_articles("Big Tech Mogul")
    #print(test_search)
    print(time.process_time() - start_time, "seconds")
    assert(test_search.get('status') == 'ok')
    assert(test_search.get('totalResults') > 0)

def test_search_with_gibberish(reporter):
    print("\nTesting Search Nonsense\n")
    start_time = time.process_time()
    test_search = reporter.search_articles("fjgdjkgnskjngsjkfgnskj")
    #print(test_search)
    print(time.process_time() - start_time, "seconds")
    assert(test_search.get('status') == 'ok')
    assert(test_search.get('totalResults') == 0)

#test_api = Reporter()
#print(test_api.get_sources())
#print(test_api.get_top_headlines())
#print(test_api.search_articles("Apple"))