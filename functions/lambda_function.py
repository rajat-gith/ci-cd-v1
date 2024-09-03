def lambda_handler(event, context):
    # Extract numbers from the event input
    num1 = event.get('num1', 0)
    num2 = event.get('num2', 0)
    
    # Perform the addition
    result = num1 + num2
    
    # Return the result
    return {
        'statusCode': 200,
        'body': {
            'num1': num1,
            'num2': num2,
            'result': result
        }
    }
