import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATA_FILE_PATH='aps_failure_training_set1.csv'

DATABASE_NAME = "aps"
CONNECTION_NAME = " sensor"






if __name__ =="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape} ")


    # convert datframe to json format so that we can dump this record in mongodb
    df.reset_index(drop=True,inplace=True)

    json_record =  list(json.loads(df.T.to_json() ).values())
    print(json_record[0])

    # insert converted json record to mongodb
    client[DATABASE_NAME][CONNECTION_NAME].insert_many(json_record)





