import pymongo
import pandas as pd
import json
<<<<<<< HEAD

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



=======
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH ="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME='aps'
collection_name='sensor'

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f'Rows and Columns: {df.shape}')

# convert dataframe to jason so that we can dump these records in mongo db
    df.reset_index(drop=True,inplace=True)
    json_record= list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    # insert converted json records to mongo DB
    client[DATABASE_NAME][collection_name].insert_many(json_record)
    
>>>>>>> 510e3e4b8682b408afbd40829bbac2f47d250bad


