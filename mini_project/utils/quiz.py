"""
utils/quiz.py
Interactive quiz loop — tests user on a deck of flashcards
"""

import random
from models import Deck, Flashcard


def run_quiz(deck: Deck):
    """Run an interactive quiz session on the given deck."""

    if len(deck) == 0:
        print("  ⚠️  This deck has no cards yet.")
        return

    print(f"\n{'─' * 50}")
    print(f"  📚 Quiz: {deck.topic.title()}")
    print(f"  {len(deck)} cards  |  Type your answer or press Enter to reveal")
    print(f"{'─' * 50}\n")

    cards = deck.cards.copy()
    random.shuffle(cards)

    correct = 0
    wrong = 0

    for i, card in enumerate(cards, 1):
        print(f"  Q{i}/{len(cards)}: {card.question}")
        input("  Press Enter to see the answer...")
        print(f"\n  💡 Answer: {card.answer}\n")

        while True:
            result = input("  Did you get it right? (y/n): ").strip().lower()
            if result in ("y", "n"):
                break
            print("  Please enter y or n.")

        if result == "y":
            card.mark_correct()
            correct += 1
            print("  ✅ Nice!\n")
        else:
            card.mark_wrong()
            wrong += 1
            print("  ❌ Keep practicing!\n")

        print(f"{'─' * 50}\n")

    # Summary
    total = correct + wrong
    pct = int((correct / total) * 100) if total > 0 else 0
    print(f"\n  🏁 Quiz Complete!")
    print(f"  Score: {correct}/{total} correct ({pct}%)")

    if pct == 100:
        print("  🎉 Perfect score! You've mastered this topic.")
    elif pct >= 70:
        print("  👍 Good job! A little more practice and you'll nail it.")
    else:
        print("  💪 Keep at it — repetition is the key to memory.")

    print()
