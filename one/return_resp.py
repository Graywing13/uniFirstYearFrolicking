def strip_response(responses):
   stripped_responses = []
   for response in responses:
       if (response[0:9] == "response:") and (len(response) >= 15):
           response = response[9:]
           if response not in stripped_responses:
               stripped_responses.append(response)
   return stripped_responses

 
def starts_with_response(s: str) -> bool:
   """
   produce True if the string starts with 'response:'
   """
   #return False #stub
   # Template based on atomic, non-distinct
   if s == 'response:':
       return True
   else:
       return s.startswith('response:')

def long_string(s: str) -> bool:
   """
   produce True if the string is longer or equal to 15 characters
   """
   #return False #stub
   # Template based on atomic, non-distinct
   if len(s) >= 15:
       return True
   else:
       return False

def strip_resp(response):
   """
   produce response if the string does not start with response: and is shorter than 15 characters,
   returns the response stripped of 'response:' if otherwise
   """
   valid_response = []
   #return 'Hello' #stub
   # Template based on arbitrary
   for r in response:
       if (starts_with_response(r) == True):
           if long_string(r) == True:
               r = r[9:]
           else:
               r = None
       if r not in valid_response:
           valid_response.append(r)
   return valid_response

chars = strip_response(["response:reinhardt", "surtr", "response:tiki", "ogma", "response:reinhardt", "katarina and celica"])

print("Do NOT use the following characters for autobattle or else kekyoin will start laughing at u. {}".format(chars))
