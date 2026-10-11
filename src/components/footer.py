import streamlit as st


def footer_home():
    st.markdown("""
    <div style="margin:2.5rem 0 0;padding-top:1rem;border-top:1px solid #e3e8df;display:flex;justify-content:center;align-items:center;gap:8px;color:#69766e;font-size:12px;">
      <span style="display:inline-block;width:7px;height:7px;border-radius:50%;background:#8ba73f;"></span>
      <span>AudioVis Attend · A smarter way to stay in sync</span>
    </div>
    """, unsafe_allow_html=True)


def footer_dashboard():
    st.markdown("""
    <div style="margin:2.5rem 0 0;padding-top:1rem;border-top:1px solid #e3e8df;display:flex;justify-content:space-between;align-items:center;gap:8px;color:#69766e;font-size:12px;flex-wrap:wrap;">
      <span><strong style="color:#17231d;">AudioVis Attend</strong> &nbsp;·&nbsp; Smart attendance, made simple</span>
      <span>Attendance workspace</span>
    </div>
    """, unsafe_allow_html=True)
