# 🗺️ Dmap - Directory Mapper

**Version:** 1.0.0 beta  
**Author:** voidh7  

---

## 🔹 Description
**Dmap** is a lightweight Python tool for discovering common admin panels, login pages, and sensitive paths on a web server. It’s ideal for **ethical hacking**, security testing, or penetration testing in **controlled environments** (labs or systems you own).  

> ⚠️ **Warning:** Use only on sites you have explicit permission to test. Unauthorized scanning is illegal.

---

## 🔹 Features
- Scan for popular admin and sensitive paths:
  - `/admin`, `/login`, `/cpainel`, `/upload`, `/phpinfo.php`, etc.
- Detect accessible URLs (HTTP status code 200)
- Optional **verbose mode** to display all HTTP responses
- Optional **screen clearing** at startup
- Simple, clean output for quick results

---

## 🔹 Requirements
- Python 3.x
- `requests` library:  
  pip install requests
- Optional: `figlet` (for ASCII banner)  
  sudo apt install figlet

---

## 🔹 Configuration
Create a file named `config.py`:

verbose = False   # True = display all HTTP responses

initClear = False # True = clear the terminal at startup

banner = True # Change to false in case you want to download figlet

outputFile = True # If true, all the program’s positive output will be saved in a .txt file

timeout = 3# limit time for wensite response Change to 3 for a faster scan (you might miss some endpoints)
---

## 🔹 Usage
1. Run the script:  
   python Dmap.py
2. Enter the target URL:  
   what is the url: http://example.com
3. The tool will check each path from the wordlist and display:  
   - `[URL] [open status code 200] [OK` → Accessible  
   - `[URL] [not found]` → Inaccessible (or verbose details if enabled)

---

## 🔹 Wordlist (Default)
/admin
/xp-admin
/administrator
/cpainel
/maneger/html
/login
/signin
/reset-password
/upload
/files
/media
/images
/config
/bug
/debug
/phpinfo.php
/db
/database
/sql

---

## 🔹 Example Output
$ python Dmap.py
what is the url: http://example.com
http://example.com/admin [open status code 200]
[;-;] error
http://example.com/login [open status code 200]
...

---

## 🔹 License
This project is free to use for **educational purposes**. Refer to ethical hacking guidelines in your region. 
