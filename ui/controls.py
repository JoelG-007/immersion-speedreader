import streamlit as st

def reader_controls():
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("▶ Play"):
            st.session_state.playing = True

    with col2:
        if st.button("⏸ Pause"):
            st.session_state.playing = False

    with col3:
        if st.button("Restart"):
            st.session_state.index = 0

    st.session_state.wpm = st.slider("Speed (WPM)", 100, 1000, 300)
