from datetime import date

class Student:
    def __init__(self,s,n,d,c):
        self.__studentID = s
        self.__Name = n
        self.__dob = d
        self.__classification = c
        self.__age = 0
        self.__register = ""
        

    def age(self):
        today = date.today()
        dob = self.__dob.split('/')
        dob_year = int(dob[2])
        self.__age = today.year - dob_year 

        
    
    def reg(self):
        if self.__classification == 'Sr':
            self.__register = '4/1 - 4/3'
        elif self.__classification == 'Jr':
            self.__register == '4/4 - 4/6'
        elif self.__classification == 'S':
            self.__register = '4/7 - 4/9'
        elif self.__classification == "F":
            self.__register ='4/10 - 4/12'
        else:
            print("Classification not found!")


        '''
        reg_dates = {"Seniors": '4/1 - 4/3',
                     "Juniors": '4/4 - 4/6',
                     "Sophomores": '4/7 - 4/9',
                     "Freshmen": '4/10 - 4/12'}
        self.__reg_dates = reg_dates[self.__classification]
    '''
    def get_age(self):
        return self.__age
    
    def get_reg(self):
        return self.__register
