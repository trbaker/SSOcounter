# IMPORTS and VARS DEFINED
import requests as r
import csv
import io
import pandas as pd
counter = 0
temp = ""

print('In testing, this script takes about 15 minutes to run 5000 URLs, during off-peak AGO hours.')
print('Upload a file named: datain.csv with data only in first col, listing AGO org URL prefixs.')
print('  ')

df = pd.read_csv('datain.csv')

print(' ')
print('AGO orgs with SSO enabled will list below. Total count at bottom.')
print(' ')
for index, row in df.iterrows():
    try:
        response = r.get("https://" + row[
            0] + ".maps.arcgis.com/sharing/rest/oauth2/authorize?client_id=arcgisonline&redirect_uri=https://fakeorg.maps.arcgis.com/home/postsignin.html&showSocialLogins=false&hideEnterpriseLogins=false&response_type=token")
        content = response.text
        startPositionInContent = content.find("idpName")
        if startPositionInContent == -1:
            pass
        else:
            print(row[0] + ".maps.arcgis.com", " : ", idpName)
            counter = counter + 1
    except:
        continue

print(' -----  ')
print("Script complete. ", counter, " AGO orgs have SSO enabled.")