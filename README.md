# Animender
An AI that recommends anime based on personal history.

# To be done
* run and publish on kaggle
* make a github pages where people can use it
* make a logo
* improve model (will be hard as the model is already low dimension and still takes a long time to train)
* (maybe) make an app
<br><img src="https://media3.giphy.com/media/L3bj6t3opdeNddYCyl/giphy.gif" alt="Do You Want To Develop An App GIFs - Get the best GIF on GIPHY"/>![image]

# model explanation
<br>--------------------- architecture ---------------------
<br> Input (1000 long array) - This says weather or not eah anime has been watched by the user or not (1 for true, 0 for false)
<br> |
<br> v
<br> embedding (turns 1d array to a 2d array of shape (1000, 10)) - this infers features about each anime without knowing anything about them
<br> |
<br> v
<br> dense / fully connected (turns 2d array of (1000, 10) to (1000, 32) with relu) - this infers more information  from the previous layer and adds the relu activation function
<br> |
<br> v
<br> Fatten (turns that array 1d again, it is now 32000 long) - This allows the next layer to work
<br> |
<br> v
<br> Dense / fully connected (1000 long array of probabilities of each 1000 animes being liked) - predicts what anime suits the user (training method below) using softmax for probabilities
<br> --------------------- training ---------------------
<br> I got all animes a user has watched from the kaggle dataset https://www.kaggle.com/hernan4444/anime-recommendation-database-2020 and then I corrupted the data - this involved taking out one of the animes. The anime list remaining is the input. The target is the one that I had taken out. The batch is all of the possibilities of taking one out. This relies on the fact that every anime a user has finished was liked, however this makes sense as they would have likely dropped the show if they didn't. This can be seen in the ratings given, with a mode of 8/10. I only used the 1000 most popular animes as the training time would go up fast with diminishing returns. In the future if #i have access to better tech then I may allow more.

# contact me
email: dominic311dj@gmail.com
