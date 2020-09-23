 #!/usr/bin/python
import yaml
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
      i=0
      with open('../data.yml') as f:
          doc = yaml.load(f,Loader=yaml.FullLoader)
          for user in doc['users']:
            print(user)
            i=i+1
            if user['name'] == username:
              break
      return i,doc

i,doc = getUserPositioninYaml('sysman')
print(i)

call_with_args = "bash ./exportconfiguration.sh '%s' '%s' '%s' '%s'" % ('1.1.1.1','testuser','test','running-config-old.xml')
print(call_with_args)
subprocess.call(call_with_args,shell=True)
#time.sleep(3) # wait for the API call to complete.

testuserpass= getUserPhash('running-config-old.xml','testuser')
print("Password is  "+testuserpass)
#doc['users'][i-1]['phash'] = testuserpass
 
with open('../data.yml','w') as f:
# doc1 = yaml.load(f)
  doc['users'][i-1]['phash'] = testuserpass
  yaml.dump(doc,f,default_flow_style=False)
