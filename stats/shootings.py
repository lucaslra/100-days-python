import csv
import enum
from collections import defaultdict
from dataclasses import dataclass
from typing import Iterable


# Based om Dataset format
class Sex(enum.Enum):
    NotInformed = ''
    Unknown = 'U'
    Male = 'M'
    Female = 'F'


@dataclass
class Shooting:
    boro: str
    perp_race: str
    perp_sex: Sex
    victim_race: str
    victim_sex: Sex
    year: int


def shootings_stats(shooting_data: Iterable):
    by_boro = defaultdict(list)
    by_victim_race = defaultdict(list)
    by_perp_race = defaultdict(list)
    by_victim_sex = defaultdict(list)
    by_perp_sex = defaultdict(list)
    by_year = defaultdict(list)

    for shooting in shooting_data:
        incident = Shooting(
            boro=shooting['BORO'],
            perp_race=shooting['PERP_RACE'],
            perp_sex=Sex(shooting['PERP_SEX']),
            victim_race=shooting['VIC_RACE'],
            victim_sex=Sex(shooting['VIC_SEX']),
            year=int(shooting['OCCUR_DATE'].split('/')[2])
        )
        by_boro[incident.boro].append(incident)
        by_victim_race[incident.victim_race].append(incident)
        by_victim_sex[incident.victim_sex].append(incident)
        by_perp_race[incident.perp_race].append(incident)
        by_perp_sex[incident.perp_sex].append(incident)
        by_year[incident.year].append(incident)

    return {
        'by_boro': by_boro,
        'by_victim_race': by_victim_race,
        'by_victim_sex': by_victim_sex,
        'by_perp_race': by_perp_race,
        'by_perp_sex': by_perp_sex,
        'by_year': by_year
    }


def count_stats(stats_data: defaultdict):
    counter = {}
    for stat, inc in stats_data.items():
        if stat is enum.Enum:
            stat = stat.value
        counter[stat] = len(inc)

    return sorted(counter.items(), key=lambda i: i[1], reverse=True)


with open('NYPD_Shooting_Incident_Data__Historic_.csv') as f:
    data = csv.DictReader(f)
    stats = shootings_stats(data)
    print(count_stats(stats['by_perp_race']))
    print(count_stats(stats['by_victim_race']))
    print(count_stats(stats['by_boro']))
    print(count_stats(stats['by_year']))
