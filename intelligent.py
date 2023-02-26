import openai
import os
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
from twilio.rest import Client

# Retrieve the OpenAI API key from an environment variable
openai.api_key = os.environ.get('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')

# Define the function to generate a response using the OpenAI API
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

# Define the Twilio WhatsApp bot
app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_message = request.values.get('Body', '').lower()
    response = MessagingResponse()

    if 'hello' in incoming_message:
        response.message('Hello, how can I help you?')
    elif 'help' in incoming_message:
        response.message('Please provide more details about your problem.')
    elif 'developer' in incoming_message:
        response.message('The developer of this bot is Jarferh haroun.')
    elif 'programmer' in incoming_message:
        response.message('The developer of this bot is Jarferh haroun.')
    elif 'creator' in incoming_message:
        response.message('The developer of this bot is Jarferh haroun.')
    else:
        # Use OpenAI to generate a response
        prompt = f"User: {incoming_message}\nBot:"
        message = generate_response(prompt)

        # Send the response to the user
        response.message(message)

    return str(response)

if __name__ == '__main__':
    app.run()
