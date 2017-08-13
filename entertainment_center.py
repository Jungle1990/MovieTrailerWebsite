import media
import fresh_tomatoes

# init 6 instances of movie class
manchester_by_the_sea = media.Movie(
    "Manchester by the Sea",
    "A man looks after his teenage nephew after his brother dies",
    "https://upload.wikimedia.org/wikipedia/en/d/de/Manchester_by_the_Sea.jpg",
    "https://www.youtube.com/watch?v=A5MXyUWMo3w")

la_la_land = media.Movie(
    "La La Land",
    """starring Ryan Gosling and Emma Stone as a musician and
     an aspiring actress who meet and fall in love in Los Angeles""",
    "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
    "https://www.youtube.com/watch?v=42nAxYtmwnY")

brave_heart = media.Movie(
    "Braveheart",
    """A 13th-century Scottish warrior led the Scots
     in the First War of Scottish Independence
     against King Edward I of England""",
    "https://upload.wikimedia.org/wikipedia/en/5/55/Braveheart_imp.jpg",
    "https://www.youtube.com/watch?v=yBK7OMRpOHs")

enders_game = media.Movie(
    "Ender's Game",
    """An unusually gifted child is sent to an advanced military
     academy in outer space to prepare for a future alien invasion""",
    "https://upload.wikimedia.org/wikipedia/en/8/8c/Ender%27s_Game_poster.jpg",
    "https://www.youtube.com/watch?v=vP0cUBi4hwE")

roman_holiday = media.Movie(
    "Roman Holiday",
    "It stars a reporter and a royal princess out to see Rome on her own",
    "https://upload.wikimedia.org/wikipedia/en/b/b7/Roman_holiday.jpg",
    "https://www.youtube.com/watch?v=9GzCG6lpFUw")

the_hitchhikers_guide_to_the_galaxy = media.Movie(
    "The Hitchhiker's Guide to the Galaxy",
    """It follows the misadventures of the last surviving man
     following the demolition of the planet Earth by a Vogon
     constructor fleet to make way for a hyperspace bypass""",
    "https://upload.wikimedia.org/wikipedia/en/7/7a/Hitchhikers_guide_to_the_galaxy.jpg",  # noqa
    "https://www.youtube.com/watch?v=MbGNcoB2Y4I")

# construct a movie list
movies = [
        manchester_by_the_sea, la_la_land, brave_heart,
        enders_game, roman_holiday, the_hitchhikers_guide_to_the_galaxy]

# call fresh_tomatoes to generate html from given movie list
fresh_tomatoes.open_movies_page(movies)
