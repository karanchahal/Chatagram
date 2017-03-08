// Example 1: sets up service wrapper, sends initial message, and
// receives response.

var ConversationV1 = require('watson-developer-cloud/conversation/v1');
let config = require('./config.json')
var prompt = require('prompt-sync')();

// Set up Conversation service wrapper.
var conversation = new ConversationV1({
  username: config.username, // replace with username from service key
  password: config.password, // replace with password from service key
  path: { workspace_id: 'fba7b3e5-6881-416c-9cf1-578fce2a9fee' }, // replace with workspace ID
  version_date: '2016-03-08'
});
// Start conversation with empty message.
conversation.message({}, processResponse);

// Process the conversation response.
function processResponse(err, response) {
  if (err) {
    console.error(err); // something went wrong
    return;
  }

  // If an intent was detected, log it out to the console.
  if (response.intents.length > 0) {
    console.log('Detected intent: #' + response.intents[0].intent);
  }

  // Display the output from dialog, if any.
  if (response.output.text.length != 0) {
      console.log(response.output.text[0]);
  }

  // Prompt for the next round of input.
  var newMessageFromUser = prompt('>> ');
  conversation.message({
    input: { text: newMessageFromUser }
    }, processResponse)
}
