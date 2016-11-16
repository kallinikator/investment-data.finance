from api.models import Stock, PriceData, FundamentalData
import pandas
import time
import glob

def log(func, *args): # BUGGY
    def wrapper(*args):
        t0 = time.time()
        func(*args)
        t1 = time.time()
        time_needed = t1 - t0
        with open("Databaselog.txt", "a") as logfile:
            logfile.write("Function {} was called on {}. It needed {} seconds.\n".format(func.__name__, args[0], str(time_needed)))
    return wrapper    

    
def create_all_prices():
    """ Basic function """
    all_files = glob.glob("C:/Users/Till/Desktop/Project Dollar/Stock_data/All_Data/*")
    print("Starting!")
    for file in all_files:
        print(file)
        create_prices(file)        
        

@log
def create_prices(file):
    """Creates the database entry for all stocks in one prices.csv file"""
    try:
        df = pandas.read_csv(file + "/prices.csv")
        df.drop(df.columns[[2, 4, 5, 6, 7]], axis=1, inplace=True)
    except:
        print("Opening {} failed!!".format(file))
        with open("Databaselog.txt", "a") as logfile:
            logfile.write(str(x) + " failed!")
    for x in df.values:
        try:
            name = Stock.objects.get(symbol=x[0])
            if not len(PriceData.objects.filter(stock=name, date=x[1])):
                dataset = PriceData()
                dataset.stock = name
                dataset.date = str(x[1])
                dataset.price_high = str(x[2])
                dataset.save()
                #print(x[0] + " added!")
            else:
                pass
                #print("Data of {} on day {} already exists!".format(str(x[0]), str(x[1])))
        except:
            print(str(x) + " failed!")
            with open("Databaselog.txt", "a") as logfile:
                logfile.write(str(x) + " failed!\n")
            # Buggy here!!
            create_stocks(file, x[0])
            create(file)

           

@log
def create_stocks(file, symbol):
    """ This function adds a company with an yet unknown symbols to the stocks- database"""
    with open(file + "/symbols.txt") as symbols:
        for company in symbols: # Hell! Files are Iterators!
            if company.startswith(symbol):
                new = Stock()
                new.symbol = symbol
                new.full_name = company.split("\t")[1]
                new.save()
                print("New Stock created!")

def clean():
    for entry in Stock.objects.iterator():
        delete_stuff(entry)


def delete_stuff(entry):
    import random
    try:
        Stock.objects.get(symbol=entry.symbol)
        print("Alright! on {}".format(entry))
    except:
        print("Alarm! on {}".format(entry))
        try:
            entry.delete()
        except:
            entry.id = random.randint(99999999999, 10000000000000)
            return
        delete_stuff(entry)
        

def create_all_fundamentals():
    """ Basic function """
    all_files = glob.glob("C:/Users/Till/Desktop/Project Dollar/Stock_data/All_Data/*")
    print("Starting!")
    for file in all_files:
        print(file)
        create_fundamentals(file)        
        

def create_fundamentals(file):
    """Creates the database entry for all stocks in one prices.csv file"""
    try:
        df = pandas.read_csv(file + "/reports.csv")
    except:
        print("Opening {} failed!!".format(file))
        with open("Databaselog2.txt", "a") as logfile:
            logfile.write(str(file) + " failed!")
    try:
        for x in df.values:
            name = Stock.objects.get(symbol=x[0])
            dataset = FundamentalData()
            dataset.stock = name
            dataset.symbol = name.symbol
            dataset.date = file.split("/")[-1]
            dataset.end_date = x[1]
            dataset.amend = x[2]
            dataset.period_focus = x[3]
            dataset.fiscal_year =x[4]
            dataset.doc_type = x[5]
            dataset.revenues = x[6]
            dataset.op_income = x[7]
            dataset.net_income = x[8]
            dataset.eps_basic = x[9]
            dataset.eps_diluted = x[10]
            dataset.dividend = x[11]
            dataset.assets = x[12]
            dataset.cur_assets = x[13]
            dataset.cur_liab = x[14]
            dataset.cash = x[15]
            dataset.equity = x[16]
            dataset.cash_flow_op = x[17]
            dataset.cash_flow_inv = x[18]
            dataset.cash_flow_fin = x[19]
            dataset.save()
            print(x[0] + " added!")
    except:
        print(str(file) + " failed!")
        with open("Databaselog2.txt", "a") as logfile:
            logfile.write(str(file) + " failed!\n")

def update_fundamentals():
    """ For special problems and mistakes """
    all_files = glob.glob("C:/Users/Till/Desktop/Project Dollar/Stock_data/All_Data/*")
    print("Starting!")
    for file in all_files:
        print(file)
        try:
            df = pandas.read_csv(file + "/reports.csv") 
        except:
            print("fail!")
            continue
        for x in df.values:
            try:
                stock = Stock.objects.get(symbol=x[0])
            except:
                continue
            try:
                dataset = stock.fundamentals.get(end_date=x[1])
            except:
                try:
                    too_big_dataset = stock.fundamentals.filter(end_date=x[1])
                    dataset = too_big_dataset[0]
                    for double in too_big_dataset[1:]:
                        double.delete()
                    print("cleaned {}".format(x[0]))
                except:
                    continue
            string_date = file[-8:]
            dataset.date = "-".join((string_date[:4], string_date[4:6], string_date[6:]))
            dataset.save()
            print(x[0] + " updated!")
            


# All this could have been done easier with pk.create("variable":"blabal")
if __name__ == "__main__":
    update("C:/Users/Till/Desktop/Project Dollar/Stock_data/All_Data/20160106/prices.csv")
