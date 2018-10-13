<!---- variable defs ----->
    <cfset myOutput ="">
    <cfset CrLf = Chr(13)>
    <cfset spitfire="Org_URL,Status,=SUM(C2:C25000)">

<cfsetting requestTimeOut="1300">
    
<!--- read in current file list ---->
<cfspreadsheet 
    action="read"
    src = "data_in/data.xlsx"
    columns = "1" 
    query = "myData"
    sheet = "1"
>
    
    <!---- convert array to list ---->
    <cfoutput> 
        <cfset targetLoop = ValueList(myData.col_1)>
        <!---- test output with:  #myList#  ---->
    </cfoutput>


<!--- Build the target URL ----->
<cfloop list=#targetLoop# index="targetLoop">
<cfset target="https://" & #targetLoop# & ".maps.arcgis.com/sharing/rest/oauth2/saml/signin">
    
<CFHTTP
    URL = "#target#"
    resolveurl = 0
    throwonerror = no
>
</CFHTTP>

<CFLOOP collection=#CFHTTP.RESPONSEHEADER# item="httpHeader">
    <CFSET value = CFHTTP.RESPONSEHEADER[httpHeader]>
    <CFIF IsSimpleValue(value)>
        <CFOUTPUT>
            <cfif value IS 746>
                <!---- CONFIRMED:  #httpheader# (#value#) is 746 ---->
                <cfset outputData="SSO">
                <cfset token=1>
            <cfelseif value GT 750>
                <cfset outputData="">
                <cfset token=0>
            <cfelse>
                <cfset outputData="Failed">
                <cfset token="">
            </cfif>
                
        </CFOUTPUT>   
    </CFIF>
</CFLOOP>
 

<cfsavecontent variable="spitfire_append">
<cfoutput>#trim(targetLoop)#, #outputData#, #token#</cfoutput>
</cfsavecontent>
<cfoutput>
<cfset spitfire = #trim(spitfire)# & #CrLf# & #trim(spitfire_append)#>
    </cfoutput>
</CFLOOP>


                        
<!---- output new Excel file ----->
<cfoutput>
    <cfset myDate = #Dateformat(now(), 'yyyymmdd')#>
    <cfset myFilename = "<fullpath_here>/SSOcheck/" & myDate & "_data.csv">
<cffile action="write" file ="#myFilename#" output="#spitfire#" fixnewline = "yes">
<hr>Script complete.
</cfoutput>
                    
                    
                    
                    