# SSO_Counter

**Added python file with IdP brand, hive/analysis server URL, and gis version number.  Full URLs will list next to the found IdP brand (e.g. Okta, ASDF/MS, Google, more). Outputs to a comma-seperated screen dump for easy move to spreadsheet.


**Added April 25: Google Collaboratory version (file: SSOcounter-2-collaboratory.ipynb). Upload the CSV (with org names) directly into the running script and org with SSO output to screen, rather than file.


**The original Jupyter Notebook version follows:
Determines if an ArcGIS Online org is using SSO and creates a tally from a supplied list of AGO URL prefixes. 

In the Python3 version of this script, place the Jupyter or .py file in any directory. In that directory, create a data folder for the input file datain.csv and the script-generated output dataout.txt.


**In the ColdFusion version (file: index.cfm):
In the ColdFusion version of this script, you'll need to add a full path at about line 69. I run this script froma CF Developer edition server as needed, giving me full access to cffile, cfhttp, etc.


