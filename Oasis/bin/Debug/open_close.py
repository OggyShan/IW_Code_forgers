from AppOpener import open as opn
from AppOpener import  mklist, close 
import json
app_cdata=mklist(name="install_apps.json")
app_list=[]
with open('install_apps.json', 'r') as app_data:
    app_data= json.load(app_data)
for app in app_data:
    app_list.append(app)

def open_app(appname):
    try:
        opn(appname, match_closest=True)
        return f"{appname}"
    except:
        return "Can not open that app!!! please try again...."

    

    


 