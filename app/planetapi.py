import numpy as np
import pandas as pd
import math

STAR_COLUMNS = ['pl_hostname', 'st_spstr', 'st_age',
                'st_mass', 'st_rad', 'st_teff', 'st_lum']
PLANET_COLUMNS = ['pl_rade', 'pl_hostname',
                  'pl_ratror', 'pl_masse', 'pl_distance']
SUN_RADIUS = 695510  # km
EFFECTIVE_TEMP_SUN = 5778
NORMALIZATION_FACTORS = {
    'pl_rade': 6.71,
    'pl_masse': 1232.493,
    'pl_distance': 0.163352
}

df = pd.read_csv('app/exoplanets.csv')
df['pl_distance'] = df['pl_ratdor']*df['st_rad']*695510/149597870
df['pl_rade_norm'] = df.pl_rade / NORMALIZATION_FACTORS['pl_rade']
df['pl_masse_norm'] = df.pl_masse / NORMALIZATION_FACTORS['pl_masse']
df['pl_distance_norm'] = df.pl_distance / NORMALIZATION_FACTORS['pl_distance']

stars_df = df.groupby('pl_hostname').first().reset_index()[STAR_COLUMNS]


def distance(v1, v2):
    return np.sqrt(np.nansum(v1 * v2))


def serialize(df):
    return df.where(pd.notnull(df), None)


def get_star_info(star_name):
    row = stars_df[stars_df['pl_hostname'] == star_name]
    if len(row) == 0:
        return None
    return serialize(row.iloc[0]).to_dict()


def similar_planets(pl_rade, pl_masse, pl_distance):
    values = np.array([pl_rade, pl_masse, pl_distance])
    vectors = df[['pl_rade_norm', 'pl_masse_norm', 'pl_distance_norm']]
    distances = vectors.apply(lambda row: distance(row, values), axis=1)
    top = vectors.assign(distance=distances).query(
        'distance > 0').sort_values('distance')
    top_allinfo = df.loc[top.index][PLANET_COLUMNS].assign(
        distance=top.distance)
    return serialize(top_allinfo.head(10)).to_dict(orient='records')


def get_star_stats():
    stats = stars_df.describe()
    return serialize(stats).to_dict()


def get_planet_stats(fields):
    if fields is not None:
        fields = [field for field in fields if field in df.columns]
        stats = df[fields].describe()
    else:
        stats = df.describe()
    return serialize(stats).to_dict()


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
