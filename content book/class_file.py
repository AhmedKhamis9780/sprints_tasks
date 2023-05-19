import pandas as pd
import datetime
class content:
    def __init__(self,filename):
        self.filename=filename
        # Read CSV file into a DataFrame
        data_df = pd.read_csv(filename)
        # Convert DataFrame to dictionary
        self.data_dict = data_df.to_dict(orient="list")
        

    
    
    def view_content(self):
        print(pd.DataFrame(self.data_dict))

    def create_content(self):
        print('creating a new content:')
        name=input('Enter a content name:')
        email=input('Enter a content email:')
        phone=input('Enter a content phone number:')
        address=input('Enter a content address:')
        self.data_dict['username'].append(name)
        self.data_dict['email'].append(email)
        self.data_dict['phone'].append(phone)
        self.data_dict['address'].append(address)
        self.data_dict['create_date'].append(datetime.date.today())
        data_df = pd.DataFrame(self.data_dict)
        data_df.to_csv(self.filename, index=False)

    def del_content(self):
        print('deleting a content')
        name=input('Enter the name of content you want to delete:')
        try :
            index=self.data_dict['username'].index(name)
        except:
            print('the name is not in the list of content')
        else:
            self.data_dict['username'].pop(index)
            self.data_dict['email'].pop(index)
            self.data_dict['phone'].pop(index)
            self.data_dict['address'].pop(index)
            self.data_dict['create_date'].pop(index)
            data_df = pd.DataFrame(self.data_dict)
            data_df.to_csv(self.filename, index=False)
        

    def modify_content(self):
        print('modify a content')
        name=input('Enter the name of content you want to modify:')
        num=input('''
        what you want to change 
        1:Name
        2:email
        3:phone number
        4:address
        Enter the number operation:''')
        change_value=input('Enter the value to change it to:')
        try :
            index=self.data_dict['username'].index(name)
        except:
            print('the name is not in the list of content')
        else:    
            if num=='1':
                self.data_dict['username'][index]=change_value
            elif num=='2':
                self.data_dict['email'][index]=change_value
            elif num=='3':
                self.data_dict['phone'][index]=change_value
            elif num=='4':
                self.data_dict['address'][index]=change_value
            else:
                print('wrong number')
        data_df = pd.DataFrame(self.data_dict)
        data_df.to_csv(self.filename, index=False)    






    