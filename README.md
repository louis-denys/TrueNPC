# TrueNPC Discord Bot

## Usage:
A Discord bot using a local version of Llama 3 installed via Ollama, as well as the `discord-py-interactions` library.
- This bot facilitates interactions between users and non-player characters (NPCs) within a Discord server dedicated to role-playing games.
- It requires [Ollama](https://ollama.com) to be installed on the machine in order to function.

### Commands:
#### 1. add_channel
*Usage:* Activates message recognition in the current channel by the AI, which will respond based on the identity you provide. (Note: a message preceded by a # will not be considered.)  
__**Identity:**__ A detailed description of the character to be played. A precise description of the character's personality will result in a more realistic portrayal.

#### 2. remove_channel
*Usage:* Deactivates message recognition in the current channel by the AI.

#### 3. general_context
*Usage:* Changes the system prompt.   
Default: "You are an assistant for a rolePlay discord server. Here are the text formats to use: \n**action** \n *thinking* \n'talking'. \nAnswer shortly."  
__**Context:**__ The context is the system prompt that will be provided to the AI from now on.

### Others
This repository is open access! Feel free to download and modify it as you wish. ;)
