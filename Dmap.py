import requests
import os
import config
import wl


if config.initClear == True:
    os.system("clear")

if config.banner == True:
    os.system("figlet Dmap")
    print("by voidh7")
    print(f"vertion:{config.vertion}")
    print("-----------------")
else:
    print("DMAP by voidh7")
    print(f"vertion {config.vertion}")
    print("-----------------")

url = input("what is the url:")


if config.outputFile == True:
    outputFilename = input("output fileName:")
    open(outputFilename,"w").close()
    with open(outputFilename,"a") as file:
        file.write(f" \n BY DMAP {config.vertion} \n ")



for i in range(len(wl.wordlist)):
    getUrl = f"{url}{wl.wordlist[i]}"
    try:
        response = requests.get(getUrl, timeout=config.timeout)

        if response.status_code == 200:
            print(f"{getUrl} [open status code 200]")
            with open(outputFilename,"a") as file:
                file.write(f"{getUrl} [open status code 200]\n")
        else:
            if config.verbose == True:
                print(f"{getUrl} {response.status_code}")
            else:
                print("[;-;] error")

    except requests.exceptions.RequestException:
        print(f"{getUrl} → erro ou timeout")


