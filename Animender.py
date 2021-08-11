import discord
import json
import numpy as np
import tensorflow as tf
import tflite

client = discord.Client()

f = open ('data.json', "r")
data = json.loads(f.read())

interpreter = tf.lite.Interpreter(model_path="optimised_model.tflite")
interpreter.allocate_tensors()

# just got all requirements

@client.event
async def on_message(message):
    try:
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        # only if activated
        if message.content.startswith('!choose'):
            code = message.content.split(" ")[-1] # getting the message and not the command
            code = str(np.base_repr(int(code, 36), 2)).zfill(1000)[::-1] # padding and flipping

            list = [] # turn the code to a list
            for i in code:
                list.append(i)

            test = np.expand_dims(list, axis=0).astype(np.float32)

            input_index = interpreter.get_input_details()[0]["index"]
            output_index = interpreter.get_output_details()[0]["index"]

            interpreter.set_tensor(input_index, test)
            interpreter.invoke()
            predictions = interpreter.get_tensor(output_index)[0] # tflite output

            titles = []
            watched = []
            for i in data:
                for j in i:
                    titles.append(j) # all titles
                    if list[i[j]] == "1":
                        watched.append(j) # previously watched titles

            preds = sorted(zip(predictions, titles), reverse=True) # (probability, title)

            finals = [] # filtering out watched

            for i in preds:
                if i[1] not in watched:
                    finals.append(i[1])
                    if len(finals) == 3:
                        break

            str_nice = "Your top 3 recommendations are: " # recommendations

            str_nice += str(finals[0])
            str_nice += ", "

            str_nice += str(finals[1])
            str_nice += ", and "

            str_nice += str(finals[2])

            await message.channel.send(str_nice) # send message
    except:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') # OAUTH TOKEN
