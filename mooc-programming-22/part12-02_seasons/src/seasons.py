# Write your solution here:

# list of dictionary (each dict has details on 1 TV show)
def sort_by_seasons(items: list):
    return sorted(items, key=lambda x : x["seasons"])


if __name__ == "__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, 
             { "name": "Friends", "rating" : 8.9, "seasons":10 },  
             { "name": "Simpsons", "rating" : 8.7, "seasons":32 }]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")