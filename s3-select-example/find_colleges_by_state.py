import boto3

# S3 bucket to query (Change this to your bucket)
S3_BUCKET = 'greg-college-data'

s3 = boto3.client('s3')

r = s3.select_object_content(
        Bucket=S3_BUCKET,
        Key='COLLEGE_DATA_2015.csv',
        ExpressionType='SQL',
        Expression="select * from s3object s where s.\"STABBR\" like '%IA%'",
        InputSerialization={'CSV': {"FileHeaderInfo": "Use"}},
        OutputSerialization={'CSV': {}},
)

for event in r['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        statsDetails = event['Stats']['Details']
        print("Stats details bytesScanned: ")