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


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!choose'):
        code = message.content.split(" ")[-1]
        code = str(np.base_repr(int(code, 36), 2)).zfill(1000)[::-1]

        list = []
        for i in code:
            list.append(i)
        #
        test = np.expand_dims(list, axis=0).astype(np.float32)

        input_index = interpreter.get_input_details()[0]["index"]
        output_index = interpreter.get_output_details()[0]["index"]

        interpreter.set_tensor(input_index, test)
        interpreter.invoke()
        predictions = interpreter.get_tensor(output_index)[0]

        titles = []
        watched = []
        for i in data:
            for j in i:
                titles.append(j)
                if list[i[j]] == "1":
                    watched.append(j)

        preds = sorted(zip(predictions, titles), reverse=True)

        finals = []

        for i in preds:
            if i[1] not in watched:
                finals.append(i[1])
                if len(finals) == 3:
                    break

        str_nice = "Your top 3 recommendations are: "

        str_nice += str(finals[0])
        str_nice += ", "

        str_nice += str(finals[1])
        str_nice += ", and "

        str_nice += str(finals[2])

        await message.channel.send(str_nice)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('ODc0MzEwMjc4MjcwMDUwNDE1.YRFG5g.GrCJ1sUOITvzXd7v1jMUZyYU-Ow')