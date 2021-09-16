from datetime import datetime
def constructYFURL(ticker,start_date,end_date,freq):
    start_date = datetime.strptime(start_date,"%Y-%m-%d").date()
    end_date = datetime.strptime(end_date,"%Y-%m-%d").date()

    s=ticker.replace("^","%5E")

    if start_date.month-1<10:
        a="0"+str(start_date.month-1)
    else:
        a=str(start_date.month-1)
    # a represents the month portion - however the month count starts from 0
    # Also the month always has 2 digits
    b=str(start_date.day)

    c=str(start_date.year)
    # b and c represent the day and year parts of the start date
    if end_date.month - 1 < 10:
        d = "0" + str(end_date.month - 1)
    else:
        d = str(end_date.month - 1)
    # similarly we have to set up the month part for the end date
    e=str(end_date.day)

    f=str(end_date.year)
    # e and f represent the day and year parts of the end date
    g=freq
    # g represents the frequency d = daily, w= weekly, m=monthly

    # Finally let's set up the URL
    # https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=1467690860&period2=1499226860&interval=1d&events=history&crumb=P.ADpVAnFKf
    yfURL = "http://download.finance.yahoo.com/"+g+"/quotes.csv?s="+s+"&a="+a+"&b="+b+"&c="+c+"&d="+d+"&e="+e+"&f="+f
    return yfURL

def download(filePath,symbol):
    from crumbSource import download

    data = download(symbol)
    data.to_csv(filePath, sep='\t', encoding='utf-8' )
    # with open(filePath,"wb") as output:
    #     output.write(bytearray(data))
    # print data