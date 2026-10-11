import streamlit as st
def _brand_mark(size=44):
    return f'''<div class="AudioVis Attend-mark" style="width:{size}px;height:{size}px;">
      <svg viewBox="0 0 48 48" width="{size}" height="{size}" role="img" aria-label="AudioVis Attend logo">
        <rect width="48" height="48" rx="15" fill="#17231d"/>
        <path d="M13 17.5C16 12.5 21 10 26 12c4 1.5 6 5 6 8.5 0 3-1.5 5-4.5 7L18 34" fill="none" stroke="#d7f36a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="33.5" cy="34" r="4" fill="#d7f36a"/>
        <path d="M14 36h9" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round"/>
      </svg>
    </div>'''


def header_home():
    st.markdown(f"""
    <style>
      .AudioVis Attend-home-brand {{ display:flex; align-items:center; justify-content:center; gap:13px; margin:8px 0 26px; }}
      .AudioVis Attend-home-name {{ font-family:'Manrope',sans-serif; color:#17231d; font-size:25px; font-weight:800; letter-spacing:-1px; line-height:1; }}
      .AudioVis Attend-home-tag {{ color:#69766e; font-size:10px; font-weight:700; letter-spacing:2.2px; margin-top:6px; }}
    </style>
    <div class="AudioVis Attend-home-brand">
      {_brand_mark(50)}
      <div><div class="AudioVis Attend-home-name">AudioVis Attend</div><div class="AudioVis Attend-home-tag">SMART ATTENDANCE, MADE SIMPLE</div></div>
    </div>
    """, unsafe_allow_html=True)

def header_dashboard():
    st.markdown(f"""
    <style>
      .AudioVis Attend-dashboard-brand {{ display:flex; align-items:center; gap:11px; margin:0 0 12px; }}
      .AudioVis Attend-dashboard-name {{ font-family:'Manrope',sans-serif; color:#17231d; font-size:23px; font-weight:800; letter-spacing:-1px; line-height:1; }}
      .AudioVis Attend-dashboard-tag {{ color:#69766e; font-size:9px; font-weight:700; letter-spacing:1.7px; margin-top:5px; }}
    </style>
    <div class="AudioVis Attend-dashboard-brand">
      {_brand_mark(44)}
      <div><div class="AudioVis Attend-dashboard-name">AudioVis Attend</div><div class="AudioVis Attend-dashboard-tag">SMART ATTENDANCE, MADE SIMPLE</div></div>
    </div>
    """, unsafe_allow_html=True)    