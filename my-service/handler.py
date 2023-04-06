import boto3
import yaml
client = boto3.client('iam')
with open('data.yaml') as f:
       data = yaml.load(f,Loader= yaml.FullLoader)

userlist = data['Users']

try:
    
  for users in userlist: 
        response = client.create_user(
        UserName=users
         )
        print(response)
        
except client.exceptions.EntityAlreadyExistsException:
        print ("This name users are already created") 
        
grouplist = data['GroupAssignment']     

try:  
    
  for groups in grouplist:
        group = client.create_group(
        GroupName=groups
         )
        print (group)
except client.exceptions.EntityAlreadyExistsException:
        print ("This name usergroups are already created") 
        
for groups in grouplist:
    for x in grouplist[groups]:
        usergroup = client.add_user_to_group(
            GroupName=groups,
            UserName=x
            )       
        print (usergroup)
