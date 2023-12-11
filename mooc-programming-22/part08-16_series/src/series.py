# Write your solution here:
"""Some of the worst code I've written..."""

class Series:
    def __init__(self, name: str, season: int, genres: list):
        self.title = name
        self.season = season
        self.genres = genres # list of strings
        self.rating = []
    
    def __str__(self):
        genre_string = ", ".join(self.genres)

        if len(self.rating) != 0: 
            return f"""\
                {self.title} ({self.season} seasons) 
                genres: {genre_string}
                {len(self.rating)} ratings, average {(sum(self.rating) / len(self.rating)):.1f} points"""
        else: 
            return f"""\
                {self.title} ({self.season} seasons) 
                genres: {genre_string}
                no ratings"""

    
    def rate(self, rating: int):
        if rating >= 0 or rating <= 5:
            self.rating.append(rating)



def minimum_grade(rating: float, series_list: list):
    min_grade_list = []
    for series in series_list:
        if sum(series.rating) / len(series.rating) >= rating:
            min_grade_list.append(series)
    
    return min_grade_list

def includes_genre(genre: str, series_list: list):
    matched = []
    for series in series_list:
        if genre in series.genres: 
            matched.append(series)

    return matched

