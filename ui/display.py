import streamlit as st
from core.pivot_letter import get_pivot_index

def render_word(word: str):
    pivot_idx = get_pivot_index(word)

    left = word[:pivot_idx]
    pivot = word[pivot_idx]
    right = word[pivot_idx + 1:]

    html = f"""
    <div class="immersion-wrapper">
        <div class="focus-bar"></div>
        <div class="orp-frame">
            <span class="orp-left">{left}</span>
            <span class="orp-pivot">{pivot}</span>
            <span class="orp-right">{right}</span>
        </div>
        <div class="focus-bar"></div>
    </div>
    """

    st.markdown(html, unsafe_allow_html=True)
