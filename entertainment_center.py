# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

Blade_Runner = media.Movie("Blade Runner", "A blade runner must pursue and try to terminate four replicants who stole a ship in space",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")


The_Lord_of_the_Rings_The_Return_of_the_King = media.Movie("The Lord of the Rings The Return of the King",
                                                           "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam",
                                                           "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
                                                           "https://www.youtube.com/watch?v=r5X-hFf6Bwo")


Body_of_Lies = media.Movie("Body of Lies", "A CIA agent on the ground in Jordan hunts down a powerful terrorist leader",
                           "https://upload.wikimedia.org/wikipedia/en/4/48/Body_of_lies_poster.jpg",
                           "https://www.youtube.com/watch?v=A4noCwwEUBA")


Django_Unchained = media.Movie("Django Unchained", "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a Mississippi plantation",
                               "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")


The_Revenant = media.Movie("The_Revenant", "A frontiersman on a fur trading expedition in the 1820s fights for survival after being mauled by a bear",
                           "https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg",
                           "https://www.youtube.com/watch?v=QRfj1VCg16Y")



movies = [Blade_Runner, The_Lord_of_the_Rings_The_Return_of_the_King, Body_of_Lies, Django_Unchained, The_Revenant]
fresh_tomatoes.open_movies_page(movies)


