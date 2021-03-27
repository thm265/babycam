# Babycam Repository
This is a repository for a babycam using RaspberryPi and webcam with Python Django backend.

## Dependencies Installation for Development
Use *pip install -r requirements.txt* to install dependencies

## Some Youtube Tutorials
1. https://www.youtube.com/watch?v=NufWIkVQT44&list=WL&index=1
2. https://www.youtube.com/watch?v=-oQvMHpKkms&t=2s

## Installation process
See https://github.com/codingforentrepreneurs/Guides/blob/master/all/DjangoPiNetworkServerGuide.md

### Get IP Address of the Pi

1. Turn Raspberry Pi on and ensure microSD card is inserted that contians the Raspbian Jessie Linux Operating System (above setup).

2. Connect USB Keyboard, USB Mouse, and Monitor (through HDMI)

3. Connect Raspberry Pi to Internet on your local network :
    - via Wifi (look for wlan0 below)
    - via Ethernet (look for eth0 below)

4. Open up `Terminal` and type `ifconfig`. You should see the following result:

    ```
    eth0      Link encap:Ethernet  HWaddr b8:27:eb:49:e9:1d  
              inet6 addr: fe80::20f:eaff:fe91:407/64 Scope:Link
              UP BROADCAST MULTICAST  MTU:1500  Metric:1
              RX packets:0 errors:0 dropped:0 overruns:0 frame:0
              TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)

    lo        Link encap:Local Loopback  
              inet addr:127.0.0.1  Mask:255.0.0.0
              inet6 addr: ::1/128 Scope:Host
              UP LOOPBACK RUNNING  MTU:65536  Metric:1
              RX packets:532 errors:0 dropped:0 overruns:0 frame:0
              TX packets:532 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1 
              RX bytes:42256 (41.2 KiB)  TX bytes:42256 (41.2 KiB)

    wlan0     Link encap:Ethernet  HWaddr b8:27:eb:1c:bc:48  
              inet addr:192.168.0.10  Bcast:192.168.0.255  Mask:255.255.255.0
              inet6 addr: fe80::20f:eaff:fe91:407/64 Scope:Link
              inet6 addr: 2715:e000:3098:a900:c338:7e68:77c2:d3ce/64 Scope:Global
              UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
              RX packets:11842 errors:0 dropped:854 overruns:0 frame:0
              TX packets:8365 errors:0 dropped:0 overruns:0 carrier:0
              collisions:0 txqueuelen:1000 
              RX bytes:11994051 (11.4 MiB)  TX bytes:1072259 (1.0 MiB)

    ```
    You'll need to find this line `inet addr:192.168.0.10  Bcast:192.168.0.255  Mask:255.255.255.0`

    The numbers `192.168.0.10` are your IP Address (`<ip>`)

5. SSH into your Pi with `ssh pi@<ip>`:

    Mac/Linux Users (non-Pi linux):
    
    1. Open Open Terminal
    2. type `ssh pi@192.168.0.10`
    3. Accept warning about fingerprint authenticity (if any)
    4. Default password is `raspberry`
    5. You're in!
    
    
    Windows Users:
    
    1. Download & Install [PuTTY](http://www.putty.org/)
    2. Open PuTTY
    3. type `ssh pi@192.168.0.10` 
    4. Accept warning about fingerprint authenticity (if any)
    5. Default password is `raspberry`
    6. You're In!



### Apache2 + Django


Update Software:

```
sudo apt-get update
sudo apt-get upgrade
```

Install Apache2:

```
sudo apt-get install apache2 -y

sudo apt-get install libapache2-mod-wsgi-py3

sudo apt-get install libapache2-mod-wsgi # if using Python2
```

Install Pip & Django:

```
sudo apt-get install python-setuptools python-dev build-essential

sudo easy_install pip 

sudo pip install django==X.Y.Z #where X.Y.Z is the version number

sudo pip install django==1.10.3

sudo pip install virtualenv 

```

Start Django Project:
```
cd ~/

mkdir Dev && cd Dev

mkdir cfehome && cd cfehome

virtualenv -p python3 .

source bin/activate

pip install django==1.10.3

django-admin.py startproject cfehome

mv /home/pi/Dev/cfehome/cfehome /home/pi/Dev/cfehome/src
```

Apache2 Settings:

```
sudo nano /etc/apache2/sites-available/000-default.conf
```
Note: If errors happen with below, just do the following and it will re-install apache:

```
sudo apt-get purge apache2 # removes apache2

sudo apt-get install apache2 -y # reinstalls it

```

```     
<VirtualHost *:80>
    ServerName www.example.com

    ServerAdmin webmaster@localhost

    Alias /static /home/pi/Dev/cfehome/static
        <Directory /home/pi/Dev/cfehome/static>
           Require all granted
         </Directory>

    <Directory /home/pi/Dev/cfehome/src/cfehome>
        <Files wsgi.py>
            Require all granted
        </Files>
    </Directory>

    WSGIDaemonProcess cfehome python-path=/home/pi/Dev/cfehome/src:/home/pi/Dev/cfehome/lib/python2.7/site-packages
    WSGIProcessGroup cfehome
    WSGIScriptAlias / /home/pi/Dev/cfehome/src/cfehome/wsgi.py


    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>

```

Restart Apache:

```
# Restart in two ways:
sudo apachectl restart
sudo service apache2 restart


# Start Apache in two ways:
sudo apachectl start
sudo service apache2 start

# Stop Apache in two ways:
sudo apachectl stop
sudo service apache2 stop
```

Set Ownership of Database to Pi user for Django
```
sudo adduser $USER www-data
sudo chown www-data:www-data /home/$USER/Dev/cfehome    
sudo chown www-data:www-data /home/$USER/Dev/cfehome/src/db.sqlite3
sudo chmod -R 775 ~/Dev/cfehome

# if above fails, try (thanks Mike!):
sudo chown -R www-data:www-data ~/Dev/cfehome
sudo chown www-data:www-data /home/pi/Dev/cfehome/src
# or if a new project
sudo chown -R www-data:www-data ~/Dev/<your-virtuaenv-name>
sudo chown www-data:www-data /home/pi/Dev/<your-virtuaenv-name>/src/
```

Enabling module wsgi
```
sudo a2enmod wsgi
```