import numpy as np
import pandas as pd
import math

STAR_COLUMNS = ['pl_hostname', 'st_spstr', 'st_age',
                'st_mass', 'st_rad', 'st_teff', 'st_lum']
PLANET_COLUMNS = ['pl_name', 'pl_rade',
                  'pl_ratror', 'pl_masse', 'pl_distance',
                  'pl_disc', 'pl_status',  'pl_pelink', 'pl_edelink', 'pl_orbsmax', 'in_hz']

SUN_RADIUS = 695510  # km
EFFECTIVE_TEMP_SUN = 5778
NORMALIZATION_FACTORS = {
    'pl_rade': 6.71,
    'pl_masse': 1232.493,
    'pl_distance': 0.163352,
    'pl_orbsmax': 0.5
}

df = pd.read_csv('app/exoplanets.csv')
df['pl_distance'] = df['pl_ratdor']*df['st_rad']*SUN_RADIUS/149597870
df['pl_rade_norm'] = df.pl_rade / NORMALIZATION_FACTORS['pl_rade']
df['pl_masse_norm'] = df.pl_masse / NORMALIZATION_FACTORS['pl_masse']
df['pl_distance_norm'] = df.pl_distance / NORMALIZATION_FACTORS['pl_distance']
df['pl_orbsmax_norm'] = df.pl_orbsmax / NORMALIZATION_FACTORS['pl_orbsmax']

stars_df = df.groupby('pl_hostname').first().reset_index()[STAR_COLUMNS]


def habitable_zones(radius, effective_temp):
    luminosity_quotient = (radius/SUN_RADIUS)**2 * \
        (effective_temp/EFFECTIVE_TEMP_SUN)**4
    min_rad = 0.75 * math.sqrt(luminosity_quotient)
    mean_rad = math.sqrt(luminosity_quotient)
    max_rad = 1.77 * math.sqrt(luminosity_quotient)

    return {'min': min_rad, 'center': mean_rad, 'max': max_rad}


def planet_in_hz(planet):
    regions = habitable_zones(planet['st_rad'], planet['st_teff'])
    mx = regions['max']
    mn = regions['min']
    return mn <= planet['pl_orbper'] <= mx


df['in_hz'] = df.apply(planet_in_hz, axis=1)


# utils

def distanceL1(v1, v2):
    return np.nansum(abs(v1 - v2))


def distanceL2(v1, v2):
    return np.sqrt(np.nansum((v1 - v2)**2))


def serialize(df):
    return df.where(pd.notnull(df), None)


def get_star_info(star_name):
    row = stars_df[stars_df['pl_hostname'] == star_name]
    if len(row) == 0:
        return None
    return serialize(row.iloc[0]).to_dict()


# api

def similar_planets(pl_rade, pl_orbsmax, first=10):
    values = np.array([pl_rade / NORMALIZATION_FACTORS['pl_rade'],
                       pl_orbsmax / NORMALIZATION_FACTORS['pl_orbsmax']])
    vectors = df[['pl_rade_norm', 'pl_orbsmax_norm']]
    distances = vectors.apply(lambda row: distanceL2(row, values), axis=1)
    top = vectors.assign(distance=distances).query(
        'distance > 0').sort_values('distance')
    top_allinfo = df.loc[top.index][STAR_COLUMNS + PLANET_COLUMNS].assign(
        distance=top.distance)
    return serialize(top_allinfo.head(first)).to_dict(orient='records')


def get_star_stats():
    stats = stars_df.describe()
    max95 = stars_df.quantile(0.90)
    max95.name = 'max95'

    return serialize(stats.append(max95)).to_dict()


def get_planet_stats(fields):
    if fields is not None:
        fields = [field for field in fields if field in df.columns]
        stats = df[fields].describe()
    else:
        stats = df.describe()

    max95 = df.quantile(0.90)
    max95.name = 'max95'
    return serialize(stats.append(max95)).to_dict()


def random_star():
    star_name = stars_df['pl_hostname'].sample().values[0]
    return get_star_info(star_name)
