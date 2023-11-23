import openai
import json

openai.api_key = 'Your API KEY'

def nlp_area_of_interest(about):
    try:
        prompt = f" Generate Areas of interest for a user with the following about text: {about}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
        )
        # Parse and return the generated interests
        interests = response['choices'][0]['text'].strip().split('\n')
        print(interests)
        intes = []
        for i in interests:
            if i != '':
                intes.append(i)
        return intes

    except:
        return []
    
