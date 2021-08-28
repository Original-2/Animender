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
            code = message.content.split(" ")[1] # getting the message and not the command
            if len(message.content.split(" ")) == 3:
                try:
                    num = int(message.content.split(" ")[2])
                    if num > 50:
                        num = 5
                except:
                    num = 3
            else:
                num = 3
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
            predscore = []

            for i in preds:
                if i[1] not in watched:
                    finals.append(i[1])
                    predscore.append(i[0])
                    if len(finals) == num:
                        break

            str_nice = f"Your top {num} recommendations are: " # recommendations

            for i in range(len(finals)):
                if finals[-1] == finals[i]:
                    str_nice += str(finals[i])
                    str_nice += " ("
                    str_nice += str(round(predscore[i] * 100, 2))
                    str_nice += "%)"
                elif finals[-2] == finals[i]:
                    str_nice += str(finals[i])
                    str_nice += " ("
                    str_nice += str(round(predscore[i] * 100, 2))
                    str_nice += "%) and "
                else:
                    str_nice += str(finals[i])
                    str_nice += " ("
                    str_nice += str(round(predscore[i] * 100, 2))
                    str_nice += "%), "
            await message.channel.send(str_nice) # send message
    except:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX') # OAUTH TOKEN
