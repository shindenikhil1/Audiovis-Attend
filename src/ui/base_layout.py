import streamlit as st


def style_background_home():
    """Clean, editorial home-page canvas for AudioVis Attend."""
    st.markdown("""
    <style>
      .stApp { background: #f6f7f4 !important; }
      [data-testid="stAppViewContainer"] > .main { background: #f6f7f4; }
    </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    """Neutral dashboard background; shared styles live in style_base_layout."""
    st.markdown("""
    <style>
      .stApp { background: #f6f7f4 !important; }
      [data-testid="stAppViewContainer"] > .main { background: #f6f7f4; }
    </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

      :root {
        --cl-ink: #17231d;
        --cl-muted: #69766e;
        --cl-paper: #f6f7f4;
        --cl-white: #ffffff;
        --cl-green: #d7f36a;
        --cl-green-dark: #30451b;
        --cl-line: #e3e8df;
      }

      #MainMenu, footer, header { visibility: hidden; }
      .stApp, [data-testid="stAppViewContainer"] { background: var(--cl-paper) !important; }
      .block-container { max-width: 1180px; padding: 1.7rem 2rem 2.5rem !important; }

      html, body, [class*="css"], p, label, input, textarea, button, select {
        font-family: 'DM Sans', sans-serif;
      }

      h1, h2, h3, h4 {
        font-family: 'Manrope', sans-serif !important;
        color: var(--cl-ink);
        letter-spacing: -0.035em;
      }
      h1 { font-size: clamp(2rem, 4vw, 3.1rem) !important; line-height: 1.08 !important; }
      h2 { font-size: 1.8rem !important; line-height: 1.15 !important; }
      h3 { font-size: 1.25rem !important; }
      p, [data-testid="stMarkdownContainer"] { color: var(--cl-ink); }

      /* Main Streamlit content surfaces */
      [data-testid="stVerticalBlockBorderWrapper"] {
        background: var(--cl-white);
        border: 1px solid var(--cl-line);
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(23, 35, 29, .035);
      }
      [data-testid="stExpander"] {
        border: 1px solid var(--cl-line);
        border-radius: 14px;
        background: white;
      }
      [data-testid="stMetric"] {
        background: white;
        border: 1px solid var(--cl-line);
        border-radius: 16px;
        padding: 1rem;
      }
      [data-testid="stMetricLabel"] { color: var(--cl-muted); }
      [data-testid="stDataFrame"], [data-testid="stTable"] {
        border: 1px solid var(--cl-line);
        border-radius: 14px;
        overflow: hidden;
      }
      [data-testid="stCameraInput"], [data-testid="stFileUploader"] {
        border: 1px dashed #bdc9b8;
        border-radius: 16px;
        background: #fbfcf8;
        padding: .5rem;
      }

      /* Inputs */
      [data-testid="stTextInput"] input,
      [data-testid="stNumberInput"] input,
      [data-testid="stTextArea"] textarea,
      [data-testid="stSelectbox"] [data-baseweb="select"] > div,
      [data-testid="stDateInput"] input,
      [data-testid="stTimeInput"] input {
        border-radius: 10px !important;
        border-color: #d8e0d5 !important;
        background: #fff !important;
        color: var(--cl-ink) !important;
      }
      [data-testid="stTextInput"] input:focus,
      [data-testid="stTextArea"] textarea:focus {
        border-color: #718b42 !important;
        box-shadow: 0 0 0 1px #718b42 !important;
      }

      /* Buttons */
      div.stButton > button,
      div[data-testid="stDownloadButton"] button {
        border-radius: 11px !important;
        min-height: 42px;
        padding: .55rem 1rem !important;
        font-weight: 700 !important;
        border: 1px solid transparent !important;
        transition: transform .16s ease, background .16s ease,
                    box-shadow .16s ease;
      }

      /* Primary buttons: dark background with white text */
      div.stButton > button[kind="primary"],
      div[data-testid="stDownloadButton"] button {
        background: #17231d !important;
        color: #ffffff !important;
        border-color: #17231d !important;
      }
      div.stButton > button[kind="primary"] *,
      div[data-testid="stDownloadButton"] button * {
        color: #ffffff !important;
        fill: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
      }

      /* Secondary buttons: lime background with dark text */
      div.stButton > button[kind="secondary"] {
        background: #d7f36a !important;
        color: #17231d !important;
        border-color: #d7f36a !important;
      }
      div.stButton > button[kind="secondary"] * {
        color: #17231d !important;
        fill: #17231d !important;
        -webkit-text-fill-color: #17231d !important;
      }

      /* Tertiary buttons: light background with dark text */
      div.stButton > button[kind="tertiary"] {
        background: #edf0e9 !important;
        color: #17231d !important;
        border-color: #dce4d8 !important;
      }
      div.stButton > button[kind="tertiary"] * {
        color: #17231d !important;
        fill: #17231d !important;
        -webkit-text-fill-color: #17231d !important;
      }

      /* Hover effects */
      div.stButton > button:hover,
      div[data-testid="stDownloadButton"] button:hover {
        transform: translateY(-1px);
        box-shadow: 0 5px 13px rgba(23, 35, 29, .10);
      }

      /* Disabled buttons */
      div.stButton > button:disabled,
      div[data-testid="stDownloadButton"] button:disabled {
        background: #e5e7e2 !important;
        color: #737b73 !important;
        border-color: #e5e7e2 !important;
        opacity: 1 !important;
      }
      div.stButton > button:disabled * {
        color: #737b73 !important;
        fill: #737b73 !important;
        -webkit-text-fill-color: #737b73 !important;
      }

      /* Tabs and separators */
      [data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--cl-line);
      }
      [data-testid="stTabs"] button[role="tab"] {
        border-radius: 10px 10px 0 0;
        padding: .7rem 1rem;
      }
      [data-testid="stTabs"] button[aria-selected="true"] {
        color: var(--cl-ink);
        border-bottom-color: #8ba73f;
      }
      hr { border-color: var(--cl-line) !important; }
      [data-testid="stAlert"] { border-radius: 12px; }

      @media (max-width: 760px) {
        .block-container { padding: 1rem 1rem 2rem !important; }
      }
    </style>
    """, unsafe_allow_html=True)
