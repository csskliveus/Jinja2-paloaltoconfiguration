import yaml, datetime
import xml.etree.ElementTree as ET 
import subprocess, shlex
from datetime import date

# today = date.today()
# d1 = today.strftime("%d-%m-%Y")
# filename = "running-config-"+str(d1)+".xml"

def getUserPhash(xmlfile,username):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    phashvalue = root.find("mgt-config/users/*[@name='"+username+"']/phash")   
    return phashvalue.text.__str__()

def getUserPositioninYaml(username):
        with open('../data.yml') as f:
                doc = yaml.load(f,Loader=yaml.FullLoader)
#existingVal = doc['users'][0]['phash']
        i=0
        for user in doc['users']:
                print(user)
                i=i+1
                if user['name'] == username: 
                        break
        return i


i = getUserPositioninYaml('sysman')            
print(i)


subprocess.call(shlex.split('../exportconfiguration.sh 52.156.70.150 testuser testP@ssw0rd running-config-old.xml'))
time.sleep(3) # wait for the API call to complete.


testuserpass= getUserPhash(filename,'testuser')
print("Password is  "+testuserpass)
doc['users'][i-1]['phash'] = testuserpass

with open('../data1.yml','w') as f:
  yaml.dump(doc,f,default_flow_style=False)




# to call shell script from the code

# import subprocess
# import shlex
# subprocess.call(shlex.split('./test.sh param1 param2'))

    



