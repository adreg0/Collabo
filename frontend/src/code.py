import json 
import requests
import os

organisation="amfoss"
i=1
repos=[]
while True:
	
	req=requests.get('https://api.github.com/users/'+organisation+'/repos?page='+str(i))
	if not req.json():
		break	
	i+=1
	for repo in req.json():
		repos.append(repo["name"])
with open("repos.json", "w") as outfile: 
	json.dump(repos, outfile) 
	
print(repos)
# import requests
# import os
# organisation="amfoss"
# i=1
# repos=[]
# while True:
# 	req=requests.get('https://api.github.com/users/bitergia/repos')
# 	if not req.json():
# 		break	
# 	i+=1
# 	for repo in req.json():
# 		print(repo)
# with open("sample.json", "w") as outfile: 
# 		json.dump({"name":repos}, outfile) 
	# with open("sample.json", "w") as outfile: 
    # 		json.dump(req.json, outfile)
# 	json_object = json.dumps(req.json, indent = 4) 

# with open("sample.json", "w") as outfile: 
#     outfile.write(json_object) 
	
		
		
  	
# # for i in range(0,len(repos)):
# # 	os.system("perceval git --json-line https://github.com/"+organisation+"/"+repos[i]+">> commits.json")

  
  
# Data to be written 
# dictionary ={ 
#     "name" : "sathiyajith", 
#     "rollno" : 56, 
#     "cgpa" : 8.6, 
#     "phonenumber" : "9976770500"
# } 
  
