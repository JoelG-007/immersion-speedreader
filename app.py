import streamlit as st
from streamlit_autorefresh import st_autorefresh
from core.text_loader import load_txt
from core.word_parser import parse_words
from core.reader_engine import get_delay
from ui.display import render_word
from utils.pdf_reader import read_pdf

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Immersion", layout="wide")

# ---------------- CSS ----------------
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
DEFAULTS = {
    "words": [],
    "index": 0,
    "playing": False,
    "wpm": 350,
    "immersion": False,
    "raw_text": ""      # stores pasted text safely across reruns (Since the text gets cleared once entering or exiting immersion mode)
}

for k, v in DEFAULTS.items():
    st.session_state.setdefault(k, v)

# ---------------- TOP BAR ----------------
with st.container():
    _, col = st.columns([8, 1])
    with col:
        if st.button("Enter/Exit Immersion Mode", use_container_width=True):
            st.session_state.immersion = not st.session_state.immersion

# ---------------- HEADER (NORMAL MODE ONLY) ----------------
if not st.session_state.immersion:
    st.markdown(
        "<h1 style='text-align:center;'>Immersion</h1>"
        "<p style='text-align:center; opacity:0.7;'>RSVP Speed Reading</p>",
        unsafe_allow_html=True
    )

# ---------------- LAYOUT ----------------
# Normal mode: Controls + Input + Reader
# Immersion mode: Controls + Reader
if st.session_state.immersion:
    controls_col, output_col = st.columns([1, 4])
else:
    controls_col, input_col, output_col = st.columns([1, 2, 3])

# ================= CONTROLS =================
with controls_col:
    with st.expander("⚙ Controls", expanded=True):

        if st.button("▶ Play", use_container_width=True):
            st.session_state.playing = True

        if st.button("⏸ Pause", use_container_width=True):
            st.session_state.playing = False

        if st.button("🔁 Restart", use_container_width=True):
            st.session_state.index = 0
            st.session_state.playing = False

        if st.button("Clear Input", use_container_width=True):
            st.session_state.words = []
            st.session_state.index = 0
            st.session_state.playing = False
            st.session_state.raw_text = ""
            st.session_state.immersion = False

        speed_mode = st.radio(
            "Reading Speed",
            ["Beginner", "Student", "Advanced"],
            index=1
        )

        SPEED_MAP = {
            "Beginner": 200,
            "Student": 350,
            "Advanced": 600
        }

        st.session_state.wpm = SPEED_MAP[speed_mode]

# ================= INPUT (NORMAL MODE ONLY) =================
if not st.session_state.immersion:
    with input_col:
        st.markdown("### Input")

        mode = st.radio(
            "Input Method",
            ["Upload File", "Paste Text"],
            horizontal=True
        )

        # -------- Upload file --------
        if mode == "Upload File":
            file = st.file_uploader("Upload TXT or PDF", type=["txt", "pdf"])
            if file:
                text = load_txt(file) if file.name.endswith(".txt") else read_pdf(file)
                st.session_state.words = parse_words(text)
                st.session_state.index = 0
                st.session_state.playing = False
                st.success(f"{len(st.session_state.words)} words loaded")

        # -------- Paste text --------
        else:
            st.text_area(
                "Paste your text below",
                height=220,
                placeholder="Paste your article, notes, or assignment here...",
                key="raw_text"
            )

            if st.button("Load Text"):
                if st.session_state.raw_text.strip():
                    st.session_state.words = parse_words(st.session_state.raw_text)
                    st.session_state.index = 0
                    st.session_state.playing = False
                    st.success(f"{len(st.session_state.words)} words loaded")

# ================= OUTPUT / READER =================
with output_col:
    reader_box = st.container()

    # No text loaded
    if not st.session_state.words:
        if not st.session_state.immersion:
            st.info("Load text and press Play")
        st.stop()

    # End of text reached
    if st.session_state.index >= len(st.session_state.words):
        st.session_state.playing = False
        if not st.session_state.immersion:
            st.success("End of text reached")
        st.stop()

    # Current word
    word = st.session_state.words[st.session_state.index]
    delay = get_delay(word, st.session_state.wpm)

    with reader_box:
        render_word(word)

    # Advance reader
    if st.session_state.playing:
        st_autorefresh(
            interval=int(delay * 1000),
            key="reader_clock"
        )
        st.session_state.index += 1
