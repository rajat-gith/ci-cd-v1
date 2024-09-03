import os
import requests

def lambda_handler(event, context):
    api_url = os.getenv('API_URL')

    if not api_url:
        return {
            'statusCode': 500,
            'body': 'Environment variables API_URL or API_KEY are not set.'
        }
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return {
                'statusCode': 200,
                'body': data
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': f'Error: {response.text}'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Exception occurred: {str(e)}'
        }
