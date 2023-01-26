# Introduction

This is a simple Python wrapper for OpenAI's GPT-3 API text completion interface.

# Setup

1. Create a file named "openai_key" in the root directory. Paste your OpenAI API key into this file. The path to this file is given to the OpenAI Python SDK to authenticate.

# Use

This script provides a simple command line argument interface. You provide the input prompt in the appropriate file (`prompt.txt`,`chat_prompt.txt`, or `code_prompt.txt`). Save the prompt, then run the script. Script run calls identify the output profile (chat, code, or text), the temperature, and the maximum length of the response in tokens. Here is a format example:

`python api-access.py [profile name] -t [temperature] -m [maximum number of tokens]`

The script will call the API using your provided API key, output some information about the prompt and parameters, wait for a response, and push the response into the prompt file. Think of it as a bare-bones implementation of the ChatGPT interface, where instead of clicking a button to get a response you "save" your prompt text and issue the run command.

### Available profiles:

text_davinci (I/O: `prompt.txt`)

chat_davinci (I/O: `chat_prompt.txt`)

code_davinci (I/O: `code_prompt.txt`)

text_curie (I/O: `prompt.txt`)

text_ada (I/O: `prompt.txt`)

OpenAI has great, thorough documentation about best practices in text completion prompt engineering [here.](https://beta.openai.com/docs/guides/completion/introduction)

I spend most of my time using the DaVinci models, but OpenAI notes the less powerful Curie and Ada models can be very useful for certain tasks (e.g. classifiers with few-shot training prompts), and they are orders of magnitude cheaper than DaVinci. The typical pattern seems to be to develop with DaVinci and refine down to less powerful models if possible.

Temperature determines the predictability of the response, and is given as any number between 0 and 1. A temperature of 0 is best for any question where there is only one correct response, whereas higher temperatures are good when you want more creativity or variability.

Maximum tokens allows you to control approximately how long the response will be. I tend to start on the lower end (50-100) to figure out if I've actually engineered my prompt well, then adjust as needed to get a satisfying response.

I have found GPT-3 helpful as a personal chat bot for planning my day and bouncing ideas off of. You can really get creative with the prompts, as well. For instance, you can structure the prompt to elicit idea feedback or critiques from GPT-3. There are other available API calls built into the Python SDK, such as text editing and image generation, and I think those would be great directions to go with this foundational script. Experiment, have fun, and let me know if you find anything cool!