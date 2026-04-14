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

    # Starter taste profile used for feature comparisons in scoring.
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.80,
        "acousticness": 0.30,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 72)
    print("Top Recommendations")
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
