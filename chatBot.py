from watson_developer_cloud import ConversationV1
import json
import fileinput

with open('config.json') as data_file:
    config = json.load(data_file)

with open('users.json') as data_file:
    users = json.load(data_file)

conversation = ConversationV1(
  username=config['conversation']['username'],
  password=config['conversation']['password'],
  version='2017-02-03'
)

# Replace with the context obtained from the initial request
global context
context = {}

workspace_id = 'fba7b3e5-6881-416c-9cf1-578fce2a9fee'



def converse(inputline):
    global context


    response = conversation.message(
      workspace_id=workspace_id,
      message_input={'text': inputline},
      context=context
    )

    context = response['context']
    print(response['output'])

    '''
    if(response['output']['text'] != [] and response['entities'] != [] and response['entities'][0]['entity'] == 'account' and response['entities'][1]['entity'] == 'sys-number'):
        acc_no = response['entities'][1]['value']
        print("The balance of " + users[acc_no]['name'] + "is " +  users[acc_no]['balance'])
    '''


for line in fileinput.input():
    converse(line.strip())





print(json.dumps(response, indent=2))
