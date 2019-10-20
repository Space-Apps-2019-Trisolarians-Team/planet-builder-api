import numpy as np
import pandas as pd
import math

STAR_COLUMNS = ['pl_hostname', 'st_spstr', 'st_age',
                'st_mass', 'st_rad', 'st_teff', 'st_lum']
PLANET_COLUMNS = ['pl_rade', 'pl_hostname',
                  'pl_ratror', 'pl_masse', 'pl_distance']

df = pd.read_csv('app/exoplanets.csv')
df['pl_distance'] = df['pl_ratdor']*df['st_rad']*695510/149597870
stars_df = df.groupby('pl_hostname').first().reset_index()[STAR_COLUMNS]

SUN_RADIUS = 695510  # km
EFFECTIVE_TEMP_SUN = 5778


def distance(v1, v2):
    return np.sqrt(np.nansum(v1 * v2))


def serialize(df, orient='dict'):
    return df.where(pd.notnull(df), None).to_dict(orient=orient)


def get_star_info(star_name):
    row = stars_df[stars_df['pl_hostname'] == star_name]
    if len(row) == 0:
        return None
    return serialize(row.iloc[0])


def similar_planets(**kwargs):
    keys = list(kwargs.keys())
    values = list(kwargs.values())
    vectors = df[keys]
    distances = vectors.apply(lambda row: distance(row, values), axis=1)
    top = vectors.assign(distance=distances).query(
        'distance > 0').sort_values('distance')
    top_allinfo = df.loc[top.index][PLANET_COLUMNS].assign(distance=top.distance)
    return serialize(top_allinfo.head(10), orient='records')


def get_star_stats():
    stats = stars_df.describe()
    return serialize(stats)


def get_planet_stats(fields):
    if fields is not None:
        fields = [field for field in fields if field in df.columns]
        stats = df[fields].describe()
    else:
        stats = df.describe()
    return serialize(stats)


def random_star():
    star_name = stars_df['pl_hostname'].sample().values[0]
    return get_star_info(star_name)


def habitable_zones(radius, effective_temp):
    luminosity_quotient = (radius/SUN_RADIUS)**2 * \
        (effective_temp/EFFECTIVE_TEMP_SUN)**4
    min_rad = 0.75 * math.sqrt(luminosity_quotient)
    mean_rad = math.sqrt(luminosity_quotient)
    max_rad = 1.77 * math.sqrt(luminosity_quotient)

    return {'min': min_rad, 'center': mean_rad, 'max': max_rad}
