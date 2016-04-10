import os,pdb,smtplib,time,mimetypes
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage

COMMASPACE = ','
SONG_PATH = r''
RECORD_FILE = ''
PIC_PATH  = ''
CC = []
TO = []
ME = ''
SMTP_SERVER = 'smtp.126.com'
USER = ''
PASS = ''

def constructAddr(addrList):
    return COMMASPACE.join(addrList)

def willChooseThisMedia(media, path):
    fp = open(path + RECORD_FILE, 'r')
    shareInfo = fp.read()
    fp.close()

    shareInfoList = shareInfo.split('\n')

    if media not in shareInfoList:
        fp = open(path + RECORD_FILE, 'a')
        fp.write(media + '\n')
        fp.close()
        return True
    else:
        return False

def getTodayMedia(path):
    mediaList = os.listdir(path)

    for media in mediaList:
        if False == os.path.isfile(path + media):
            continue
        else:
            if (media.endswith('mp3') or media.lower().endswith('jpg')) and\
                willChooseThisMedia(media, path):
                return media

def getMIMEImage(pic):
    fp = open(PIC_PATH + pic, 'rb')
    imageType = mimetypes.guess_type(PIC_PATH + pic)
    image = MIMEImage(fp.read(),imageType[0].split('/')[1])
    fp.close()
    image.add_header('Content-Disposition', 'attachment')
    image.set_param('filename', pic, header = 'Content-Disposition', charset = 'gb2312')

    return image

def getMIMEAudio(song):
    fp = open(SONG_PATH + song, 'rb')
    audioType = mimetypes.guess_type(SONG_PATH + song)
    audio = MIMEAudio(fp.read(),audioType[0].split('/')[1])
    fp.close()
    audio.add_header('Content-Disposition', 'attachment')
    audio.set_param('filename', song, header = 'Content-Disposition', charset = 'gb2312')

    return audio

def constructMail():
    mail = MIMEMultipart()

    song = getTodayMedia(SONG_PATH)
    pic  = getTodayMedia(PIC_PATH)

    mailSubject = Header('今日分享 | ' + song, 'utf-8')
    mailDate = Header(time.ctime())

    mail['subject'] = mailSubject
    mail['date'] = mailDate
    mail['to'] = constructAddr(TO)
    mail['cc'] = constructAddr(CC)
    mail['from'] = ME

    mailBody = MIMEText(song, _charset='gb2312')
    mail.attach(mailBody)
    mail.attach(getMIMEAudio(song))
    mail.attach(getMIMEImage(pic))
    return mail

def sendMail():
    session = smtplib.SMTP(SMTP_SERVER)
    session.login(USER,PASS)
    mail = constructMail()
    session.sendmail(ME, constructAddr(TO), mail.as_string())
    session.quit()

sendMail()