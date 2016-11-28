from api import StreamClient, ObjCode, AtTaskObject
import getpass
from Tkinter import *


#Global Variables
username = 'username'
password = 'password'
carrieridlist = 'carrieridlist'
periodid = '0'
taskname = 'taskname'
Builder = 'Builder'
projIDlist = []
taskIDlist = []
assignIDlist = []
client = StreamClient('https://entersubdomainhere.attask-ondemand.com/attask/api/')


#start TKinter build#
root = Tk()
root.resizable(width=False, height=False)

mainframe = Frame(root)
mainframe.pack()

photo = PhotoImage(file="broadsword.gif")
test = Label(mainframe, image=photo, bd=5)
test.image = photo
test.grid(column=0,row=0, columnspan=2)

unL = Label(mainframe, text='Batch edit WF assignments | Written by BE')
unL.grid(column=0, row=1, columnspan=2)

unL = Label(mainframe, text='User Name: ')
unL.grid(column=0, row=2)
unE = Entry(mainframe, bd=5,width=30)
unE.grid(column=1, row=2)

passL = Label(mainframe, text='Password: ')
passL.grid(column=0,row=3)
passE = Entry(mainframe, bd=5, show='*',width=30)
passE.grid(column=1,row=3)

periodL = Label(mainframe, text='StartingPeriodID: ')
periodL.grid(column=0,row=4)
periodE = Entry(mainframe, bd=5,width=30)
periodE.grid(column=1,row=4)

carrierL = Label(mainframe, text='CarrierID List (as csv): ')
carrierL.grid(column=0,row=5)
carrierE = Entry(mainframe, bd=5,width=30)
carrierE.grid(column=1,row=5)

TaskNameL = Label(mainframe, text='What task do\nyou want to assign: ')
TaskNameL.grid(column=0,row=6)
TaskNameE = Listbox(mainframe, selectmode=BROWSE, height=4, bd=5,width=30)
TaskNameE.insert(1, 'CarrierBuild - Assign')
TaskNameE.insert(2, '2nd - Assign')
TaskNameE.insert(3, 'QA - Assign')
TaskNameE.insert(4, 'GoLive - Process - Assign')
TaskNameE.grid(column=1,row=6)

spacer = Label(mainframe, text='___________________')
spacer.grid(column=0,row=7,columnspan=2)

BuilderL = Label(mainframe, justify=CENTER, text='Who would you like to assign to?\n(Please only input the number)')
BuilderL.grid(column=0,row=8,columnspan=2)
BuilderL2 = Label(mainframe,justify=CENTER,text='1) Andrew K\n2) Brian E\n3) Heather Y\n4) Hillary V\n5) Isaac M\n6) James D\n7) Jon B\n8) Jon N')
BuilderL2.grid(column=0,row=9)
BuilderL3 = Label(mainframe,justify=CENTER,text='9) Matthew A\n10) Matthew S\n11) Melodie C\n12) Rick N\n13) Robert E\n14) Shawn L\n15) Susan B')
BuilderL3.grid(column=1,row=9)

BuilderE = Entry(mainframe,bd=5)
BuilderE.grid(column=0,row=10,columnspan=2)

def tester():
    global username
    global password
    global carrieridlist
    global periodid
    global taskname
    global Builder
    global client
    username = unE.get()
    password = passE.get()
    carrieridlist = carrierE.get()
    periodid = periodE.get()
    taskname = TaskNameE.get(ACTIVE)
    Builder = BuilderE.get()
    client.login(username,password)
    getproject()
    gettask()
    putassignment()
    print 'Update successful!'

runprogram = Button(mainframe, text='Execute', command=tester)
runprogram.grid(column=0, row=11, columnspan=2)






#fieldlist = ['ID','DE:Quotit CarrierID','DE:Quotit EffectiveDateStart']


def getproject():
    global carrieridlist
    global periodid
    global client
    
    carrierIDs = [int(x) for x in carrieridlist.split(",")]
    for carrierid in carrierIDs:
        results = client.search(ObjCode.PROJECT,{'DE:Quotit CarrierID':carrierid,'DE:Quotit EffectiveDateStart':convertperiodid(int(periodid))})
        print 'Project ID list:'
        for p in results:
            project = AtTaskObject(p)
            projIDlist.append(project.ID)
            print project.ID
        

def gettask():
    global taskname
    global client
    
    chosen = False
    for projid in projIDlist:      
        results = client.search(ObjCode.TASK,{'projectID':projid,'name':taskname})
        for p in results:
            task = AtTaskObject(p)
            taskIDlist.append(task.ID)


def putassignment():
    global Builder
    global client
    Builder = int(Builder)
    userdict = {1:'55d60ecd00a4517d7415e1cf2de7cd5f',2:'55de23b801009a88cbcaf585798f8f09',3:'55de23b801009ad947ca5f247e35c196',4:'55de23b801009af0bcc3e4132872867e',5:'55de23b801009a96df0c4a6ad04a365d',6:'55de23b801009aa73f21613500b738e3',7:'55de23b901009b0dd1b7e26c6f351f91',8:'55de23b901009b1e5819654925ba79d0',9:'55e0c49f00279aa470cefd44be40676f',10:'55de23b801009a716cbfc82eb38c5543',11:'55de23b901009b2f4e5b7da737aab254',12:'55d51a820020a3800f6e0f01c450d3e2',13:'55de23b901009b228d9cca8accda5c5d',14:'55de23b901009b282667fbb576d1d822',15:'55de23b801009a7bee1b1b0b382856e3'}
    for taskassign in taskIDlist:
        results = client.put(ObjCode.TASK,taskassign,{'assignedToID':userdict[Builder]})
     

    
def convertperiodid(period):
    yearmod = (period - 205)/12  
    if period % 12 == 0:
        monthmod = 12
    else:
        monthmod = period % 12
    monthprefix = '0' if monthmod < 10 else ''
    return str(2016+yearmod) + '-' + monthprefix + str(monthmod) + '-01T00:00:00:000-0000'


    
    
if __name__ == '__main__':
    root.mainloop()
    

