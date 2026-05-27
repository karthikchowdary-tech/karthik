"""
models/flashcard.py
OOP: Flashcard and Deck classes (covers Day 5 - OOP + Architecture)
"""

import json
import os
from datetime import datetime


class Flashcard:
    """Represents a single Q&A flashcard."""

    def __init__(self, question: str, answer: str, topic: str):
        self.question = question
        self.answer = answer
        self.topic = topic
        self.created_at = datetime.now().isoformat()
        self.times_seen = 0
        self.times_correct = 0

    def mark_correct(self):
        self.times_seen += 1
        self.times_correct += 1

    def mark_wrong(self):
        self.times_seen += 1

    @property
    def score(self) -> str:
        if self.times_seen == 0:
            return "New"
        pct = int((self.times_correct / self.times_seen) * 100)
        return f"{pct}%"

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "answer": self.answer,
            "topic": self.topic,
            "created_at": self.created_at,
            "times_seen": self.times_seen,
            "times_correct": self.times_correct,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Flashcard":
        card = cls(data["question"], data["answer"], data["topic"])
        card.created_at = data.get("created_at", datetime.now().isoformat())
        card.times_seen = data.get("times_seen", 0)
        card.times_correct = data.get("times_correct", 0)
        return card


class Deck:
    """A named collection of Flashcards for one topic."""

    def __init__(self, topic: str):
        self.topic = topic
        self.cards: list[Flashcard] = []

    def add_card(self, card: Flashcard):
        self.cards.append(card)

    def __len__(self):
        return len(self.cards)

    def to_dict(self) -> dict:
        return {
            "topic": self.topic,
            "cards": [card.to_dict() for card in self.cards],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Deck":
        deck = cls(data["topic"])
        for card_data in data.get("cards", []):
            deck.add_card(Flashcard.from_dict(card_data))
        return deck


class DeckManager:
    """Handles saving and loading decks from the data/ folder."""

    DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

    def __init__(self):
        os.makedirs(self.DATA_DIR, exist_ok=True)

    def _path(self, topic: str) -> str:
        safe = topic.lower().replace(" ", "_")
        return os.path.join(self.DATA_DIR, f"{safe}.json")

    def save(self, deck: Deck):
        with open(self._path(deck.topic), "w") as f:
            json.dump(deck.to_dict(), f, indent=2)
        print(f"  ✅ Deck saved: {deck.topic} ({len(deck)} cards)")

    def load(self, topic: str) -> Deck | None:
        path = self._path(topic)
        if not os.path.exists(path):
            return None
        with open(path) as f:
            return Deck.from_dict(json.load(f))

    def list_topics(self) -> list[str]:
        topics = []
        for fname in os.listdir(self.DATA_DIR):
            if fname.endswith(".json"):
                topics.append(fname.replace(".json", "").replace("_", " "))
        return sorted(topics)
