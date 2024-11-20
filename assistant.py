from gtts import gTTS
import random

KB_limit = 9  # -1 for all
vocab = []

# Load nouns from the file
with open("nouns.txt", encoding="UTF-8") as f:
    vocab = f.read().splitlines()  # Fix: Load lines directly into the `vocab` list

# Text-to-speech function
def text_to_speech(text):
    tts = gTTS(text, lang="en")
    tts.save("nouns.mp3")
    print("Audio saved as 'nouns.mp3'.")

# Prepare vocabulary
vocabready = []

# Main program loop
if __name__ == "__main__":
    if KB_limit == -1 or KB_limit > len(vocab):  # Fix: Handle KB_limit correctly
        KB_limit = len(vocab)

    for _ in range(KB_limit):
        vocabready.append(random.choice(vocab))  # Randomly pick nouns from `vocab`

    text_to_speech(', '.join(vocabready))  # Join the nouns into a single string
    print("Text-to-speech operation completed.")
