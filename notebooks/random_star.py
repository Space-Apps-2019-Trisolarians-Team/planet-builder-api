import pandas as pd

df = pd.read_csv('../app/exoplanets.csv')


txt = """
# COLUMN pl_hostname:    Host Name
# COLUMN pl_letter:      Planet Letter
# COLUMN pl_name:        Planet Name
# COLUMN pl_discmethod:  Discovery Method
# COLUMN pl_controvflag: Controversial Flag
# COLUMN pl_pnum:        Number of Planets in System
# COLUMN pl_orbper:      Orbital Period [days]
# COLUMN pl_orbpererr1:  Orbital Period Upper Unc. [days]
# COLUMN pl_orbpererr2:  Orbital Period Lower Unc. [days]
# COLUMN pl_orbperlim:   Orbital Period Limit Flag
# COLUMN pl_orbsmax:     Orbit Semi-Major Axis [AU])
# COLUMN pl_orbsmaxerr1: Orbit Semi-Major Axis Upper Unc. [AU]
# COLUMN pl_orbsmaxerr2: Orbit Semi-Major Axis Lower Unc. [AU]
# COLUMN pl_orbsmaxlim:  Orbit Semi-Major Axis Limit Flag
# COLUMN pl_orbeccen:    Eccentricity
# COLUMN pl_orbeccenerr1: Eccentricity Upper Unc.
# COLUMN pl_orbeccenerr2: Eccentricity Lower Unc.
# COLUMN pl_orbeccenlim: Eccentricity Limit Flag
# COLUMN pl_orbincl:     Inclination [deg]
# COLUMN pl_orbinclerr1: Inclination Upper Unc. [deg]
# COLUMN pl_orbinclerr2: Inclination Lower Unc. [deg]
# COLUMN pl_orbincllim:  Inclination Limit Flag
# COLUMN pl_bmassj:      Planet Mass or M*sin(i) [Jupiter mass]
# COLUMN pl_bmassjerr1:  Planet Mass or M*sin(i) Upper Unc. [Jupiter mass]
# COLUMN pl_bmassjerr2:  Planet Mass or M*sin(i) Lower Unc. [Jupiter mass]
# COLUMN pl_bmassjlim:   Planet Mass or M*sin(i) Limit Flag
# COLUMN pl_bmassprov:   Planet Mass or M*sin(i) Provenance
# COLUMN pl_radj:        Planet Radius [Jupiter radii]
# COLUMN pl_radjerr1:    Planet Radius Upper Unc. [Jupiter radii]
# COLUMN pl_radjerr2:    Planet Radius Lower Unc. [Jupiter radii]
# COLUMN pl_radjlim:     Planet Radius Limit Flag
# COLUMN pl_dens:        Planet Density [g/cm**3]
# COLUMN pl_denserr1:    Planet Density Upper Unc. [g/cm**3]
# COLUMN pl_denserr2:    Planet Density Lower Unc. [g/cm**3]
# COLUMN pl_denslim:     Planet Density Limit Flag
# COLUMN pl_ttvflag:     TTV Flag
# COLUMN pl_kepflag:     Kepler Field Flag
# COLUMN pl_k2flag:      K2 Mission Flag
# COLUMN pl_nnotes:      Number of Notes
# COLUMN ra_str:         RA [sexagesimal]
# COLUMN ra:             RA [decimal degrees]
# COLUMN dec_str:        Dec [sexagesimal]
# COLUMN dec:            Dec [decimal degrees]
# COLUMN st_dist:        Distance [pc]
# COLUMN st_disterr1:    Distance Upper Unc. [pc]
# COLUMN st_disterr2:    Distance Lower Unc. [pc]
# COLUMN st_distlim:     Distance Limit Flag
# COLUMN gaia_dist:      Gaia Distance [pc]
# COLUMN gaia_disterr1:  Gaia Distance Upper Unc. [pc]
# COLUMN gaia_disterr2:  Gaia Distance Lower Unc. [pc]
# COLUMN gaia_distlim:   Gaia Distance Limit Flag
# COLUMN st_optmag:      Optical Magnitude [mag]
# COLUMN st_optmagerr:   Optical Magnitude Unc. [mag]
# COLUMN st_optmaglim:   Optical Magnitude Limit Flag
# COLUMN st_optband:     Optical Magnitude Band
# COLUMN gaia_gmag:      G-band (Gaia) [mag]
# COLUMN gaia_gmagerr:   G-band (Gaia) Unc. [mag]
# COLUMN gaia_gmaglim:   G-band (Gaia) Limit Flag
# COLUMN st_teff:        Effective Temperature [K]
# COLUMN st_tefferr1:    Effective Temperature Upper Unc. [K]
# COLUMN st_tefferr2:    Effective Temperature Lower Unc. [K]
# COLUMN st_tefflim:     Effective Temperature Limit Flag
# COLUMN st_mass:        Stellar Mass [Solar mass]
# COLUMN st_masserr1:    Stellar Mass Upper Unc. [Solar mass]
# COLUMN st_masserr2:    Stellar Mass Lower Unc. [Solar mass]
# COLUMN st_masslim:     Stellar Mass Limit Flag
# COLUMN st_rad:         Stellar Radius [Solar radii]
# COLUMN st_raderr1:     Stellar Radius Upper Unc. [Solar radii]
# COLUMN st_raderr2:     Stellar Radius Lower Unc. [Solar radii]
# COLUMN st_radlim:      Stellar Radius Limit Flag
# COLUMN rowupdate:      Date of Last Update
# COLUMN pl_facility:    Discovery Facility
"""
import re
regex = r'COLUMN (?P<key>[a-z_\d]+)\: *(?P<description>.+)'
column_data = []
for line in txt.strip().splitlines():
  matches = re.search(regex, line)
  column_data.append([matches.group('key'), matches.group('description')])

