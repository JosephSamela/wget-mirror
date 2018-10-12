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
     
