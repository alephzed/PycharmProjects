from download import constructYFURL
from download import download

localFilePath = "/Users/adlee/download.csv"
download(localFilePath, "MSFT")

# ticker = "^GSPC"
# start_date = "2015-01-01"
# end_date = "2017-07-03"
# freq = "d"
# yfURL = constructYFURL(ticker, start_date, end_date, freq)
# print yfURL
