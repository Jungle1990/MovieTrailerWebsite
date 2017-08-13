import webbrowser


class Movie(object):
    """Movie class will store title, storyline, poster image, trailer url"""

    def __init__(
            self, title, storyline,
            poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # open trailer url from webbrowser
        webbrowser.open(self.trailer_url)
