import json
import requests

def lambda_handler(event, context):
    response = requests.get('https://example.com/')
    message = 'site is Down!'
    if response.status_code == 200:
        message = 'site is Up!'
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message,
            'version': '1.1'
        })
    }