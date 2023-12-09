```python
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


```


### Model Solution
similiar to mine actually, I like the way ratings and the __str__ constructor was handled

```
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = [0, 0, 0, 0, 0, 0]
        self.number_of_ratings = 0
 
    def grade(self):
        if self.number_of_ratings == 0:
            return 0
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            return grade_sum / self.number_of_ratings
 
 
    def __str__(self):
        genres = ", ".join(self.genres)
 
        if self.number_of_ratings == 0:
            ratings = "no ratings"
        else:
            grade_sum = 0
            for i in range(0, 6):
                grade_sum += self.ratings[i] * i
            ka = grade_sum / self.number_of_ratings
            ratings = f"{self.number_of_ratings} ratings, average {ka:.1f} points"
 
        return f"{self.title} ({self.seasons} seasons)\ngenres: {genres}\n{ratings}"
 
    def rate(self, grade: int):
        self.number_of_ratings += 1
        self.ratings[grade] += 1
 
def minimum_grade(grade: float, seriest: list):
    result = []
    for series in seriest:
        if series.grade() >= grade:
            result.append(series)
 
    return result
 
def includes_genre(genre: str, seriest: list):
    result = []
    for series in seriest:
        if genre in series.genres:
            result.append(series)
 
    return result
 
if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    seriest = [s1, s2, s3]
 
    answer = minimum_grade(4.5, seriest)
    print(answer)
```