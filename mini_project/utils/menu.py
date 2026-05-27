"""
utils/menu.py
Main CLI menu — ties all modules together (modular architecture, Day 5)
"""

from models import Deck, Flashcard, DeckManager
from utils.ai_generator import generate_flashcards
from utils.quiz import run_quiz


manager = DeckManager()


def show_menu():
    while True:
        print("  What would you like to do?\n")
        print("  [1] Generate new flashcard deck with AI")
        print("  [2] Study an existing deck")
        print("  [3] View all saved decks")
        print("  [4] View cards in a deck")
        print("  [5] Quit")
        print()

        choice = input("  Enter choice (1-5): ").strip()
        print()

        if choice == "1":
            _generate_deck()
        elif choice == "2":
            _study_deck()
        elif choice == "3":
            _list_decks()
        elif choice == "4":
            _view_deck()
        elif choice == "5":
            print("  Goodbye! Keep learning. 👋\n")
            break
        else:
            print("  ⚠️  Invalid choice. Please enter 1–5.\n")


def _generate_deck():
    topic = input("  Enter a topic to generate flashcards for: ").strip()
    if not topic:
        print("  ⚠️  Topic cannot be empty.\n")
        return

    while True:
        count_str = input("  How many cards? (default: 5, max: 15): ").strip()
        if count_str == "":
            count = 5
            break
        if count_str.isdigit() and 1 <= int(count_str) <= 15:
            count = int(count_str)
            break
        print("  ⚠️  Please enter a number between 1 and 15.")

    print()

    try:
        raw_cards = generate_flashcards(topic, count)
    except (EnvironmentError, PermissionError, ConnectionError, RuntimeError, ValueError) as e:
        print(str(e))
        print()
        return

    # Check if deck already exists; merge if so
    deck = manager.load(topic) or Deck(topic)
    existing_questions = {c.question for c in deck.cards}

    added = 0
    for item in raw_cards:
        q = item.get("question", "").strip()
        a = item.get("answer", "").strip()
        if q and a and q not in existing_questions:
            deck.add_card(Flashcard(q, a, topic))
            added += 1

    manager.save(deck)
    print(f"  Added {added} new card(s). Deck '{topic}' now has {len(deck)} cards.\n")

    study_now = input("  Study this deck now? (y/n): ").strip().lower()
    print()
    if study_now == "y":
        run_quiz(deck)


def _study_deck():
    topics = manager.list_topics()
    if not topics:
        print("  No decks yet. Generate one first!\n")
        return

    _print_topic_list(topics)
    choice = input("  Enter deck number: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(topics)):
        print("  ⚠️  Invalid choice.\n")
        return

    topic = topics[int(choice) - 1]
    deck = manager.load(topic)
    if deck:
        run_quiz(deck)


def _list_decks():
    topics = manager.list_topics()
    if not topics:
        print("  No decks saved yet.\n")
        return

    print("  📂 Saved Decks:\n")
    for i, topic in enumerate(topics, 1):
        deck = manager.load(topic)
        count = len(deck) if deck else 0
        print(f"  {i}. {topic.title()}  ({count} cards)")
    print()


def _view_deck():
    topics = manager.list_topics()
    if not topics:
        print("  No decks yet.\n")
        return

    _print_topic_list(topics)
    choice = input("  Enter deck number: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(topics)):
        print("  ⚠️  Invalid choice.\n")
        return

    topic = topics[int(choice) - 1]
    deck = manager.load(topic)
    if not deck:
        print("  ❌ Could not load deck.\n")
        return

    print(f"\n  📖 Deck: {deck.topic.title()} ({len(deck)} cards)\n")
    for i, card in enumerate(deck.cards, 1):
        print(f"  Q{i}: {card.question}")
        print(f"  A:  {card.answer}")
        print(f"  Score: {card.score} ({card.times_seen} seen)\n")


def _print_topic_list(topics: list[str]):
    print("  Available decks:\n")
    for i, topic in enumerate(topics, 1):
        print(f"  [{i}] {topic.title()}")
    print()
