# LRRP DECODER
This script is a simple decoder for the lrrp geolocation data transmitted via DMR radio. This script parses the output of the command `DSDPlus` and make a `map.html` that contains a dinamic map with markers on all extracted positions.  

## Usage

To correctly use this script you will need [Python](https://www.python.org/), [DSDPlus](https://www.dsdplus.com/download-2/) and a `.waw` file of a DRM comunication that contains LRRP data and that can be recorded using an SDR interface using a software like [SDR#](https://airspy.com/download/).  
To save the output of DSDPlus you can make a `.bat` file like this:
    
    @echo off
    DSDPlus.exe -E -v4 communication.waw > logfile.txt
note that the `-v4` level of verbosity is required.  

## Disclaimer

Please note that this script will work only with a particular model of radio that is not included for security reasons.