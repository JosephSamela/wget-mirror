# wget-mirror
Host local self-updating webpage mirror with wget!

## Here's the situation. 
I need to mirror a remote webpage locally. Problem is - the webpage can be updated at any time, and the mirror needs to stay current. Here's my solution! Python script uses a tailored [wget](https://www.gnu.org/software/wget/) command to download mirrorized site, updating on 1hr intervals. I tried many flag combinations and this is what works best for a single page local mirror, see flag explainations below. In my environment `.` is pointed to the `htdocs` folder of my [Apache](https://httpd.apache.org/) webserver. Edit `mirror.py` with your domain and webserver directory of choice, then run!

```python
import os
import time

while True:
     # Grab latest mirror
     os.system("wget -E -H -k -K -nd -N -p -P . http://www.domain.com")
     # -E  =  Include suffix ‘.html’ to be appended to the local filename
     # -H  =  Enable spanning across hosts when doing recursive retrieving
     # -k  =  Convert links to make sutible for local viewing (javascript + css imports)
     # -K  =  Back up the original version with a ‘.orig’ suffix
     # -nd =  Enable "distruct" to overwrite old files
     # -N  =  If file exists locally and remote file is not newer, don't download
     # -p  =  Download just this single page and all its requisites
     # -P  =  Specify location to download site files, I use '.' to target current directory
     print("Mirror Updated! Waiting 1hr...")
     time.sleep(3600)
```

## Webpage require credentials?
If the webpage requires credentials - Try logging in first to recieve a user token, then use that subsequent retrievals.
```
--header "Authorization: Basic ac1zMDUzDFpJbnRltJhEYGAwMCA"
```
