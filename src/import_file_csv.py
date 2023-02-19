import pandas

# filepath_or_buffer
# skiprows #skiprows=0, nrows=500
# chunksize = n
# filepath_or_buffer = "files\"
filename = 'files\departments.csv'
df = pandas.read_csv(filename, sep=',', header=None, chunksize=3)   #header=0
#df = pd.read_csv("dataset.csv",usecols=["Country","Sales Channel","Order Priority"])

for data in df:
    print(data)


# print(data.shape)
# print (data.head(20))
# print (data)

