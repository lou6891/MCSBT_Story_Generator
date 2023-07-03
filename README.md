# MCSBT_Story_Generator

## Index

- [Overview](#overview)
- [Requirements](#requirements)
    - [Google Cloud Setup](#google-cloud-setup)
    - [OpenAI Setup](#openai-setup)
- [File Descriptions](#file-descriptions)
- [How to Run](#how-to-run)
- [Usage](#usage)
- [Features](#features)
- [Possible Improvements](#possible-improvements)
- [The Project in Action](#the-project-in-action)

## Overview

This project integrates DialogFlow and OpenAI's GPT-4 for a multilingual chatbot. It starts the conversation using DialogFlow, which helps in getting the user's intent and understanding the parameters. Then, it uses OpenAI GPT-4 for more advanced language understanding and completion tasks.
Requirements

This project uses several Python libraries. Make sure to install the following dependencies:

pip install google-cloud-dialogflow
pip install google-cloud-translate
pip install google-auth
pip install gradio
pip install openai
pip install configparser

Also, you need to setup your Google Cloud and OpenAI credentials as described below:

### Google Cloud Setup

1. Create a Google Cloud Project.
2. Enable DialogFlow API and Cloud Translation API for your project.
3. Generate a service account key file (in JSON format) for your project.

### OpenAI Setup

1. Create an OpenAI account.
2. Generate an API key.

After setting up the above services, make sure to replace the placeholder values in the 'config.ini' file with your actual credentials.

## File Descriptions

1. main.py: The main Python script containing all the code.
2. config.ini: A configuration file where you put your DialogFlow project ID, file path to your Google Cloud service account key file, and OpenAI API Key.
3. index.html :  wrapper for the Gradio interface

## How to Run

To run the project, simply execute the main.py script:

The Gradio interface will launch in your default browser.

To use the HTML page, connect the iframe sourceto the adddress where the gradio inteface is running and launch it.

## Usage

1. Select a language from the dropdown menu.
2. Start the conversation by typing a welcome message.
3. The chatbot will guide you through the process of creating a story. It will ask you for details about the genre, main characters, location, and time period of the story. It will then use these details to create a unique script.
4. You can restart the conversation at any point by clicking the 'Restart' button.

## Features

1. Multilingual Support: You can chat with the bot in several languages.
2. User Intent Identification: The bot uses DialogFlow to understand your requests.
3. Script Creation: Based on the details you provide, the bot uses GPT-4 to create a unique script.

## Possible improvements

1. Multiuser Support: Currently Gradio is generating a single session token, to truly support multiple users it would be better to create a Python server that creates a session for each user when he/she loads the html page
2. Translation Improvements: Currently the code translates only the messages after the user selects a language, it could be beneficial to change the behavior so it translates the entire chat.
3. Current Implemetation has a bug for which once the user selects "begin" on dialogflow, the chatbot cannot be restarted until all input fields are filled. Possible solution by using fullfilment.


## The Project in action


*The Front End*
[*The Front End*](https://raw.githubusercontent.com/lou6891/MCSBT_Story_Generator/main/img/readme/img_1.png)

*Example of a Chat*

**USER:** hello

**DIALOGFLOW:** Hello there, I am the script generator AI, write "start" to begin or "begin" to start!

**USER:** begin

**DIALOGFLOW:** What genre would you like the story to be in?

**USER:** Action and romance

**DIALOGFLOW:** Where would you like for the story to be set?

**USER:** Indonesia

**DIALOGFLOW:** Amazing! And what time period is the story set in?

**USER:** During the 1960

**DIALOGFLOW:** Would you like me to add some props to the story?

**USER:** a broken clock that will be reveiled to have a secret linking the main protagonist past with her antagonist

**DIALOGFLOW:** Sounds great, now I need a few seconds to write your story

**ChatGPT:** 

**Title:** Tides of Destiny

**Genre:** Action/Romance

**Setting:** Indonesia, 1960

Characters:

- Captain Isabella "Bella" Morgan - A bold and fearless pirate woman, skilled in combat and navigation. She travels the world with her loyal companion, a dog named Rudder.
- Damien Blackwood - The charismatic and enigmatic antagonist, seeking an artifact tied to Bella's past.
- Amelia Monroe - A vibrant and independent archeologist who stumbles upon Bella's quest.
- John Reynolds - A cunning treasure hunter and former associate of Blackwood.
- Professor Harold Thompson - Amelia's mentor and an expert in Indonesian history and artifacts.

Props:

- Broken clock - A mysterious artifact that connects Bella and Damien's past.

Scene 1: Pirate Ship - Bella's Cabin

(Bella is sitting at a table, looking at a broken clock. The sound of waves crashing against the ship can be heard.)

Bella: (whispering) This broken clock... it holds the key to my past, Rudder.

(Rudder, the loyal dog, looks up at Bella, wagging its tail.)

Scene 2: Pirate Ship - Deck

(Bella stands at the helm of her ship, overlooking the vast ocean. She spots a distant island on the horizon.)

Bella: (determined) Indonesia... the land of mysteries and treasures. Let's set sail, Rudder. We have unfinished business with Damien Blackwood.

(The ship sets sail towards Indonesia.)

Scene 3: Indonesian Jungle

(Amelia Monroe, an archeologist, is digging in an excavation site. She uncovers an ancient map.)

Amelia: (excited) This map... it could lead to a hidden treasure!

(Suddenly, Damien Blackwood appears, snatching the map from Amelia.)

Damien: (smirking) Thank you, my dear. This will lead me to the ultimate power I seek.

(Amelia watches helplessly as Damien disappears into the jungle.)

Scene 4: Indonesian Port Town

(Bella and Rudder arrive at the bustling port town. They start to gather information about Damien's whereabouts.)

Bella: (to the local townsfolk) Have any of you seen a man named Damien Blackwood? He stole something precious from me.

(A local fisherman points Bella towards an inn.)

Scene 5: Indonesian Inn

(Bella enters the inn, spotting John Reynolds, a fellow treasure hunter, sitting at a table.)

Bella: (sly smile) Long time no see, John. Heard you've been working with Blackwood lately.

John: (nervously) Bella... I regret that association. But I do know where he's headed. Deep into the heart of the jungle.

(Bella clenches her fists.)

Scene 6: Indonesian Jungle - Ancient Temple Ruins

(Bella and Rudder navigate through treacherous terrain, finally arriving at the ancient temple ruins.)

Bella: (whispering) This place... it holds the answers I've been seeking.

(Suddenly, Damien appears, holding the broken clock in his hands.)

Damien: (mocking) You've come a long way, Bella. But it's too late. I have the key to your past, and soon the world shall bow at my feet.

(Bella and Damien engage in a fierce battle, with Rudder providing support.)

Scene 7: Ancient Temple - Hidden Chamber

(Bella manages to overpower Damien and reaches the hidden chamber.)

Bella: (gasping) The clock... it's here. The secret awaits.

(She pieces the broken clock together, revealing a hidden compartment.)

Scene 8: Hidden Compartment - Ancient Manuscript

(Inside the compartment, Bella finds an ancient manuscript detailing her forgotten lineage as the protector of a precious artifact.)

Bella: (astonished) This manuscript... it's my birthright. And the artifact... Damien seeks to harness its power for his own gain.

Scene 9: Ancient Temple - Final Battle

(Bella confronts Damien once again, ready to protect the artifact and the world from his grasp.)

Bella: (determined) You won't succeed, Damien! I will protect this world from your darkness.

(They engage in a final epic battle with high stakes.)

Scene 10: Indonesian Shoreline - Sunset

(Bella emerges victorious from the battle, clutching the artifact in her hands. Amelia and Professor Thompson join her.)

Amelia: (grateful) Thank you, Bella. You saved us all.

Professor Thompson: (in awe) The tales were true... the pirate woman and her faithful dog, destined to safeguard the artifact.

(Bella looks out at the ocean, feeling a sense of fulfillment.)

Bella: (grinning) Our journey isn't over yet, Rudder. There are still more treasures to uncover.

(Fade out as Bella, Rudder, Amelia, and Professor Thompson walk into the horizon.)

------------------------
And that concludes "Tides of Destiny," an action-packed adventure interwoven with romance and mystery.
