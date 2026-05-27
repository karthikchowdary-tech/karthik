# 🃏 AI Flashcard Generator

> Type a topic → AI generates Q&A flashcards → Quiz yourself → Track your score

A CLI-based learning tool built with Python, OpenAI API, OOP, and JSON persistence.  
Built as the **Day 6 Engineering Mini Project** of the 6-day Python bootcamp.

---

## Features

- **AI-powered card generation** — Enter any topic and get smart Q&A flashcards instantly
- **Interactive quiz mode** — Self-grade each answer; scores are tracked per card
- **JSON persistence** — Decks saved locally; re-run the app anytime to keep studying
- **Merge support** — Generate more cards for an existing topic without losing old ones
- **Modular structure** — Clean separation: models, utils, data, entry point

---

## Project Structure

```
flashcard_generator/
│
├── main.py                  # Entry point
│
├── models/
│   ├── __init__.py
│   └── flashcard.py         # Flashcard, Deck, DeckManager classes (OOP)
│
├── utils/
│   ├── __init__.py
│   ├── ai_generator.py      # OpenAI API integration (REST + requests)
│   ├── quiz.py              # Interactive quiz loop
│   └── menu.py              # CLI menu controller
│
├── data/                    # Auto-created; stores decks as JSON files
│   └── python_basics.json   # Example saved deck
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Skills Demonstrated

| Day | Skill | Where used |
|-----|-------|------------|
| Day 1 | Python basics, debugging, logging | `ai_generator.py` error handling |
| Day 2 | Lists, dicts, JSON | `flashcard.py` `to_dict/from_dict`, `data/` folder |
| Day 3 | Git workflow | This repo structure + commit history |
| Day 4 | REST APIs, `requests` | `ai_generator.py` → OpenAI API |
| Day 5 | OOP, modular architecture | `Flashcard`, `Deck`, `DeckManager` classes |
| Day 6 | Mini project integration | Everything wired together in `main.py` |

---

## Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/flashcard-generator.git
cd flashcard-generator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install & start Ollama (free, runs locally — no API key needed)

```bash
# Install from https://ollama.com, then:
ollama pull llama3.2     # download the model (~2GB)
ollama serve             # start the local server
```

> Want a different model? Edit `OLLAMA_MODEL` in `utils/ai_generator.py`.  
> Good options: `mistral`, `gemma2`, `phi3`, `llama3.2`

### 4. Run the app

```bash
python main.py
```

---

## Example Session

```
==================================================
   🃏  AI Flashcard Generator
==================================================
  Learn anything, faster.

  What would you like to do?

  [1] Generate new flashcard deck with AI
  [2] Study an existing deck
  [3] View all saved decks
  [4] View cards in a deck
  [5] Quit

  Enter choice (1-5): 1

  Enter a topic to generate flashcards for: Python decorators
  How many cards? (default: 5, max: 15): 5

  INFO: Generating 5 flashcards for topic: 'Python decorators'...
  ✅ Deck saved: Python decorators (5 cards)
  Added 5 new card(s). Deck 'Python decorators' now has 5 cards.

  Study this deck now? (y/n): y

  ──────────────────────────────────────────────────
  📚 Quiz: Python Decorators
  5 cards  |  Type your answer or press Enter to reveal
  ──────────────────────────────────────────────────

  Q1/5: What is a decorator in Python?
  Press Enter to see the answer...

  💡 Answer: A decorator is a function that wraps another function to extend
             its behaviour without modifying its source code.

  Did you get it right? (y/n): y
  ✅ Nice!
```

---

## Ideas to Extend This Project

- [ ] Add a `--topic` CLI flag using `argparse` to skip the menu
- [ ] Add spaced repetition: show weak cards more often
- [ ] Export decks to PDF or CSV
- [ ] Build a web UI with Flask
- [ ] Support multiple AI providers (Ollama, Gemini)

---

## Author

Built by **[Your Name]** as part of a 6-day Python Engineering Bootcamp.
