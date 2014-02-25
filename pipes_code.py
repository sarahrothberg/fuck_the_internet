# Instantiate the Choreo, using a previously instantiated TembooSession object, eg:
# session = TembooSession('ACCOUNT_NAME', 'APP_NAME', 'APP_KEY')
getMessageChoreo = GetMessage(session)

# Get an InputSet object for the choreo
getMessageInputs = getMessageChoreo.new_input_set()

# Set inputs
getMessageInputs.set_AuthToken("")
getMessageInputs.set_AccountSID("")
getMessageInputs.set_SMSMessageSID("")

# Execute choreo
getMessageResults = getMessageChoreo.execute_with_results(getMessageInputs)