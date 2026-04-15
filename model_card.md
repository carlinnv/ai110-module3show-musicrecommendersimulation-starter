# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeShift Recommender**

---

## 2. Intended Use  

This recommender suggests songs from a small catalog by using user preferences like genre, mood, and audio traits. It assumes users can describe what they want in simple labels. 

---

## 3. How the Model Works  

Each song gets points when it matches the user profile, and the exact genre and mood matches add fixed points. Features like energy, acousticness, tempo, valence, and danceability add points based on closeness. The database of songs are then sorted by total score and the top results are returned. I changed the weights to test bias: genre was doubled and acousticness was cut in half.

---

## 4. Data  

The dataset has 18 songs and includes genres like pop, lofi, rock, ambient, jazz, synthwave, and more. Moods include happy, chill, intense, focused, and relaxed. I used AI to generate 10 songs in addition to the original song database. Unfortunately, the catalog is still small, so many music styles and cultures are missing.

---

## 5. Strengths  

It works well when a user has clear preferences. High-Energy Pop, Chill Lofi, and Deep Intense Rock gave believable top songs. The scoring reacts clearly when energy or genre changes. The reason strings help explain why a song was ranked high.

---

## 6. Limitations and Bias 

The biggest weakness is filter bubble behavior. Exact genre matching has a strong weight, so similar styles might be pushed down, which can make results repetitive and reduce discovery. Users with mixed or niche taste may get weaker matches. Furthermore, my model also ignores context like lyrics, language, and listening history.

---

## 7. Evaluation  

I tested High-Energy Pop, Chill Lofi, Deep Intense Rock, Empty Profile, Out-of-Range Numeric Values, Conflicting Vibes, and Unknown Labels and Noise. I checked if top songs matched the intended vibe, and also checked whether explanation text matched the strongest scoring features. The surprising part was how much exact genre matching dominated ranking. Another surprise was that weird input values still returned usable results by falling back to other features.

---

## 8. Future Work  

I want to add a diversity step so top results are less repetitive. I want softer genre similarity, not only exact label matches. I also want negative preferences, like "less intense" or "not acoustic." Better explanations could show a feature-by-feature score breakdown. Long term, I would add more songs and richer user profile options.

---

## 9. Personal Reflection  

My biggest learning moment was finding out that the edge cases still gave good outputs. This showed me that it is indeed important to check edge cases just incase they do not give plausible results. AI tools helped me by providing feedback on my proposed outlines. I double checked them at most steps, especially during implementation. I was also surprised that such a simple point-based algorithm could still feel like a real recommender. Even without deep AI, matching a few meaningful features made the results feel personal and believable. If I extend this project, the first thing I would try is a diversity re-ranking step so the top results are less repetitive.