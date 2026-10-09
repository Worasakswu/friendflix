import base64
import re
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="ยินดีด้วยนะ เฟรน 🎓",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit chrome and stretch the component iframe over the whole viewport.
st.markdown(
    """
    <style>
    header[data-testid="stHeader"], #MainMenu, footer,
    [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
    html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {background: #000 !important; overflow: hidden !important;}
    .block-container, [data-testid="stMainBlockContainer"] {padding: 0 !important; max-width: 100% !important;}
    iframe {
        position: fixed !important; inset: 0 !important;
        width: 100vw !important; height: 100vh !important; height: 100dvh !important;
        border: 0 !important; z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def build_page(version: tuple) -> str:
    """Inline every assets/* image as a data URI so the page is self-contained."""
    html = (ROOT / "index.html").read_text(encoding="utf-8")

    def to_data_uri(match: re.Match) -> str:
        path = ROOT / match.group(0)
        if not path.exists():
            return match.group(0)
        mime = {".png": "image/png", ".glb": "model/gltf-binary"}.get(path.suffix.lower(), "image/jpeg")
        return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()

    return re.sub(r"assets/[\w.-]+\.(?:jpg|jpeg|png|glb)", to_data_uri, html)


# Cache key follows file changes, so edits show up without restarting the app.
version = tuple((p.name, p.stat().st_mtime_ns) for p in [ROOT / "index.html", *sorted((ROOT / "assets").iterdir())])
components.html(build_page(version), height=860, scrolling=True)
