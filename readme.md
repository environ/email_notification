Add cron

sudo crontab -e

@reboot sudo python -u /home/pi/email_notification/post.py &
*/60 * * * * sudo /home/pi/email_notification/kontroll_post.sh


kontroll_post kontrollib, et teenus töötaks. kui ei tööta, siis taaskäivitab

