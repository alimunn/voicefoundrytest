# voicefoundrytest
  
This is the technical test for Voice Foundry. I implemented the project in Python, making use of the boto3 module and the pandas module for manipulating the dataset. To run the code, pull it to your computer, make sure you have the required dependencies installed before running sls deploy. This will create the Lambda, S3 bucket and Dynamo DB table, and upload a file to the bucket. After this, navigate to the URL listed under the endpoints as GET. This will extract the file from S3, insert the data into Dynamo DB and display information about the dataset on the screen.
  
The dataset that I decided to use for this project was the Rolling Stone magazine's 2012 list of top 500 albums of all time. Music is one of my main hobbies and I completed my individual project at university on Group Music Recommendation, so I was keen to use another music-based dataset in this project. This dataset is contained within the UploadData folder to allow it to be uploaded to s3 when sls deploy is run. A link to the dataset is contained here: https://data.world/notgibs/rolling-stones-top-500-albums
  
I had very limited experience with AWS and no experience with the Serverless framework before completing this project. Due to this I spent around 4 days completing online courses, reading documentation and doing a couple of sample projects before diving into the assigned task. After looking at the assignment I came up with the following plan to complete the assignment.
  
1. Create the s3 bucket and upload csv file to it
2. Create the dynamodb table
3. When triggered by accessing the GET url listed in the command line when successfully deployed, using a lambda function extract the csv file from the s3 bucket and populate the dynamodb table.
4. Expand upon this function to provide insights into the dataset, displayed in a message on the screen.
  
I completed the first two steps in good time, however when attempting to extract the csv file from the s3 bucket I kept getting an AccessDenied error, due to my inexperience with AWS. This was eventually resolved by fixing some indentation in my serverless.yml file, and I will make sure to not make that mistake again. Due to limited time before the deadline after resolving this error I wrote a couple insights into the dataset, extracting the most popular artists and genres over the whole dataset and for each decade. Given more time I would delve further into the dataset, expand upon these insights and combine the information in this dataset with other datasets to gain more detailed information. 
  
I thoroughly enjoyed completing this assignment and enjoyed the creative realm given to me. Having no previous experience with Serverless and limited AWS experience, the task gave me the opportunity to learn several new skills and implement my programming knowledge in a way I haven't before. I am excited to continue developing these cloud-based skills and tackle many more projects in the future. I look forward to hearing from you!
  