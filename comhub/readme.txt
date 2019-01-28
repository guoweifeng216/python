1. Required packages:
python2
pyqt4
pyyaml
xmodem
pyserial
paramiko

2. Features:
1) support python2
2) support multi serial/SSH
3) support multi tabs
4) support port/text max line show in status bar
5) support log path/size show in status bar
6) support ctrl+o to open a dialog
7) support ctrl+w to close current session
8) support ctrl+r to resize the window
9) support ctrl+l to reload a log file
10) support ctrl+a to select all text in window
11) support ctrl+tab to switch the tabs
12) support select the text to copy
13) support mouse right click to paste (only the first line is valid)
14) support dialog/session history
15) support record log
16) support log size limit
17) support record time stamp begin of every line
18) support set text max line
19) support xmodem send file
20) support execute command before xmodem send (e.g. "dl fw")
21) support xmodem file history

3. Usage:
Server:
1) python main.py
2) ctrl+o to open a dialog
3) setup the serial and common, press ok
Client:
1) use SSH tool(xShell/secureCRT...) to connect this session

4. Q/A:
1) cannot connect to the server
--- please make sure the firewall is closed.
2) does this tool support python3/pyqt5?
--- Not yet, if you need, please let me know.

Enjoy!

Author: yyang
Email: yyang@cnexlabs.com
Skype: yangyingjun@outlook.com
