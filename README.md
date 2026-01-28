# Immersion
**Visual RSVP Speed Reading App**

## Inspiration

I was casually scrolling through Instagram when I came across a reel about  
**RSVP (Rapid Serial Visual Presentation)** - a technique where words are shown one at a time at a fixed point on the screen.

What caught my attention was that:
- I was reading **much faster**
- My eyes were not moving left and right
- I could still **retain the information**
- It felt less tiring compared to reading long paragraphs

As a student who already reads fast, I usually find it **boring and mentally exhausting** to scroll through chunks of pages, PDFs, or notes. That’s when I thought -
**why not build a simple tool that makes reading faster, cleaner, and less tiring?**

This project is the result of that idea.

---

## What is Immersion?

**Immersion** is a visual speed-reading app based on the RSVP technique.

Instead of reading paragraphs:
- Words are displayed **one at a time**
- A **fixed pivot letter (ORP)** is highlighted to reduce eye movement
- The reader stays focused at a single point
- Reading speed can be adjusted based on comfort

It’s designed to reduce:
- Eye strain
- Mental fatigue
- Boredom from long reading sessions

---

## Features

- Upload **TXT or PDF** files  
- Paste custom text (notes, articles, assignments)  
- RSVP-style word-by-word reading  
- Fixed pivot letter (Optimal Recognition Point)  
- Speed presets: Beginner, Student, Advanced  
- Play / Pause / Restart controls  
- Immersion mode (Controls + Reader only)  
- Clean, minimal dark UI  

---

## Why Streamlit?

I used **Streamlit** as the frontend because:
- I wanted to focus on **logic and functionality**, not UI boilerplate
- Building a full frontend (React, CSS, routing, state) felt unnecessary
- Streamlit made it **quick to prototype and demo**
- It allowed me to iterate faster and keep the project lightweight

This was a **productivity-first decision**, not laziness (maybe a little....).

---

## Tech Stack

- **Python**
- **Streamlit** – frontend & UI rendering
- **HTML + CSS** – custom ORP layout and styling
- **Session State** – reader state management
- **PDF parsing** – text extraction from PDFs

---

## Project Structure (Simplified)

```
.
├── app.py                      # Main Streamlit app
├── core/
│   ├── text_loader.py          # TXT file reader
│   ├── word_parser.py          # Text → words
│   ├── reader_engine.py        # WPM & delay logic
│   └── pivot_letter.py         # ORP calculation
├── ui/
│   └── display.py              # Word rendering (ORP layout)
├── utils/
│   └── pdf_reader.py           # PDF text extraction
├── assets/
│   └── styles.css              # Styling & layout
└── README.md

```
## How to Run

```bash
Copy code
pip install streamlit streamlit-autorefresh
streamlit run app.py

```

## Disclaimer
This is a minor project built for:
Learning
Experimentation
Improving personal productivity

It’s not meant to replace traditional reading, but to offer a faster alternative when skimming, revising, or consuming large amounts of text.

## Final Thoughts
This project started from curiosity and a random reel -
and turned into something genuinely useful for my own study workflow.

If it helps even one other student read better and feel less exhausted, that’s already a win...