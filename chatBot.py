from watson_developer_cloud import ConversationV1
import json
import fileinput

#Opening Files
with open('config.json') as data_file:
    config = json.load(data_file)

with open('users.json') as data_file:
    users = json.load(data_file)

# Setting up Watson API's
conversation = ConversationV1(
  username=config['conversation']['username'],
  password=config['conversation']['password'],
  version='2017-02-03'
)

# Variables
global context
context = {}
workspace_id = 'fba7b3e5-6881-416c-9cf1-578fce2a9fee'

''' Authenticates/logs-in user '''
def authenticate(acc_no,pincode):
    if(users[acc_no]['pincode'] == pincode):
        return True
    else:
        return False


'''
Deals With Various responses and Updates Context Variables for directing conversation flow
'''
def dealWith(response):
    more_response = ''
    if('verified' in response['context']):

        if(response['context']['verified'] == "1" and response['output']['nodes_visited'][0] == 'bank-balance'):
            acc_no = response['context']['acc_no']
            more_response = users[acc_no]['name'] + "'s account balance is " + users[acc_no]['balance'] + " " +users[acc_no]['currency']

    if(response['output']['nodes_visited'][0] == 'account-number'):
        response['context']['acc_no'] = response['entities'][0]['value']
        acc_no = response['context']['acc_no']
        response['context']['pincode'] = users[acc_no]['pincode']


    return response,more_response


''' Helper functions '''
def printJSON(printThis):
    print(json.dumps(printThis, indent=2))

''' Driver main function '''
def converse(inputline):
    global context
    response = conversation.message(
      workspace_id=workspace_id,
      message_input={'text': inputline},
      context=context
    )
    response,additionalResponse = dealWith(response)
    context = response['context']
    return response['output']['text'][0] +'\n' +  additionalResponse
