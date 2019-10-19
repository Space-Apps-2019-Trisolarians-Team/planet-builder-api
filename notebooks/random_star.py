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



df['pl_hostname'].sample().values[0]

star_columns = ['st_spstr', 'st_age', 'st_mass', 'st_rad', 'st_teff', 'st_lum']
series = df[df['pl_hostname'] == df['pl_hostname'].sample().values[0]].iloc[0][star_columns]
series.where(pd.notnull(series), None)



df['pl_hostname'].nunique()

stars_df = df.groupby('pl_hostname').first()[star_columns]
stars_df
stars_df.describe().to_dict()

- distancia
- radio
- tilt

df.describe().where(pd.notnull(df.describe()), None).to_json()
