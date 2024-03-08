import random
from datetime import datetime

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = 0

    def __repr__(self):
        return f"{self.title} {self.year} {self.genre} {self.views}"
    
    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self):
        self.views += 1
    

        
class Serie(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season.zfill(2)}E{self.episode.zfill(2)}"
    
    def __repr__(self):
        return f"{self.title} S{self.season.zfill(2)}E{self.episode.zfill(2)} {self.year} {self.genre} {self.views}"
    


## Functions
def get_movies(list):
    movies = []
    for i in range(len(list)):
        if isinstance(list[i], Movie) and not isinstance(list[i], Serie):
            movies.append(list[i])
    movies_sort = sorted(movies, key = lambda x: x.title)
    return movies_sort

def get_series(list):
    series = []
    for i in range(len(list)):
        if isinstance(list[i], Serie):
            series.append(list[i])
    series_sort = sorted(series, key= lambda x: x.title)
    return series_sort

def search(list, title):
    i=0
    res = []
    while i < len(list):
        if list[i].title == title:
            res.append(list[i])
        i +=1
    return res

def run_10_times(func):
    def wrapper(*args):
        for i in range(10):
            func(*args)
    return wrapper

@run_10_times
def generate_view(lista):
    instance = random.randint(0, len(lista)-1)
    lista[instance].views += random.randint(1,100)
    
def top_titles(lista, top_number):
    lista_sorted = sorted(lista, key= lambda x: x.views, reverse=True)
    return lista_sorted[0:top_number]

def add_serie(title, year, genre, season, num_of_episodes):
    list_of_episodes = []
    for i in range(num_of_episodes):
        temp = Serie(title=title, year=year, genre=genre, season=season, episode=str(i+1))
        list_of_episodes.append(temp)
    return list_of_episodes

def number_of_episodes(lista, title):
    list_series = get_series(lista)
    number_of_episodes = 0
    for i in range(len(list_series)):
        if list_series[i].title == title:
            number_of_episodes += 1
    
    print(f"{title} contains {number_of_episodes} episodes in the library")


if __name__ == "__main__":
    print("Movie library")
    
    movies_series = []

    dune_1 = Movie(title="Dune 1", year=2021, genre="Sci-fi/Adventure")
    movies_series.append(dune_1)
    dune_2 = Movie(title="Dune 2", year=2024, genre="Sci-fi/Adventure")
    movies_series.append(dune_2)
    oppenheimer = Movie(title="Oppenheimer", year=2023, genre="Historical drama")
    movies_series.append(oppenheimer)
    barbie = Movie(title="Barbie", year=2023, genre="Comedy/Fantasy")
    movies_series.append(barbie)

    dune_1.play()
    dune_2.play()

    friends = Serie(title="Friends", year=1994, genre="TV show", season="1", episode="1")
    movies_series.append(friends)
    avatarS01E01 = Serie(title="Avatar", year=2024, genre="Sci-fi/Adventure", season="1", episode="1")
    movies_series.append(avatarS01E01)
    avatarS01E08 = Serie(title="Avatar", year=2024, genre="Sci-fi/Adventure", season="1", episode="8")
    movies_series.append(avatarS01E08)

    print(friends)

    new_serie = add_serie(title="Dr. House", year=2004, genre="Medical Drama",
                      season="1", num_of_episodes=22)
    movies_series.extend(new_serie)

    generate_view(movies_series) #run 10 times 
    generate_view(movies_series) #run 10 times 

    print(f"Most popular movies and TV shows {datetime.now().strftime('%d.%M.%Y')}")

    top_list = top_titles(movies_series, 3)
    print(top_list)
    
    # Find particular Movies/Series
    result = search(movies_series, "Avatar")
    print(f"List of Avatar serie {result}")

    
    number_of_episodes(movies_series, "Dr. House")