import pandas as pd
import math

STAR_COLUMNS = ['st_spstr', 'st_age',
                'st_mass', 'st_rad', 'st_teff', 'st_lum']
PLANET_COLUMNS = ['pl_rade', 'pl_hostname', '']

df = pd.read_csv('app/exoplanets.csv')
stars_df = df.groupby('pl_hostname').first()[STAR_COLUMNS]
SUN_RADIUS = 695510  # km
EFFECTIVE_TEMP_SUN = 5778


def get_star_info(star_name):
    rows = df[df['pl_hostname'] == star_name]
    if len(rows) == 0:
        return None
    series = rows.iloc[0][STAR_COLUMNS]
    series = series.where(pd.notnull(series), None)
    return series.to_dict()


def similar_planets():
    return 1


def get_star_stats():
    stats = stars_df.describe()
    stats = stats.where(pd.notnull(stats), None)
    return stats.to_dict()


def get_planet_stats(fields):
    if fields is not None:
        fields = [field for field in fields if field in df.columns]
        stats = df[fields].describe()
    else:
        stats = df.describe()
    stats = stats.where(pd.notnull(stats), None)
    return stats.to_dict()


def random_star():
    star_name = df['pl_hostname'].sample().values[0]
    print(star_name)
    return get_star_info(star_name)


def habitable_zones(radius, effective_temp):
    luminosity_quotient = (radius/SUN_RADIUS)**2 * \
        (effective_temp/EFFECTIVE_TEMP_SUN)**4
    min_rad = 0.75 * math.sqrt(luminosity_quotient)
    mean_rad = math.sqrt(luminosity_quotient)
    max_rad = 1.77 * math.sqrt(luminosity_quotient)

    return {'min': min_rad, 'center': mean_rad, 'max': max_rad}
