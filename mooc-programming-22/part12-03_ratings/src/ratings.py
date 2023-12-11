# TEE RATKAISUSI TÄHÄN:
# list of dictionary (each dict has details on 1 TV show)
def sort_by_ratings(items: list):
    return sorted(items, key=lambda x : x["rating"], reverse=True)