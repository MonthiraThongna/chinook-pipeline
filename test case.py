# Databricks notebook source
import pandas as pd
from datetime import datetime

# file path
inputpath = "/Workspace/Users/monthira.t@ppp.co.th/track_small.csv"
outputpath = "/Workspace/Users/monthira.t@ppp.co.th/output_small.csv"
testresultpath = "/Workspace/Users/monthira.t@ppp.co.th/test_result.txt"

# open test result
f = open(testresultpath, "w")

# read csv file
tracksinput = pd.read_csv(inputpath)
tracksoutput = pd.read_csv(outputpath)

# case 1
if tracksoutput.dtypes["UnitPrice"] == 'int64':
    f.write("Case 1: Passed\n")
else:
    f.write("Case 1: Failed\n")

# case 2
mergedtracks = tracksinput.merge(tracksoutput, on='TrackId', suffixes=("_input","_output"))
if (mergedtracks['UnitPrice_output'] - mergedtracks['UnitPrice_input'] < 1).all:
    f.write("Case 2: Passed\n")
else:
    f.write("Case 2: Failed\n")

# close
f.close()

# COMMAND ----------


