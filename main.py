import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date,get_amount,get_category,get_description
class CSV:
    csv_file="data.csv"
    colums=["date","amount","category","description"]
    
    @classmethod
    def initialise_csv(cls):
        try:
            pd.read_csv(cls.csv_file)#try to read the file
        except FileNotFoundError:
            df=pd.DataFrame(cls.colums)#create the csv file if it dose not exist
            df.to_csv(cls.csv_file,index=False)
    @classmethod
    def add_data(cls,date,amount,category,description):
        new_entry={"date":date,
                  "amount":amount,
                  "category":category,
                  "description":description}
        with open(cls.csv_file,mode="a",newline='') as file:#open the file with a context manager and will auto handle closing it after the writer works
            writer=csv.DictWriter(file,fieldnames=cls.colums)
            writer.writerow(new_entry)
            
        print("the data is added successufully")
    @classmethod
    def get_transaction(cls,start_date,end_date):
        df=pd.read_csv(CSV.csv_file)
        df["date"]=pd.to_datetime(df["date"],format="%d-%m-%Y",errors='coerce')
        start_date=datetime.strptime(start_date,"%d-%m-%Y")
        end_date=datetime.strptime(end_date,"%d-%m-%Y")#change it to datetime type
        mask=(df["date"]>= start_date )&( df["date"]<=end_date)#this mask will be applied to every ligne to choose the date or not 
        filtered_data_frame=df.loc[mask]#return a filtered df will locate all the raws where the mask condition is valid
        if filtered_data_frame.empty:
            print ("no transaction found on this date range")
        else:
            print(f"transactions from{start_date.strftime("%d-%m-%Y")} to {end_date.strftime("%d-%m-%Y")}")
            print(
                filtered_data_frame.to_string(index=False, formatters={"date": lambda x: x.strftime("%d-%m-%Y")}))
            total_income=filtered_data_frame[filtered_data_frame["category"]=="Income"]["amount"].sum()
            total_expense=filtered_data_frame[filtered_data_frame["category"]=="Expenses"]["amount"].sum()
            print(f" Total Income :${total_income:.2f}")# the 2f is to give the dicimal number
            print(f"Total Expense :${total_expense:.2f}")
            print(f"total net :${(total_income-total_expense):.2f}")
        return filtered_data_frame
        
def add():
    CSV.initialise_csv()
    date=get_date("eneter the date in the format dd-mm-yyyy or u can use todays date",allow_default=True,)
    amount=get_amount()
    category=get_category()
    description=get_description()
    CSV.add_data(date,amount,category,description)
def test_input():
    while True:
        print("\n1.add transaction")
        print("2.get transaction")
        print("3.exit")
        choice=input("enter your choice(1-3): ").strip()
        print(f"DEBUG: User entered '{choice}' (length: {len(choice)})") 
        
        if choice =="1":
            add()
        elif choice =="2":
            startDate=get_date("Enter the start date (dd-mm-yyyy): ")
            endDate=get_date("Enter the end date (dd-mm-yyyy): ")
            df=CSV.get_transaction(startDate,endDate)
            
        elif choice == "3":
            print("Exiting !!!!")
            break
        else:
            print("invalid choice")
            
            
if __name__ == "__main__":
    test_input()
            