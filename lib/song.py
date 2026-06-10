# Song class for MusicTech Innovations Music Library System
# Tracks individual song data and global insights across all songs


class Song:
    # Class attributes to track global song data
    count = 0           # Total number of songs created
    genres = []         # All unique genres
    artists = []        # All unique artists
    genre_count = {}    # Number of songs per genre e.g. {"Rap": 5, "Rock": 1}
    artists_count = {}  # Number of songs per artist e.g. {"Beyonce": 17}

    def __init__(self, name, artist, genre):
        # Instance attributes for each song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger all class methods when a new song is created
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artists_count()

    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count by 1 each time a song is created."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre=None):
        """Adds the song's genre to the genres list if it isn't already there (no duplicates)."""
        # When called from __init__ via classmethod, we need to look at last-added song
        # Using instance approach: genre passed directly or derived from count
        pass  # Overridden below with instance method

    @classmethod
    def add_to_artists(cls, artist=None):
        """Adds the song's artist to the artists list if not already present (no duplicates)."""
        pass  # Overridden below with instance method

    @classmethod
    def add_to_genre_count(cls, genre=None):
        """Increments the genre's count in genre_count dict; adds it with value 1 if new."""
        pass  # Overridden below with instance method

    @classmethod
    def add_to_artists_count(cls, artist=None):
        """Increments the artist's count in artists_count dict; adds it with value 1 if new."""
        pass  # Overridden below with instance method


# Override the class methods as instance-aware methods
# Re-defining cleanly using proper instance method + classmethod pattern

class Song:
    # ── Class Attributes ──────────────────────────────────────────────────────
    count = 0           # Total songs created
    genres = []         # Unique genres across all songs
    artists = []        # Unique artists across all songs
    genre_count = {}    # { genre: song_count }
    artists_count = {}  # { artist: song_count }

    # ── Constructor ───────────────────────────────────────────────────────────
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update all class-level tracking on creation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    def __repr__(self):
        return f"Song(name='{self.name}', artist='{self.artist}', genre='{self.genre}')"

    # ── Class Methods ─────────────────────────────────────────────────────────

    @classmethod
    def add_song_to_count(cls):
        """Increments total song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """Appends genre to genres list only if it doesn't already exist (unique values)."""
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """Appends artist to artists list only if not already present (unique values)."""
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates genre_count dictionary.
        Increments count for existing genre, or initialises it to 1 if new.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Updates artists_count dictionary.
        Increments count for existing artist, or initialises it to 1 if new.
        """
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1
