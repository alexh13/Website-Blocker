import time  
from datetime import datetime as dt  # short variable dt cause it is used so much later
# to run this you need to change every hosts_temp with the correct hosts_path, see comments below, must run as administrator

hosts_temp = "hosts"
hosts_path = r"/etc/hosts"  # Host file on a Mac or Linux based system
# host path for windows based system: hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1" 
websites_list = ["www.revzilla.com", "revzilla.com", "www.faceboook.com", "facebook.com"]  # list of websites to block

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          16):  # checks date and time 8 am - 4 pm
        print("Working hours.....")  
        with open(hosts_temp, 'r+') as file:
            content = file.read()  # read the text in host file
            for website in websites_list:
                if website in content:  # if website is in our host file we don't want to do anything during work hours
                    pass
                else:
                    file.write(redirect + " " + website + "\n")  # hosts require at least one space between IP address
                                                                 # and host name
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()  # loads text in our content variable of all the lines
            file.seek(0)  # places pointer just before first character of file content
            for line in content:  # start looping through the lines of content
                if not any(website in line for website in websites_list):  # if not any Site in that first line then:
                    file.write(line)  # write that Site in the line
                file.truncate()  # remove everything after new file is written
        print("Recreation hours...")  

    time.sleep(5)  # every 5 seconds

