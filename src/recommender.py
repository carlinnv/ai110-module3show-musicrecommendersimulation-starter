from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file into typed dictionaries."""
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": int(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and return reasons."""
    score = 0.0
    reasons: List[str] = []

    def add_exact_match(feature_name: str, user_key: str, song_key: str, points: float) -> None:
        """Add fixed points for exact categorical feature matches."""
        nonlocal score
        if user_key in user_prefs and str(user_prefs[user_key]).strip().lower() == str(song[song_key]).strip().lower():
            score += points
            reasons.append(f"{feature_name} match (+{points:.1f})")

    def add_numeric_match(feature_name: str, user_key: str, song_key: str, max_points: float, tolerance: float) -> None:
        """Add proportional points based on numeric closeness to target."""
        nonlocal score
        if user_key not in user_prefs:
            return

        target = float(user_prefs[user_key])
        value = float(song[song_key])
        closeness = max(0.0, 1.0 - (abs(value - target) / tolerance))
        points = closeness * max_points
        if points > 0:
            score += points
            reasons.append(f"{feature_name} close match (+{points:.1f})")

    add_exact_match("genre", "genre", "genre", 2.0)
    add_exact_match("mood", "mood", "mood", 2.0)
    add_numeric_match("energy", "energy", "energy", 3.0, 0.5)
    add_numeric_match("acousticness", "acousticness", "acousticness", 1.5, 0.7)
    add_numeric_match("tempo", "tempo_bpm", "tempo_bpm", 1.5, 40.0)
    add_numeric_match("valence", "valence", "valence", 1.0, 0.5)
    add_numeric_match("danceability", "danceability", "danceability", 1.0, 0.5)

    if not reasons:
        reasons.append("no strong preference match")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top-k recommendations."""
    scored_songs = [
        (song, score, "; ".join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]
