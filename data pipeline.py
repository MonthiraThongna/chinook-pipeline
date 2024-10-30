# Databricks notebook source
import pandas as pd
import math

# file path
inputpath = "/Workspace/Users/monthira.t@ppp.co.th/track_small.csv"
outputpath = "/Workspace/Users/monthira.t@ppp.co.th/output_small.csv"

# extract
tracks = pd.read_csv(inputpath)

# transform
tracks['UnitPrice'] = tracks['UnitPrice'].apply(lambda x: math.ceil(x))

# load
tracks.to_csv(outputpath, index=False)

# COMMAND ----------


