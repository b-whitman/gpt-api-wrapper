import openai
import time
import argparse
import random

openai.api_key_path = "./openai_key"

parser = argparse.ArgumentParser()
parser.add_argument("profile", help="Profile name")
parser.add_argument("--temperature", "-t", help="Temperature", default="0")
parser.add_argument("--maxtokens", "-m", help="Maximum tokens")

def main(profile, temperature, maxtokens):

    prompt_file = profile[0]
    model = profile[1]
    prompt_append = profile[2]
    result_append = profile[3]

    prompt = load_prompt(prompt_file)
    prompt = prompt + prompt_append
    responded = False
    wait_s = 5
    maxtokens = draw_max_tokens(default=maxtokens)
    print(f"Prompt length: {len(prompt)}")
    print(f"Prompt opens with '{prompt[:50]}' and closes with '{prompt[-50:]}'")
    while not responded:
        print("Attempting to connect...")
        try:
            response = openai.Completion.create(
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_tokens=maxtokens
                )
            responded = True
        except Exception as e:
            print(f"Connection failed:\n{e}")
            time.sleep(wait_s)
            wait_s += int(wait_s*0.5)
    result = response['choices'][0]['text']
    print(f"Result length: {len(result)}")
    result = prompt_append + result + result_append
    write_result(prompt_file, result)


def load_prompt(filename):
    with open(filename, "r") as file:
        text = file.read()
    if len(text) > 8000:
        start = len(text) - 8000
    else:
        start = 0
    return text[start:]

def write_result(filename, result):
    with open(filename, "r") as file:
        text = file.read()
    text = text + "\n" + result
    with open(filename, "w") as file:
        file.write(text)

def load_profile(profile_name):
    # [profile name]: ([prompt file],[model name],[prompt append],[result append])
    # May move this to separate JSON file
    profiles = {
        "chat_davinci": ("chat_prompt.txt","text-davinci-003","\nBot:","\nUser:"),
        "text_davinci": ("prompt.txt","text-davinci-003","",""),
        "text_curie": ("prompt.txt","text-curie-001","",""),
        "text_ada": ("prompt.txt","text-ada-001","",""),
        "code_davinci": ("code_prompt.txt","code-davinci-002","","")
    }
    profile = profiles[profile_name]
    return profile

def draw_max_tokens(default=None):
    """
    Experimental function for simulating a natural response length variance in chat_davinci.
    I usually just provide max tokens through command line arguments. Not sure a random selection technique is good here.
    """
    if default:
        max_tokens = default
    else:
        possible_values = [10,30,50,50,50,100,100,150,300]
        max_tokens = random.choice(possible_values)
    return max_tokens


if __name__ == "__main__":
    args = parser.parse_args()
    profile_name = args.profile
    temperature = float(args.temperature)
    if args.maxtokens:
        maxtokens = int(args.maxtokens)
    print(f"Profile name: {profile_name}")
    print(f"Temperature: {temperature}")
    print(f"Maximum tokens: {maxtokens}")
    profile = load_profile(profile_name)
    main(profile, temperature, maxtokens)
