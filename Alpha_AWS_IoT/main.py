"""
Instructions:

 - "ssl_params" shows which ssl parameters are required, and gives
   examples for referencing the files
 - If needed, replace the file paths to match the certificates you're using
 - The policy attached to the SSL certificates must allow for
   publishing, subscribing, connecting, and receiving
 - The host and region need to be filled in to create a valid
   AWS endpoint to connect to
 - If you want to change any of the params in the method, call the method again
   and pass in the params you want

"""

from umqtt.simple import MQTTClient
import time, network

#cert files
CA = '/cert/aws.ca'
KEY = '/cert/aws.key'
CERT = '/cert/aws.crt'

with open(KEY, 'r') as f:
    key = f.read()
print('got keys')

with open(CERT, 'r') as f:
    cert = f.read()
print('got cert')

# AWS endpoint parameters
host = b'abcdefg1234567'  # ex: b'abcdefg1234567'
region = b'us-east-1'  # ex: b'us-east-1'

aws_endpoint = b'%s.iot.%s.amazonaws.com' % (host, region)
    

def publish_test(clientId="donat", hostname=aws_endpoint, sslp={ "key":key, "cert":cert, "server_side":True }):
    # "clientId" should be unique for each device connected
    c = MQTTClient(client_id=clientId, server=aws_endpoint, port=8883, keepalive=10000, ssl=True, ssl_params=sslp)
    print("connecting...")
    c.connect()
    print("connected")

    # topic: "sample/xbee"
    # message: {message: AWS Samples are cool!}
    print("publishing message...")
    c.publish("test/python", '{"message": "AWS Sample Message"}')
    print("published")
    c.disconnect()
    print("DONE")

publish_test() 
 
