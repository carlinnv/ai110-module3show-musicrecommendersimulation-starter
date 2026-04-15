"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Named taste profiles for quick simulation runs.
    user_profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.85,
            "acousticness": 0.20,
            "danceability": 0.85,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
            "acousticness": 0.85,
            "tempo_bpm": 80,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.90,
            "acousticness": 0.10,
            "valence": 0.35,
        },
        # Edge case: no preferences produces ties at score 0.0.
        "Empty Profile": {},
        # Adversarial: valid keys but out-of-range targets to force unexpected closeness behavior.
        "Out-of-Range Numeric Values": {
            "genre": "pop",
            "mood": "happy",
            "energy": 3.5,
            "acousticness": -1.2,
            "tempo_bpm": 500,
            "valence": 2.0,
            "danceability": -0.6,
        },
        # Edge case: contradictory target signals can reveal weight dominance.
        "Conflicting Vibes": {
            "genre": "rock",
            "mood": "chill",
            "energy": 0.95,
            "acousticness": 0.95,
            "tempo_bpm": 70,
            "valence": 0.15,
            "danceability": 0.90,
        },
        # Adversarial: unknown category labels and ignored extra key.
        "Unknown Labels and Noise": {
            "genre": "hyperfolk",
            "mood": "astral",
            "energy": 0.60,
            "acousticness": 0.40,
            "favorite_decade": "2090s",
        },
    }

    active_profile = "Chill Lofi"  # Change this to test different profiles quickly.
    user_prefs = user_profiles[active_profile]

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 72)
    print("Top Recommendations")
    print(f"Profile: {active_profile}")
    print("=" * 72)

    for rank, rec in enumerate(recommendations, start=1):
        # Expected tuple shape from recommend_songs: (song, score, explanation)
        song, score, explanation = rec
        reasons = [reason.strip() for reason in explanation.split(";") if reason.strip()]

        print(f"\n[{rank}] {song['title']}")
        print(f"    Final Score : {score:.2f}")
        print("    Reasons     :")
        for reason in reasons:
            print(f"      - {reason}")

    print("\n" + "=" * 72)


if __name__ == "__main__":
    main()
