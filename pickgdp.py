# import os
# os.chdir('C:\\Users\\Mathew\\myStuff\\school\\sem14_Spring2016\\data-sci-case-comp')
# exec(open("pickgdp.py").read(), globals())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
import csv
import math

def summary_nonnulls(gdp_dict):
	to_list = gdp_dict.values.tolist()

	dict_by_indic = {}
	for row in to_list:
		indic = row[3]
		num_nans = pd.notnull(row[4:-1]).sum()
		if indic in dict_by_indic:
			dict_by_indic[indic].append(num_nans)
		else:
			dict_by_indic[indic] = [num_nans]

	for k in dict_by_indic.keys():
		non_nulls = pd.Series(dict_by_indic[k])
		print(k+": ")
		print(non_nulls.describe())


# Country Name,Country Code,Indicator Name,Indicator Code,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015

print( "hello")

print("Loading csv into data frame...")
df = pd.read_csv('WDI_csv/WDI_Data.csv')
print("Loading complete!")

gdps = df[ (df['Indicator Code']=='NY.GDY.TOTL.KD' )|(df['Indicator Code']=='NY.GDY.TOTL.KN' )|(df['Indicator Code']=='NY.GDS.TOTL.ZS' )|(df['Indicator Code']=='NY.GDS.TOTL.KN' )|(df['Indicator Code']=='NY.GDS.TOTL.CN' )|(df['Indicator Code']=='NY.GDS.TOTL.CD') ]

summary_nonnulls(gdps)

print("for LDC: ")

gdps_ldc = df[ ( (df['Indicator Code']=='NY.GDY.TOTL.KD' )|(df['Indicator Code']=='NY.GDY.TOTL.KN' )|(df['Indicator Code']=='NY.GDS.TOTL.ZS' )|(df['Indicator Code']=='NY.GDS.TOTL.KN' )|(df['Indicator Code']=='NY.GDS.TOTL.CN' )|(df['Indicator Code']=='NY.GDS.TOTL.CD') ) & (	(df['Country Code']=='AFG') | (df['Country Code']=='AGO') | (df['Country Code']=='BGD') | (df['Country Code']=='BEN') | (df['Country Code']=='BTN') | (df['Country Code']=='BFA') | (df['Country Code']=='BDI') | (df['Country Code']=='KHM') | (df['Country Code']=='CPV') | (df['Country Code']=='CAF') | (df['Country Code']=='TCD') | (df['Country Code']=='COM') | (df['Country Code']=='COD') | (df['Country Code']=='DJI') | (df['Country Code']=='GNQ') | (df['Country Code']=='ERI') | (df['Country Code']=='ETH') | (df['Country Code']=='GMB') | (df['Country Code']=='GIN') | (df['Country Code']=='GNB') | (df['Country Code']=='HTI') | (df['Country Code']=='KIR') | (df['Country Code']=='LAO') | (df['Country Code']=='LSO') | (df['Country Code']=='LBR') | (df['Country Code']=='MDG') | (df['Country Code']=='MWI') | (df['Country Code']=='MDV') | (df['Country Code']=='MLI') | (df['Country Code']=='MRT') | (df['Country Code']=='MOZ') | (df['Country Code']=='MMR') | (df['Country Code']=='NPL') | (df['Country Code']=='NER') | (df['Country Code']=='RWA') | (df['Country Code']=='WSM') | (df['Country Code']=='STP') | (df['Country Code']=='SEN') | (df['Country Code']=='SLE') | (df['Country Code']=='SLB') | (df['Country Code']=='SOM') | (df['Country Code']=='SDN') | (df['Country Code']=='TZA') | (df['Country Code']=='TLS') | (df['Country Code']=='TGO') | (df['Country Code']=='TUV') | (df['Country Code']=='UGA') | (df['Country Code']=='VUT') | (df['Country Code']=='YEM') | (df['Country Code']=='ZMB') ) ]

summary_nonnulls(gdps_ldc)


