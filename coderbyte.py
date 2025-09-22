import pandas as pd 

#stringio was also a viable alternative to write the data into the csv file, however i could not recall it's implementation at the time of coding this :(
# so i went ahead using the open function 
#this version fills in missing flight codes while preserving existing values, while the first submission overwrote the entire column in new sequence


data = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

with open("flight_data.csv", "w") as file:
    file.write(data)

df = pd.read_csv("flight_data.csv", sep = ";")

df["Airline Code"] = (
    df["Airline Code"]
    .str.replace(r"[^\w\s]", "", regex=True) #cleaning the airline code column
    .str.strip() 
)


df["FlightCodes"] = pd.to_numeric(df["FlightCodes"], errors="coerce") #converting the flight codes to numeric values
codes = pd.Series(range(1010, 1010 + 10*len(df),10), index=df.index) 
df["FlightCodes"] = df["FlightCodes"].fillna(codes)#filling null vals with ideal sequnces 
df["FlightCodes"] = df["FlightCodes"].astype(int)

df[["From", "To"]] = df["To_From"].str.upper().str.split("_", expand=True)

df = df.drop(columns=["To_From"])

df.to_csv("final_flight_data.csv", index=False)







print(data)
