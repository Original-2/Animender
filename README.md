# Animender
An AI that recommends anime based on personal history. You can use it here: https://discord.gg/h6nTTprMKd.

# model explanation
<br> ───────────────────── architecture ─────────────────────
<br> Input (1D array of shape (1000)) - Conveys which anime has been watched (1 for true, 0 for false)
<br> ↓
<br> Embedding (transforms 1D array to a 2D array of shape (1000, 10)) - Infers features about each anime
<br> ↓
<br> Dense (transforms 2D array of shape (1000, 10) to 2D array of shape (1000, 32) with ReLU) - Infers features about each anime
<br> ↓
<br> Fatten (transforms 2D array of shape (1000, 32) to 1D array of shape (3200) - This allows the next layer to work
<br> ↓
<br> Dense (1000 long array of probabilities of each 1000 animes being liked) - Predicts what anime suits the user with softmax
<br> ───────────────────── training ─────────────────────
<br> I got all animes a user has watched from the kaggle dataset https://www.kaggle.com/hernan4444/anime-recommendation-database-2020 then corrupted the data - this involved taking out one of the animes. The anime list remaining is the input. The target is the one that I had taken out. The batch is all of the possibilities of taking one out. This assumes every anime a user has finished was liked. This can be seen in the ratings given, with a mode of 8/10. Only the 1,000 most popular animes have been considered as the training time would increase with diminishing returns, in the future with better hardware I may allow more input features.

# To be done
* showing more lower popularity shows (adjusting it)
* bot parameters for better usage

# Contact me
email: dominic311dj@gmail.com

Please do not use this code without crediting me.
