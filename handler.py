import json
import boto3
import os
import pandas as pd

# create the s3 object from boto3.resource
s3 = boto3.resource("s3")
object = s3.Object(os.environ["BUCKET"], "albumlist.csv")

# create the dynamodb table object from boto3.resource
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["TABLE"])


# function to extract data from s3 into dynamodb table
# first it pulls the csv file from the s3 storage and creates a pandas dataframe
# then for each row in dataframe an item is created and placed into the table
# returns a response with success message
def s3toDynamo(event, context):
    csv = object.get()
    df = pd.read_csv(csv["Body"])

    for row in df.itertuples():
        item={
            "itemId": row.number,
            "year": row.year,
            "album": row.album,
            "artist": row.artist,
            "genre": row.genre,
            "subgenre": row.subgenre
        }
        table.put_item(Item=item)


    body = {
        "message": "File imported from s3 to dynamodb successfully",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
