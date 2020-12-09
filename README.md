# Automatic Ripping Machine (ARM)

There are new config parameters so review the new arm.yaml file

Make sure the 'arm' user has write permissions to the db directory (see your arm.yaml file for locaton). is writeable by the arm user.  A db will be created when you first run ARM.

Make sure that your rules file is properly **copied** instead of linked:
```
sudo rm /usr/lib/udev/rules.d/51-automedia.rules
sudo cp /opt/arm/setup/51-automedia.rules /etc/udev/rules.d/
```
Otherwise you may not get the auto-launching of ARM when a disc is inserted behavior
on Ubuntu 20.04.

Please log any issues you find.  Don't forget to run in DEBUG mode if you need to submit an issue (and log files).  Also, please note that you are running 2.2_dev in your issue.

You will also need to visit your http://WEBSERVER_IP:WEBSERVER_PORT/setup  
							&#x26A0; &#x26A0; **!!!WARNING!!!** &#x26A0; &#x26A0;  					

Visiting this page will delete your current database and create a new db file. You WILL lose jobs/tracks/etc from your database
This will setup the new database, and ask you to make an admin account. Because of the changes to the armui its not possible to view/change/delete entries without logging in. 
Due to these large number of changes to the database its not currently possible to upgrade without creating a new database


## Overview

Insert an optical disc (Blu-Ray, DVD, CD) and checks to see if it's audio, video (Movie or TV), or data, then rips it.

See: https://b3n.org/automatic-ripping-machine


## Features

- Detects insertion of disc using udev
- Auto downloads keys_hashed.txt and KEYDB.cfg using robobrowser and tinydownloader
- Determines disc type...
  - If video (Blu-Ray or DVD)
    - Retrieve title from disc or Windows Media MetaServices API to name the folder "movie title (year)" so that Plex or Emby can pick it up
    - Determine if video is Movie or TV using OMDb API
    - Rip using MakeMKV or HandBrake (can rip all features or main feature)
    - Eject disc and queue up Handbrake transcoding when done
    - Transcoding jobs are asynchronusly batched from ripping
    - Send notification when done via IFTTT or Pushbullet
  - If audio (CD) - rip using abcde
  - If data (Blu-Ray, DVD, or CD) - make an ISO backup
- Headless, designed to be run from a server
- Can rip from multiple-optical drives in parallel
- HTML UI to interact with ripping jobs, view logs, etc


## Requirements

- Ubuntu Server 18.04 (should work with other Linux distros) - Needs Multiverse and Universe repositories
- One or more optical drives to rip Blu-Rays, DVDs, and CDs
- Lots of drive space (I suggest using a NAS like FreeNAS) to store your movies

## Pre-Install (only if necessary)

If you have a new DVD drive that you haven't used before, some require setting the region before they can play anything.  Be aware most DVD players only let you change the region a handful (4 or 5?) of times then lockout any further changes.  If your region is already set or you have a region free DVD drive you can skip this step.

```bash
sudo apt-get install regionset
sudo regionset /dev/sr0
```

## Install

**Please use the setup script for Ubuntu **
**This MUST be run as root!**
 ```
 apt install wget
 wget https://raw.githubusercontent.com/1337-server/automatic-ripping-machine/v2.2_dev_ubuntu/scripts/ubuntu-20.04-install.sh
 chmod +x ubuntu-20.04-install.sh
 ./ubuntu-20.04-install.sh
 ```
 ```reboot``` 
 to complete installation.

## Intel QuickSync support 
I have added Intel QSV support for this branch only, Dont use this branch unless you want Intel quicksync for HandBrake 
**This MUST be run as root!**
 ```
 apt install wget
 wget https://raw.githubusercontent.com/1337-server/automatic-ripping-machine/v2.2_dev_ubuntu/scripts/ubuntu-quicksync.sh
 chmod +x ubuntu-quicksync.sh
 ./ubuntu-quicksync.sh
 ```
 ```reboot``` 
 to complete installation.


**Configure ARM**

- Edit your "config" file (located at /opt/arm/arm.yaml) to determine what options you'd like to use.  Pay special attention to the 'directory setup' section and make sure the 'arm' user has write access to wherever you define these directories.

- Edit the music config file (located at /home/arm/.abcde.conf)

- To rip Blu-Rays after the MakeMKV trial is up you will need to purchase a license key or while MakeMKV is in BETA you can get a free key (which you will need to update from time to time) here:  https://www.makemkv.com/forum2/viewtopic.php?f=5&t=1053 and create /home/arm/.MakeMKV/settings.conf with the contents:

        app_Key = "insertlicensekeyhere"

- For ARM to identify movie/tv titles register for an API key at OMDb API: http://www.omdbapi.com/apikey.aspx and set the OMDB_API_KEY parameter in the config file.

After setup is complete reboot...
    
    reboot
 
 **Details about this script**
 
 The script installs all dependencies, a service for the ARMui and the fstab entry for sr0, if you have more than one drive you will need to make the mount folder and insert any additional fstab entries.
 The attended installer will do all of the necessary installs and deal with dependencies but will need user input.

## Usage

- Insert disc
- Wait for disc to eject
- Repeat

## Troubleshooting

When a disc is inserted, udev rules should launch a script (scripts/arm_wrapper.sh) that will launch ARM.  Here are some basic troubleshooting steps:
- Look for empty.log.  
  - Everytime you eject the cdrom, an entry should be entered in empty.log like:
  ```
  [2018-08-05 11:39:45] INFO ARM: main.<module> Drive appears to be empty or is not ready.  Exiting ARM.
  ```
  - Empty.log should be in your logs directory as defined in your arm.yaml file.  If there is no empty.log file, or entries are not being entered when you eject the cdrom drive, then udev is not launching ARM correctly.  Check the instructions and make sure the symlink to 51-automedia.rules is set up right.  I've you've changed the link or the file contents you need to reload your udev rules with:
  ```
  sudo udevadm control --reload-rules 
  ```

- Sometimes running the following command can help track down what is stopping arm (remember to replace sr0 with the name of your own device) 
```
/usr/bin/python3 /opt/arm/arm/ripper/main.py -d sr0 | at now
```

- Check ARM log files 
  - The default location is /home/arm/logs/ (unless this is changed in your arm.yaml file) and is named after the dvd. These are very verbose.  You can filter them a little by piping the log through grep.  Something like 
  ```
  cat <logname> | grep ARM:
  ```  
    This will filter out the MakeMKV and HandBrake entries and only output the ARM log entries.
  - You can change the verbosity in the arm.yaml file.  DEBUG will give you more information about what ARM is trying to do.  Note: please run a rip in DEBUG mode if you want to post to an issue for assistance.  
  - Ideally, if you are going to post a log for help, please delete the log file, and re-run the disc in DEBUG mode.  This ensures we get the most information possible and don't have to parse the file for multiple rips.

If you need any help feel free to open an issue.  Please see the above note about posting a log.

## Contributing

Pull requests are welcome.  Please see the [Contributing Guide](./CONTRIBUTING.md)

If you set ARM up in a different environment (harware/OS/virtual/etc), please consider submitting a howto to the [wiki](https://github.com/automatic-ripping-machine/automatic-ripping-machine/wiki).

## License

[MIT License](LICENSE)
