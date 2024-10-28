from datetime import datetime
categories={'I':"Income",'E':"Expenses"}
def get_date(prompt,allow_default=False):
    date_str=input(prompt)
    if allow_default and not date_str:
       return datetime.today().strftime("%d-%m-%Y")
    try:
       valide_date=datetime.strptime(date_str,"%d-%m-%Y")
       return valide_date.strftime("%d-%m-%Y")#it give us the date in the clean format we what it 
    except ValueError :
       print("Invalid date format. ")
       return get_date(prompt,allow_default)
def get_amount():
    try:
        amount=float(input("Enter the amount: "))
        if amount<=0:
            raise ValueError("the amount must not be negative")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category=input("please enter category ('I'for income , 'E' for expenses)").upper()
    if category  in categories:
        return categories[category]
    else :
        print("Invalid category")
        return get_category()
def get_description():
    return input("Enter the description ! :")
    