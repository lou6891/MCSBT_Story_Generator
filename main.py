from google.cloud import dialogflow
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
import uuid
import gradio as gr
import random
import time
import os
import openai
import json
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

file_path = config.get('agent_dialogflow', 'file_path')

with open(file_path, 'r') as file:
    file_contents = file.read()
    credentials = service_account.Credentials.from_service_account_file(file_path)

openai.api_key = config.get('openai', 'openai_api_key')

session_id = uuid.uuid4().hex
project_id = config.get('agent_dialogflow', 'project_id')

# Initiate the clients 
session_client = dialogflow.SessionsClient(credentials=credentials)
session = session_client.session_path(project_id, session_id)
translate_client = translate.Client(credentials=credentials)

# Define a dictionary mapping language names to their codes
language_codes = {
    'English': 'en', 'French': 'fr', 'German': 'de', 'Italian': 'it',
    'Spanish': 'es', 'Arabic': 'ar', 'Bulgarian': 'bg', 'Catalan': 'ca',
    'Chinese Simplified': 'zh-CN', 'Croatian': 'hr', 'Czech': 'cs',
    'Danish': 'da', 'Dutch': 'nl', 'Estonian': 'et', 'Finnish': 'fi',
    'Greek': 'el', 'Hebrew': 'he', 'Hindi': 'hi', 'Hungarian': 'hu',
    'Icelandic': 'is', 'Indonesian': 'id', 'Japanese': 'ja', 'Korean': 'ko'
    }

# This variable acts as a swithc when the default ending proprt from dialogflow
# is received by the user, the value becomes True 
# sending the requests to CHatGPT instead of Dialogflow
dialogflow_LLN_swith = False

# Dictionary that stores the user imput
parameters_dict = {}
 
# Set up the environment of chatGPT as a famous script creator
global chat_gpt_messages
chat_gpt_messages = [
  {"role": "system", "content": "You are a a famous and well regarded script creator."},
]

# List of messages used to initiate the conversation with dialogflow
# Used to restart the conversation
welcome_messages  = [
    "hello",
    "hello there!",
    "hey, what's up?",
    "greetings!",
    "howdy",
    "hi",
    "hey",
]

def translator(text, target_lang):
  # This function takes in a string of text and used the google translate api  
    translate_client = translate.Client(credentials=credentials)

    if isinstance(text, bytes):
        text = text.decode("utf-8")
    translation = translate_client.translate(text, target_language=target_lang)
    return translation["translatedText"]

def dialogflow_request(text, language_code):
    # translate the request to english every time
    text = translator(text, "en")
    # get the chatbot repsonse
    text_input = dialogflow.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response

def process_parameters(data):
  # THis fucntion takes the data retrieved from the Dialogflow API requests
  # Loops thought the parameters to add the user imput to the dictionary that
  # is used to create the proprt for ChatGPT 
  if len(data) > 1:
    if data and data[0] is not None:
      for i in data[0].parameters:
        if str(i).endswith(".original"):
          continue;
        elif data[0].parameters[i]:
          parameters_dict[i] = data[0].parameters[i]

def chat_with_chatgpt(prompt, model="gpt-3.5-turbo",):
  # This function is the one that is responsable for sending messages to chat GPT,
  # receive the repsonse from the LLM and appends the message of the user and the reposnse to the chat 
  # so that ChatGPT has context of the conversation with the user

  chat_gpt_messages.append( {"role": "user", "content": prompt}, )
  
  chat = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=chat_gpt_messages)
  reply = chat.choices[0].message.content
  chat_gpt_messages.append({"role": "assistant", "content": reply})
  return reply


with gr.Blocks() as demo:
  chatbot = gr.Chatbot()
  msg = gr.Textbox()
  Restat = gr.Button("Restart")
  lang = gr.Dropdown(list(language_codes.keys()) ,label='Language', info="Select Your langauge")

  def restart_chat_gpt():
    # Function in charge of resetting the environment of chat GPT when the conversation is restarted
    global chat_gpt_messages
    chat_gpt_messages = [
      {"role": "system", "content": "You are a a famous and well regarded script creator."},
    ]

  def respond(message, lang ,chat_history):
    global dialogflow_LLN_swith
    global parameters_dict

    if message.lower() in welcome_messages:
      # If the user writes a welcome message the model reverts back to using DialogFlow
      # So when the user press restart, the chat is cleared, he/she write a welcome messgae an dthe chatbot 
      # responds with dialgflow
      restart_chat_gpt()
      dialogflow_LLN_swith = False

    if dialogflow_LLN_swith:
      bot_message = chat_with_chatgpt(message)

    else:
      # Use dialogflow_request
      response = dialogflow_request(message, 'en')

      # Get the answer from the response of Dialogflow
      if response.query_result.fulfillment_messages and response.query_result.fulfillment_messages[0]:
          bot_message = str(response.query_result.fulfillment_messages[0].text.text[0])
      else:
          # Handle the case when fulfillment_messages is empty
          bot_message = "Please refresh the page."
      

      process_parameters(response.query_result.output_contexts)

    # if no language is selected, use english as default answer language
    target_lang = "en"
    if lang :
      target_lang = language_codes[lang]

    # Translate the bot's message
    bot_message_tr = translator(bot_message, target_lang)

    # Append the message and response to the chat history
    chat_history.append((message, bot_message_tr))

    if bot_message == "Sounds great, now I need a few seconds to write your story":
      # When the message ending the DialogFlow conversation is received the switch is activated
      # And the propt with the user inputs are sent to ChatGPT
      dialogflow_LLN_swith = True
      prompt = f'''write a script for a {parameters_dict["genre"]},  where the main character/s is/are {parameters_dict["characters"]}, 
      the location of story shall be  {parameters_dict["location"]}, and the timeperiod is {parameters_dict["time_period"]}, 
      you shall use these props in the story {parameters_dict["props"]}'''
      gpt_story = chat_with_chatgpt(prompt)
      gpt_story_tr = translator(gpt_story, target_lang)
      chat_history.append(("",gpt_story_tr))


    time.sleep(1)
    return "", chat_history

  # Include lang in the call to submit
  msg.submit(respond, [msg, lang, chatbot], [msg, chatbot])

  # And in the call to restart
  Restat.click(lambda:None, None, chatbot, queue=False)

demo.launch()