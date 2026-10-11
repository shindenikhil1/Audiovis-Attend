import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    """Compact landing page with both login options visible without scrolling on desktop."""
    style_background_home()
    style_base_layout()
    header_home()

    st.markdown("""
    <style>
      .block-container { max-width:1160px; padding:.65rem 1.5rem .45rem !important; }
      .av-eyebrow { color:#758d37; font-size:10px; font-weight:800; letter-spacing:2.2px; margin:0 0 12px; }
      .av-title { color:#17231d; font-family:'Manrope',sans-serif; font-size:clamp(38px,4.5vw,60px); font-weight:800; letter-spacing:-3px; line-height:1.02; margin:0; }
      .av-title span { color:#758d37; }
      .av-copy { color:#69766e; font-size:14px; line-height:1.7; max-width:440px; margin:15px 0 20px; }
      .av-feature { background:#17231d; border-radius:20px; padding:19px 22px; }
      .av-feature-label { color:#d7f36a; font-size:9px; font-weight:800; letter-spacing:1.8px; }
      .av-feature-title { color:#fff; font-family:'Manrope',sans-serif; font-size:21px; font-weight:800; letter-spacing:-.5px; margin-top:9px; }
      .av-feature-copy { color:#c5cec5; font-size:12px; line-height:1.65; margin-top:5px; max-width:370px; }
      .av-login-heading { color:#69766e; font-size:10px; font-weight:800; letter-spacing:2px; margin:0 0 10px; }
      .av-role { background:#fff; border:1px solid #e3e8df; border-radius:16px; padding:13px 15px 10px; margin:0 0 6px; }
      .av-role-top { display:flex; align-items:center; gap:12px; }
      .av-role-icon { width:40px; height:40px; flex:0 0 40px; border-radius:12px; background:#edf2e4; color:#30451b; display:flex; align-items:center; justify-content:center; font-size:20px; }
      .av-role-kicker { color:#758d37; font-size:9px; font-weight:800; letter-spacing:1.5px; margin-bottom:3px; }
      .av-role-name { color:#17231d; font-family:'Manrope',sans-serif; font-size:17px; font-weight:800; }
      .av-role-copy { color:#69766e; font-size:12px; line-height:1.5; margin:7px 0 0; }
      div.stButton > button { min-height:38px !important; padding:.4rem .85rem !important; }
      .av-home-foot { color:#879087; font-size:10px; text-align:center; margin-top:10px; padding-top:8px; border-top:1px solid #e3e8df; }
      @media(max-width:760px) {
        .block-container { padding:.6rem 1rem .5rem !important; }
        .av-title { font-size:42px; letter-spacing:-2px; }
        .av-copy { margin:10px 0 14px; }
        .av-feature { padding:15px 18px; }
      }
      @media(max-height:760px) and (min-width:761px) {
        .av-title { font-size:45px; }
        .av-copy { margin:10px 0 13px; line-height:1.55; }
        .av-feature { padding:13px 18px; }
        .av-role { padding:10px 13px 8px; }
        .av-role-copy { margin-top:5px; }
        .av-home-foot { margin-top:6px; padding-top:6px; }
      }
    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.03, .97], gap="large", vertical_alignment="center")
    with left:
        st.markdown("""
        <div class="av-eyebrow">ATTENDANCE, REIMAGINED</div>
        <h1 class="av-title">Make every<br>class <span>count.</span></h1>
        <p class="av-copy">A calmer, clearer way to manage classroom attendance. Choose your workspace and get straight to what matters.</p>
        <div class="av-feature">
          <div class="av-feature-label">AUDIOVIS ATTEND</div>
          <div class="av-feature-title">Less admin. More learning.</div>
          <div class="av-feature-copy">One simple workspace to help students and educators stay organized and in sync.</div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="av-login-heading">CHOOSE YOUR LOGIN</div>', unsafe_allow_html=True)
        st.markdown('''<div class="av-role"><div class="av-role-top"><div class="av-role-icon">↗</div><div><div class="av-role-kicker">FOR LEARNERS</div><div class="av-role-name">Student Login</div></div></div><p class="av-role-copy">View your attendance and open your student workspace.</p></div>''', unsafe_allow_html=True)
        if st.button("Continue as Student", type="primary", icon=":material/arrow_forward:", icon_position="right", key="student_portal", use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()

        st.markdown('''<div class="av-role" style="margin-top:10px;"><div class="av-role-top"><div class="av-role-icon" style="background:#f1eadb;color:#765a21;">▤</div><div><div class="av-role-kicker" style="color:#a17b31;">FOR EDUCATORS</div><div class="av-role-name">Teacher Login</div></div></div><p class="av-role-copy">Manage subjects, record attendance, and review class records.</p></div>''', unsafe_allow_html=True)
        if st.button("Continue as Teacher", type="primary", icon=":material/arrow_forward:", icon_position="right", key="teacher_portal", use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    st.markdown('<div class="av-home-foot">● &nbsp; AudioVis Attend &nbsp;·&nbsp; A smarter way to stay in sync</div>', unsafe_allow_html=True)
