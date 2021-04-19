import csv
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Movie():
    title: str
    year: int
    score: float

data_file = 'movies.csv'


def get_dir_movies(data=data_file):
    dirs = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for l in csv.DictReader(f):
            try:
                d = l['director_name']
                t = l['movie_title'].replace('\xa0', '')
                y = int(l['title_year'])
                s = float(l['imdb_score'])
            except ValueError:
                continue

            m = Movie(t, y, s)
            dirs[d].append(m)

    return dirs


def get_dir_avg(directors):
    avgs = []
    for d, m in directors.items():
        if len(m) < 4:
            continue
        avg = round(sum(mov.score for mov in m) / len(m), 1)
        avgs.append((d, avg))

    return sorted(avgs, key=lambda i: i[1], reverse=True)[:10]


def print_director(d_name, d_pos, d_avg):
    print()
    txt = f'{str(d_pos).rjust(2, "0")}. {d_name} '
    txt = f'{txt:<85}{str(d_avg)}'
    print(txt)
    print('-' * (len(txt) + 1))


def print_films(films):
    for m in films:
        text = f'{m.year}] {m.title} '
        text = f'{text:<85}{str(m.score)}'
        print(text)


def print_top(dirs, avgs):
    pos = 1
    for d, avg in avgs:
        print_director(d, pos, avg)
        films = dirs[d]
        print_films(films)
        pos += 1


directors = get_dir_movies(data_file)
averages = get_dir_avg(directors)
print_top(directors, averages)
