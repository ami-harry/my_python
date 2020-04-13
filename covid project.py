from plyer import notification
import requests

def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="/home/harry/PycharmProjects/first/ck.jpg",
        )

"""def getdata(url):
    r = requests.get(url)
    return r.text"""

if __name__ == '__main__':
         notifyMe("harry", "lets stop the spread of this virus together")
         # myHtmldata = getdata('https://www.mohfw.gov.in')
         # print(myHtmldata)