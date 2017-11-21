# Internet-Connection-CSV-Logger
Created in November 2017

If your internet drops out regularly it can be handy to have evidence to show your ISP.  
This python script will run every 30 seconds, try and connect to Google and if it 
fails, it will add the date and time of the failure to a CSV file for proof.

Latest source : https://github.com/therealrobster/Internet-Connection-CSV-Logger
license : https://github.com/therealrobster/Internet-Connection-CSV-Logger/blob/master/LICENSE

You will need python installed.
If python is ready, to run load your command line and type:

python connectionLogger.py

This will start the script.  If a dropout is determined it will create a CSV file in the same folder.
If you interrupt (stop) the script (with CTRL V for example) it will simply append to the file later when you run it again.  It won't delete the existing file.

Enjoy, any feedback or questions to the github page please.
