import requests
import os
import config                                                         import wl

                                                                      
if config.initClear == True:
    os.system("clear")

if config.banner == True:                                                 os.system("figlet Dmap")
    print("by voidh7")
    print(f"vertion:{config.vertion}")                                    print("-----------------")
else:
    print("DMAP by voidh7")
    print(f"vertion {config.vertion}")
    print("-----------------")                                        

url = input("what is the url:")                                       

for i in range(len(wl.wordlist)):
   i+=1

   getUrl = f"{url}{wl.wordlist[i]}"
   response = requests.get(getUrl)

   if response.status_code == 200:
      print(f"{getUrl} [open status code 200]")

   else:
        if config.verbose == True:
            print(f"{getUrl} {response.status_code}")
        else:
            print("[;-;] error ") 