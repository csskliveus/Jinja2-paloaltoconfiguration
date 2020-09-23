#!/usr/bin/env bash
#-----------------------------------------------------------------

## Precondition:  To run this script, xmllint needs to be deployed'
# sudo apt install libxml2-utils

# Parameters:
# serverip or fqdn
# apikey
# new config file

# Todo : Enable API in palo-alto using CLI ?
#-----------------------------------------------------------------

#dateformat1='date +%m-%d-%Y'
#echo $dateformat1
$1, $2 , $3, $4
serverip=$1
username=$2
password=$3
file_name=$4
# name the backup config file

#file_name="running-config-"`date +"%Y-%m-%d"`".xml"

# delete if the same file exists
# if [ -f "$file_name" ]; then
#         echo "$file_name exists.So remove file."
#         rm $file_name
# fi

echo "----------------Get API key for the new palo-alto set up ------------------------"

curl -k -X GET "https://$serverip/api/?type=keygen&user=$username&password=$password" > apikeyconfig.xml

apikey=$(xmllint --xpath "string(//response//key)" apikeyconfig.xml)

rm ./apikeyconfig.xml
echo ''
echo ''
echo "----Taking back up of existing configuration file---------------------------------"

# export running-config from the server
curl -kG -H "X-PAN-KEY:$apikey" "https://$serverip/api/?type=export&category=configuration" > "./$file_name"

echo "-------Backup is completed. Please check file $file_name----------------------------"
echo ''
echo ''
echo "-------Import new configuration file ---------------------------------------------"
