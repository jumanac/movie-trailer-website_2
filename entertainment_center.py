import media
import fresh_tomatoes
import os
import ntpath


def get_running_path():
    head, tail = os.path.split(os.path.realpath(__file__))
    return head

exe_path = get_running_path()

# Create Son of God movie object
sonofgod = media.Movie(
    "Son of God",
    "Now, the larger-than-life story of The New Testament gets a larger-than" +
    "life treatment in the stand-alone feature SON OF GOD. Told with scope" +
    "and scale of an action epic, the film features powerful performances," +
    "exotic locales, dazzling effects and a rich orchestral score from" +
    "Oscar-winner Hans Zimmer. Portuguese actor Diogo Morgado portrays Jesus" +
    "as the film spans from his birth through his teachings, crucifixion" +
    "and ultimate resurrection. It marks the motion picture about Jesus" +
    "life since Passion of the Christ, released ten years ago",
    "sonofgod.jpg",
    "https://youtu.be/WcIXCok9HPg",
    "Feb 28, 2014",
    ["Diogo Morgado", "Amber Rose Revah", "Sebastian Knapp"]
)

# Create Transformers movie object
transformers = media.Movie(
    "Transformers",
    "Our world will be transformed when two races of robots--the Autobots" +
    "and the evil Decepticons (which are able to change into a variety of" +
    "objects, including cars, planes and other technological creations)" +
    "make Earth their final battleground. As the forces of seek the key to" +
    "ultimate power, last chance for survival rests in the hands of young" +
    "Sam Witwicky.",
    "transform.jpg",
    "https://youtu.be/gAjgXlvVexI",
    "Jul 03, 2007",
    ["Shia LaBeouf", "Megan Fox", "Josh Duhamel"])

# Create The Matrix movie object
matrix = media.Movie(
    "The Matrix",
    "In the near future, a  hacker named Neo discovers that all life on" +
    "Earth may be nothing more than a facade created by a malevolent" +
    "cyber-intelligence, for the purpose of placating us while our essence" +
    "is farmed to fuel the campaign of domination in the real world. He" +
    "joins like-minded warriors Morpheus and Trinity in their struggle to" +
    "overthrow the Matrix.",
    "matrix.jpg",
    "https://youtu.be/m8e-FF8MsqU",
    "Mar 31, 1999",
    ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]
)

# Create A Beautiful Mind movie object
mind = media.Movie(
    "A Beautiful Mind",
    "From the heights to the depths of depravity, John Forbes Nash," +
    "Jr. experiences it all. A mathematical genius, he made an astonishing" +
    "discovery early in his career and stood on the brink of international" +
    "acclaim. But the handsome Nash soon found himself on a painful" +
    "and harrowing journey of self-discovery once he was diagnosed with" +
    "schizophrenia. After years of struggle, he eventually triumphed over" +
    "this tragedy, and finally, late in life, received the Nobel Prize.",
    "mind.jpg",
    "https://youtu.be/aS_d0Ayjw4o",
    "Jan 04, 2002",
    ["Russell Crowe", "Ed Harris", "Jennifer Connelly"])

# Create Predator movie object
predator = media.Movie(
    "Predator",
    "Dutch and his group of commandos are hired by the CIA to rescue downed" +
    "airmen from guerillas in a Central American jungle. The mission goes" +
    "well but as they return they find that something is hunting them." +
    "Nearly invisible, it blends in with the forest, taking trophies from" +
    "the bodies of it's victims as it goes along. Occasionally seeing " +
    "through it's eyes, the audience sees it is an alien hunter," +
    "hunting them for sport, killing them off one at a time.",
    "predator.jpg",
    "https://youtu.be/Y1txEAywdiw",
    "Jun 12, 1987",
    ["Arnold Schwarzenegger", "Carl Weathers", "Kevin Peter"])

# Create Terminator Salvation movie object
terminator = media.Movie(
    "Terminator Salvation",
    "This anticipated new installment of The Terminator film franchise" +
    "is set in post-apocalyptic 2018. John Connor is the man fated to lead" +
    "the human resistance against Skynet and its army of Terminators. The" +
    "future that Connor was raised to believe in is altered in part by the" +
    "appearance of Marcus Wright, a stranger whose memory is of being on" +
    "death row. Connor must decide whether Marcus has been sent from the " +
    "future, or rescued from the past. As Skynet prepares its onslaught," +
    "Connor and Marcus both embark on an odyssey that takes them into the" +
    "heart of Skynet's operations, where they uncover the terrible secret" +
    "behind the possible annihilation of mankind",
    "terminator.jpg",
    "https://youtu.be/6GmLfivKQL8",
    "May 21, 2009",
    ["Christian Bale", "Sam Worthington", "Anton Yelchin"]
)

movies = [sonofgod, transformers, matrix, mind, predator, terminator]
fresh_tomatoes.open_movies_page(movies)
