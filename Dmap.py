import requests
import os
import config                                                                           import wl
import sys

allowed_status = [200, 201, 202, 204, 301, 302, 307, 308]                               
status_desc = {
    200: "[Ok]",                                                                            201: "[Created]",
    202: "[Accepted]",
    204: "[No Content]",                                                                    301: "[Redirect]",
    302: "[Redirect]",
    307: "[Redirect]",                                                                      308: "[Redirect]",
    401: "[Unauthorized]",
    403: "[Forbidden]",
    404: "[Not Found]",                                                                     500: "[Server Error]",
    502: "[Bad Gateway]",
    503: "[Service Unavailable]",
    504: "[Gateway Timeout]"                                                            }

if config.initClear:
    os.system("clear")

if config.banner:
    os.system("figlet Dmap")
    print("by voidh7")
    print(f"vertion:{config.vertion}")
    print("-----------------")
else:
    print("DMAP by voidh7")
    print(f"vertion {config.vertion}")
    print("-----------------")

url = sys.argv[1]

if config.outputFile:
    outputFilename = input("output fileName:")
    open(outputFilename, "w").close()
    with open(outputFilename, "a") as file:
        file.write(f"\nBY DMAP {config.vertion}\n")

for i in range(len(wl.wordlist)):
    getUrl = f"{url}{wl.wordlist[i]}"
    try:
        response = requests.get(getUrl, timeout=config.timeout)
        code = response.status_code
        desc = status_desc.get(code, "[Unknown]")

        if code in allowed_status:
            print(f"{getUrl} [open status code {code}] {desc}")
            if config.outputFile:
                with open(outputFilename, "a") as file:
                    file.write(f"{getUrl} [open status code {code}] {desc}\n")
        else:
            if config.verbose:
                print(f"{getUrl} {desc}")
            else:
                print("[;-;] error")

    except requests.exceptions.RequestException:
        print(f"{getUrl} → erro ou timeout")