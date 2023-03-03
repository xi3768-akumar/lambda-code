# Test 1
import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    print("value4 = " + event['key4'])
    print("value5 = " + event['key5'])
    return event['key1']  # Echo back the first key value
    print("Changes made to this lambda only")
