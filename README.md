# WeeNotifyMatrix
WeeNotifyMatrix is a Mac OS X plugin for Matrix, a chat protocol for WeeChat, a CLI chat client. 

WeeNotifyMatrix displays a Mac OS X notification whenever a message is received on any buffer you have on WeeChat.

![Alt text](/weeNotifyPic.png?raw=true "Script in Action")

# Instructions for Use:
  1. Make sure you have the following installed:
      * [WeeChat](https://weechat.org/files/doc/weechat_faq.en.html#compile_osx)
      * [Matrix](https://github.com/torhve/weechat-matrix-protocol-script/blob/master/README.md) 
      * [Terminal-Notifier](https://github.com/julienXX/terminal-notifier)
      
  2. Clone this repo:
  ```     
    git clone https://github.com/omart075/WeeNotifyMatrix.git    
  ``` 
  3. Move script to WeeChat's Python Directory:
  
  ```
    mv weeNotify.py ~/.weechat/python
  ```  
  4. Go into WeeChat's autoload directory for Python:
  
  ```
    cd ~/.weechat/python/autoload
  ```  
  5. Make a link to script from Weechat's Python dir to WeeChat's autoload dir:
  
  ```
    ln -s ../weeNotify.py
  ```
