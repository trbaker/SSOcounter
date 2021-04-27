# IMPORTS and VARS DEFINED
import requests as r
import pandas as pd
from urllib.parse import urlparse  # used for hive detection
from arcgis.gis import GIS # used for hive detection
counter = 1
counter_MS=0
counter_GOO=0
counter_OK = 0
counter_RI = 0
counter_CL = 0
counter_CA = 0
counter_UNK = 0

print('In testing, this script takes about 15 minutes to run 5000 URLs, during off-peak AGO hours.')
print('Upload a file named: datain.csv with data only in first col, listing AGO org URL prefixes.')
print('AGO with SSO enabled will list below in a comma-seperated dump. Total count at bottom.')

df = pd.read_csv('datain.csv')

print(' ')
print('count, url, SSO brand, analysis server, AGO version')
for index, row in df.iterrows():
    response = r.get("https://" + row[0] + ".maps.arcgis.com/sharing/rest/oauth2/authorize?client_id=arcgisonline&redirect_uri=https://fakeorg.maps.arcgis.com/home/postsignin.html&showSocialLogins=false&hideEnterpriseLogins=false&response_type=token")
    content = response.text
    startPositionInContent = content.find("idpName")
    if startPositionInContent != -1:
        print(counter, ',', row[0] + ".maps.arcgis.com,", sep="", end="")
        response2 = r.get("https://" + row[0] + ".maps.arcgis.com/sharing/rest/oauth2/saml/authorize?client_id=arcgisonline&redirect_uri=https://fakeorg.maps.arcgis.com/home/postsignin.html&showSocialLogins=false&hideEnterpriseLogins=false&response_type=token")
        if response2.history:
            workable = response2.url.split('/')[2] + '/' + response2.url.split('/')[3]
            # SSO detection logic
            if 'adfs' in workable or 'microsoft' in workable:
                print ('Microsoft,', sep="", end="")
                counter_MS = counter_MS+1
            elif 'google' in workable:
                print ('Google,', sep="", end="")
                counter_GOO = counter_GOO +1
            elif 'okta' in workable:
                print ('Okta,', sep="", end="")
                counter_OK = counter_OK+1
            elif '/idp' in workable:
                print ('RapidIdentity,', sep="", end="")
                counter_RI = counter_RI +1
            elif 'classlink' in workable:
                print ('ClassLink,', sep="", end="")
                counter_CL = counter_CL +1
            elif 'idaptive' in workable:
                print ('CyberArk,', sep="", end="")
                counter_CA = counter_CA +1
            else:
                print('SSO:',workable,',',sep="", end="")
                counter_UNK = counter_UNK +1
        else:
            print('SSO:NA ', sep="", end="")  # this forces a newline when the SSO detection logic doesn't return anything
        #insert hive code here
        try:
            gis = GIS("https://" + row[0] + ".maps.arcgis.com")
            flyr_list = gis.content.search(query="*", item_type="Feature Layer")
            flyr_item = flyr_list[0]
            flyr = flyr_item.layers[0]
            hive_inferred = urlparse(flyr.url).netloc
            print(hive_inferred,',', sep="", end="")
            vers = str(gis.version).replace(',','.')
            vers = vers.replace(" ", "")[1:4]
            print(vers)
        except:
            print('Analysis server: NA',',', sep="", end="")
            print('AGO version: NA')
        #general org counter
        counter = counter + 1

print(' ')
print(' -----  ')
print(" AGO orgs with SSO enabled: ", counter)
print('  - Microsoft: ', counter_MS)
print('  - Google: ', counter_GOO)
print('  - Okta: ', counter_OK)
print('  - RapidIdentity: ', counter_RI)
print('  - ClassLink: ', counter_CL)
print('  - CyberArk: ', counter_CA)
print('  - Unknown/Unresponsive: ', counter_UNK)
print(' -----  ')
print(' ')