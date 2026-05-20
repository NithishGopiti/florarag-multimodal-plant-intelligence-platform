cache_store = {}

def cache_recommendation(query, recommendation):

    cache_store[query] = recommendation

def retrieve_cached_recommendation(query):

    return cache_store.get(query)
