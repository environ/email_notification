kontroll_post.sh 
#!/bin/sh

ps auxw | grep post.py | grep -v grep > /dev/null

if [ $? != 0 ]
then
       sudo python -u /home/pi/email_notification/post.py &
fi