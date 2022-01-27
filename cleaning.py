from turtle import shape
import pandas as pd 
import csv 

df = pd.read_csv("final.csv")
print(df.shape)
del df["hyperlink"]
print(df.shape)
del df["temp_planet_date"]
print(df.shape)
del df["temp_planet_mass"]
print(df.shape)
del df["pl_letter"]
print(df.shape)
del df["pl_name"]
print(df.shape)
del df["pl_controvflag"]
print(df.shape)
del df["pl_pnum"]
print(df.shape)
del df["pl_orbper"]
print(df.shape)
del df["pl_orbpererr1"]
print(df.shape)
del df["pl_orbpererr2"]
print(df.shape)
del df["pl_orbperlim"]
print(df.shape)
del df["pl_orbsmax"]
print(df.shape)
del df["pl_orbsmaxerr1"]
print(df.shape)
del df["pl_orbsmaxerr2"]
print(df.shape)
del df["pl_orbsmaxlim"]
print(df.shape)
del df["pl_orbeccen"]
print(df.shape)
del df["pl_orbeccenerr1"]
print(df.shape)
del df["pl_orbeccenerr2"]
print(df.shape)
del df["pl_orbeccenlim"]
print(df.shape)
del df["pl_orbinclerr1"]
print(df.shape)
del df["pl_orbinclerr2"]
print(df.shape)
del df["pl_orbincllim"]
print(df.shape)
del df["pl_bmassj"]
print(df.shape)
del df["pl_bmassjerr1"]
print(df.shape)
del df["pl_bmassjerr2"]
print(df.shape)
del df["pl_bmassjlim"]
print(df.shape)
del df["pl_bmassprov"]
print(df.shape)
del df["pl_radj"]
print(df.shape)
del df["pl_radjerr1"]
print(df.shape)
del df["pl_radjerr2"]
print(df.shape)
del df["pl_radjlim"]
print(df.shape)
del df["pl_denserr1"]
print(df.shape)
del df["pl_denserr2"]
print(df.shape)
del df["pl_denslim"]
print(df.shape)
del df["pl_ttvflag"]
print(df.shape)
del df["pl_kepflag"]
print(df.shape)
del df["pl_k2flag"]
print(df.shape)
del df["pl_nnotes"]
print(df.shape)
del df["ra"]
print(df.shape)
del df["dec"]
print(df.shape)
del df["st_dist"]
print(df.shape)
del df["st_disterr1"]
print(df.shape)
del df["st_disterr2"]
print(df.shape)
del df["st_distlim"]
print(df.shape)
del df["gaia_dist"]
print(df.shape)
del df["gaia_disterr1"]
print(df.shape)
del df["gaia_disterr2"]
print(df.shape)
del df["gaia_distlim"]
print(df.shape)
del df["st_optmag"]
print(df.shape)
del df["st_optmagerr"]
print(df.shape)
del df["st_optmaglim"]
print(df.shape)
del df["st_optband"]
print(df.shape)
del df["gaia_gmag"]
print(df.shape)
del df["gaia_gmagerr"]
print(df.shape)
del df["gaia_gmaglim"]
print(df.shape)
del df["st_tefferr1"]
print(df.shape)
del df["st_tefferr2"]
print(df.shape)
del df["st_tefflim"]
print(df.shape)
del df["st_masserr1"]
print(df.shape)
del df["st_masserr2"]
print(df.shape)
del df["st_masslim"]
print(df.shape)
del df["st_raderr1"]
print(df.shape)
del df["st_raderr2"]
print(df.shape)
del df["st_radlim"]
print(df.shape)
del df["rowupdate"]
print(df.shape)
del df["pl_facility"]
print(df.shape)