column_description = pd.DataFrame(column_data, columns=['key', 'description'])
column_description



df['pl_hostname'].unique().sample().values[0]

star_columns = ['pl_hostname', 'st_spstr', 'st_age', 'st_mass', 'st_rad', 'st_teff', 'st_lum']
series = df[df['pl_hostname'] == df['pl_hostname'].sample().values[0]].iloc[0][star_columns]
series.where(pd.notnull(series), None)




df['pl_hostname'].nunique()

stars_df = df.groupby('pl_hostname').first().reset_index()[star_columns]
stars_df
stars_df.describe().to_dict()

stars_df.head()['pl_hostname'].sample()


stars_df[stars_df.index == '11 Com']

- distancia
- radio
- tilt

df.describe().where(pd.notnull(df.describe()), None).to_json()

[field for field in ['a', 'b', 'pl_hostname'] if field in df.columns]
df[['asd']]


stars_df[stars_df['pl_hostname'] == '11 Com']
stars_df[] == '11 Com'
stars_df.index



########## similar Planets
df.sample()
df.sample()[['pl_hostname', 'pl_rade', 'pl_ratror', 'pl_masse']]
df['pl_rade'].hist(bins=20)

import numpy as np

def is_outlier(points, thresh=3.5):
    if len(points.shape) == 1:
        points = points[:,None]
    median = np.nanmedian(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.nanmedian(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > thresh

def normalize(points, thresh=3.5):
    without_outliers = points.loc[~is_outlier(points, thresh)]
    # min = without_outliers.min()
    max = without_outliers.max()
    print(max)
    return without_outliers/max

normalize(df['pl_rade']).hist(bins=50)
normalize(df['pl_masse']).hist(bins=50)
normalize(df['pl_distance']).hist(bins=50)


df[~is_outlier(df['pl_rade'], thresh=3.50)]['pl_rade'].hist(bins=20)
(df[~is_outlier(df['pl_rade'], thresh=3.5)]['pl_rade']/ 7 ).hist(bins=20)



df[~is_outlier(df['pl_masse'], thresh=3.5)].query('pl_masse > 0')['pl_masse'].hist(bins=200)
(df[~is_outlier(df['pl_masse'], thresh=3.5)].query('pl_masse > 0')['pl_masse'] / 1200).hist(bins=200)


df['pl_distance'] = df['pl_ratdor']*df['st_rad']*695510/149597870
df[~is_outlier(df['pl_distance'], thresh=3.5)]['pl_distance'].hist(bins=200)
(df[~is_outlier(df['pl_distance'], thresh=3.5)]['pl_distance'] / 0.16).hist(bins=200)


def distance(v1, v2):
    return np.sqrt(np.nansum(v1 * v2))

kwargs = {'pl_distance': 0.04, 'pl_masse': 1, 'pl_rade': 3}
keys = kwargs.keys()
values = np.array(list(kwargs.values()))
vectors = df[keys]
vectors.values
np.sqrt(vectors.values.dot(values))

distances = vectors.apply(lambda row: distance(row, values), axis=1)
vectors.assign(distance=distances)
top = vectors.assign(distance=distances).query('distance > 0').sort_values('distance')
top
df.loc[top.index].assign(distance=top.distance)
res = df.loc[top.index].assign(distance=top.distance).head(5)
res.to_dict(orient='records')


NORMALIZATION_FACTORS = {
    'pl_rade': 6.71,
    'pl_masse': 1232.493,
    'pl_distance': 0.163352
}
pl_rade = 1
pl_masse = 1
pl_distance = 1
values = np.array([pl_rade, pl_masse, pl_distance])

df['pl_rade_norm'] = df.pl_rade / NORMALIZATION_FACTORS['pl_rade']
df['pl_masse_norm'] = df.pl_masse / NORMALIZATION_FACTORS['pl_masse']
df['pl_distance_norm'] = df.pl_distance / NORMALIZATION_FACTORS['pl_distance']
vectors = df[['pl_rade_norm', 'pl_masse_norm', 'pl_distance_norm']]
distances = vectors.apply(lambda row: distance(row, values), axis=1)
top = vectors.assign(distance=distances).query(
    'distance > 0').sort_values('distance')
top_allinfo = df.loc[top.index][PLANET_COLUMNS].assign(
    distance=top.distance)
return serialize(top_allinfo.head(10)).to_dict(orient='records')







import math
SUN_RADIUS = 695510  # km
EFFECTIVE_TEMP_SUN = 5778
def habitable_zones(radius, effective_temp):
    luminosity_quotient_r = math.sqrt((radius)**2 * (effective_temp/EFFECTIVE_TEMP_SUN)**4)
    min_rad = 0.75 * luminosity_quotient_r
    mean_rad = luminosity_quotient_r
    max_rad = 1.77 * luminosity_quotient_r

    return {'min': min_rad, 'center': mean_rad, 'max': max_rad}


stars_df.head()
def planet_in_hz(planet):
    regions = habitable_zones(planet['st_rad'], planet['st_teff'])
    mx = regions['max']
    mn = regions['min']
    return mn <= planet['pl_orbper'] <= mx


df.apply(planet_in_hz, axis=1)
df['in_hz'] = df.apply(planet_in_hz, axis=1)
df.head()




###########


somedata = pd.read_json('https://exoplanet-api.herokuapp.com/exoplanet/')
somedata['habitability'].sum()


# df.apply(lambda g: g['pl_orbsmax']/(1+g['pl_orbeccen']),axis=1).notnull().sum()
# df['pl_orbsmax'].notnull().sum()
df['pl_orbsmax'].hist()
without_outliers(df['pl_orbsmax'])

df['pl_orbsmax'].loc[~is_outlier(df['pl_orbsmax'])].hist(bins=30)



df.describe()
max95 = df.quantile(0.95)
max95.name = 'max95'
df.describe().append(max95)


###
df.pl_orbsmax.notnull().sum()
