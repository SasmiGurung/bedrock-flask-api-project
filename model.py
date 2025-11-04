import boto3
from botocore.exceptions import ClientError


# class BedrockModel:
#   def invokeModel(self, long_text: str = ""):
#     # TODO: Create bedrock client, define model
    
#     user_message = f"""
#     # Role
#     You are an expert content creator specializing in content summarization for generic tasks.

#     # Task
#     Your task is to understand the content from the input text, which is usually a long paragraph, and summarize this long content into short paragraphs by retaining all the meaningful information.

#     # Input
#     This is the input long content for summarization:
#     {long_text}

#     # Output
#     Please return a summarized paragraph for the inputs in maximum of 2 to 3 sentences. It is forbidden to add any additional explanation, details or unnecessary structures.
#     """

#     # TODO: Define payload: converstions

#     # TODO: Invoke bedrock model. Use try-catch, client.converse
#     bedrock_response = ""

#     # TODO: Postprocessing of raw bedrock response
#     response_text = "Waiting implementaion"

#     return response_text







class BedrockModel:
  def invokeModel(self, long_text: str = ""):
    # TODO: Create bedrock client, define model

    #Create bedrock runtime Client
    client = boto3.client("bedrock-runtime", region_name = "us-east-1")

    #Set the model ID
    model_id = "amazon.nova-micro-v1:0"
    
    user_message = f"""
    # Role
    You are an expert content creator specializing in content summarization for generic tasks.

    # Task
    Your task is to understand the content from the input text, which is usually a long paragraph, and summarize this long content into short paragraphs by retaining all the meaningful information.

    # Input
    This is the input long content for summarization:
    {long_text}

    # Output
    Please return a summarized paragraph for the inputs in maximum of 2 to 3 sentences. It is forbidden to add any additional explanation, details or unnecessary structures.
    """

    # TODO: Define payload: converstions
    conversation = [
      {
        "role": "user",
        "content":[{"text": user_message}], 
      }
    ]
      

    # TODO: Invoke bedrock model. Use try-catch, client.converse
    try:
    #Send message to the model
      bedrock_response = client.converse(
      modelId=model_id,
      messages=conversation,
      inferenceConfig={"maxTokens":50, "temperature":0.5, "topP":0.9}   
    )
    # TODO: Postprocessing of raw bedrock response

    #Extract and print the response text.
      response_text = bedrock_response["output"]["message"]["content"][0]["text"]
      return response_text
      # print(response_text)

    except (ClientError, Exception) as e:
      print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")

      return str(e)
     




#Create bedrock runtime Client
# client = boto3.client("bedrock-runtime", region_name = "us-east-1")

#Set the model ID
# model_id = "amazon.nova-micro-v1:0"

# #Start a conversation with the user message
# system_prompt = ""
# user_message = "Describe bedrock in 30 words."

# conversation = [
#   {
#     "role": "user",
#     "content":[{"text": user_message}],
#     }
#     ]

# try:
#   #Send message to the model
#   response = client.converse(
#     modelId=model_id,
#     messages=conversation,
#     inferenceConfig={"maxTokens":50, "temperature":0.5, "topP":0.9}   
#   )
#   #Extract and print the response text.
#   response_text = response["output"]["message"]["content"][0]["text"]
#   print(response_text)

#   # print(response)

# except (ClientError, Exception) as e:
#   print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
#   exit(1)




# def model_functions():
#   client = boto3.client("bedrock-runtime", region_name = "us-east-1")
#   model_id = "amazon.nova-micro-v1:0"
#   system_prompt = ""
#   user_message = "Describe bedrock in 30 words."
  
#   conversation = [{
#     "role": "user",
#     "content":[{"text": user_message}],
#   }
#   ]
  
#   try:
#     response = client.converse(
#     modelId=model_id,
#     messages=conversation,
#     inferenceConfig={"maxTokens":50, "temperature":0.5, "topP":0.9}   
#   )
#     response_text = response["output"]["message"]["content"][0]["text"]
#     # print(response_text)

#     model_functions(response_text)
#      # print(response)

   
    
#   except (ClientError, Exception) as e:
#     print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
#     exit(1)