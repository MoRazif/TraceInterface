## Simple API for Trace Interface : Analyzer Error (API Issue: Error) ##
## M.Razif 2018 ##

import re, os, sys, time, optparse, random, win32com.client

# Clear Command Line
os.system("cls")

# Open Communication with Lecroy Analyzer
Analyzer = win32com.client.Dispatch("Lecroy.SASAnalyzer")

# Error Summary Report
Trace = Analyzer.OpenFile("C:\Users\Public\Documents\LeCroy\SAS SATA Protocol Suite\Examples\Samples\NCQ-Write-Read.sts")

AnalyzerError = Trace.AnalyzerErrors()
print "Trigger Packet Number " + str(AnalyzerError)
time.sleep(1)

ClosingTrace = Trace.Close()

print "Closing Trace"
time.sleep(1)

os.system("TASKKILL /F /IM sas.exe")




