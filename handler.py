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

    body = datasetFacts(df)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


# function to provide facts about the dataset
# the most popular artist in the entire dataset and in each decade is calculated
# the most popular genre in the entire dataset and in each decade is calculated
# returns the description in the form of a message in the body
def datasetFacts(df):
    mp_artist = df["artist"].value_counts().idxmax()
    mp_artist_1960 = df[df["year"].between(1960, 1969)]["artist"].value_counts().idxmax()
    mp_artist_1970 = df[df["year"].between(1970, 1979)]["artist"].value_counts().idxmax()
    mp_artist_1980 = df[df["year"].between(1980, 1989)]["artist"].value_counts().idxmax()
    mp_artist_1990 = df[df["year"].between(1990, 1999)]["artist"].value_counts().idxmax()
    mp_artist_2000 = df[df["year"].between(2000, 2009)]["artist"].value_counts().idxmax()

    mp_genre = df["genre"].value_counts().idxmax()
    mp_genre_1960 = df[df["year"].between(1960, 1969)]["genre"].value_counts().idxmax()
    mp_genre_1970 = df[df["year"].between(1970, 1979)]["genre"].value_counts().idxmax()
    mp_genre_1980 = df[df["year"].between(1980, 1989)]["genre"].value_counts().idxmax()
    mp_genre_1990 = df[df["year"].between(1990, 1999)]["genre"].value_counts().idxmax()
    mp_genre_2000 = df[df["year"].between(2000, 2009)]["genre"].value_counts().idxmax()

    body = {
        "message": "The most popular artist in the dataset was %s and the most popular genre in the dataset was %s. \n \
        In the 1960s, the most popular artist was %s and the most popular genre was %s. \n \
        In the 1970s, the most popular artist was %s and the most popular genre was %s. \n \
        In the 1980s, the most popular artist was %s and the most popular genre was %s. \n \
        In the 1990s, the most popular artist was %s and the most popular genre was %s. \n \
        In the 2000s, the most popular artist was %s and the most popular genre was %s."
        % (str(mp_artist), str(mp_genre), str(mp_artist_1960), str(mp_genre_1960),
        str(mp_artist_1970), str(mp_genre_1970), str(mp_artist_1980), str(mp_genre_1980),
        str(mp_artist_1990), str(mp_genre_1990), str(mp_artist_2000), str(mp_genre_2000))
    }

    return body
