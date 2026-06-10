# Music Library System

## Description
A Python-based music library system that tracks songs and provides global insights 
about artists and genres. Built for MusicTech Innovations as part of a music 
streaming service backend.

## Features
- Create song objects with a name, artist, and genre
- Track the total number of songs created
- View all unique artists and genres
- Count songs per genre e.g. `{"Rap": 5, "Rock": 1}`
- Count songs per artist e.g. `{"Beyonce": 17, "Jay-Z": 40}`

## Setup

```bash
git clone <your-repo-url>
cd python-music-library-system-lab
```

## Usage

```python
from song import Song

s1 = Song("Halo", "Beyonce", "Pop")
s2 = Song("Crazy in Love", "Beyonce", "Pop")
s3 = Song("99 Problems", "Jay-Z", "Rap")

print(Song.count)          # 3
print(Song.genres)         # ['Pop', 'Rap']
print(Song.artists)        # ['Beyonce', 'Jay-Z']
print(Song.genre_count)    # {'Pop': 2, 'Rap': 1}
print(Song.artists_count)  # {'Beyonce': 2, 'Jay-Z': 1}
```

## Class Structure

### Instance Attributes
| Attribute | Description |
|-----------|-------------|
| `name`    | Name of the song |
| `artist`  | Artist of the song |
| `genre`   | Genre of the song |

### Class Attributes
| Attribute       | Description |
|-----------------|-------------|
| `count`         | Total number of songs created |
| `genres`        | List of all unique genres |
| `artists`       | List of all unique artists |
| `genre_count`   | Dictionary of song counts per genre |
| `artists_count` | Dictionary of song counts per artist |

## Screenshot
<!-- Add a screenshot of your terminal output here -->

## Author
[Your Name]