#-*-coding:utf-8-*-
class student:
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = ph
        print('created instance for:',self.name)
    def update(self,newph):
        self.phone = newph
        print('update phone#for:',self.name)



student = student('xiaoli','13987461894')
print(student.phone)


