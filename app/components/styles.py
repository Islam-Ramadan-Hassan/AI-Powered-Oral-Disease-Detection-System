from __future__ import annotations

import streamlit as st


def inject_styles() -> None:
    """Inject dark-first styling, interactive effects, and clear typography.

    The user explicitly requested custom CSS: a dark theme across the whole
    project, a loading screen, and interactive/animated UI. Styling is scoped
    to Streamlit's generated keys and re-injected on every rerun.
    """
    st.html(f"""
    <style>
    :root {{
        --ov-bg: #0B1220;
        --ov-bg-deep: #080E1A;
        --ov-card: #131E30;
        --ov-card-hover: #182542;
        --ov-border: #24304A;
        --ov-border-strong: #33507A;
        --ov-text: #E2E8F0;
        --ov-muted: #94A3B8;
        --ov-primary: #42A5F5;
        --ov-primary-soft: #90CAF9;
        --ov-glow: rgba(66, 165, 245, 0.18);
        --ov-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }}

    /* ---------- Clear, readable base typography ---------- */
    html, body, [data-testid="stAppViewContainer"] {{
        font-family: 'Inter', -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-rendering: optimizeLegibility;
        letter-spacing: -0.01em;
        color: var(--ov-text);
    }}
    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] li {{
        line-height: 1.7;
        font-size: 1rem;
        color: var(--ov-text);
    }}
    h1, h2, h3, h4 {{
        letter-spacing: -0.025em;
        line-height: 1.25;
        color: var(--ov-text);
    }}

    /* ---------- Whole-project dark background ---------- */
    html, body, [data-testid="stAppViewContainer"] {{
        background: var(--ov-bg);
    }}
    [data-testid="stAppViewContainer"] {{
        background:
            radial-gradient(900px 520px at 0% 0%, var(--ov-glow) 0%, transparent 60%),
            linear-gradient(180deg, var(--ov-bg) 0%, var(--ov-bg-deep) 120%) fixed;
    }}
    [data-testid="stHeader"] {{
        background: rgba(11, 18, 32, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-bottom: 1px solid var(--ov-border);
    }}
    [data-testid="stSidebar"] {{
        background: var(--ov-bg);
        border-right: 1px solid var(--ov-border);
    }}

    /* ---------- Loading splash overlay ---------- */
    .ov-splash {{
        position: fixed;
        inset: 0;
        z-index: 999999;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 18px;
        background:
            radial-gradient(700px 420px at 50% 30%, rgba(66, 165, 245, 0.16) 0%, transparent 65%),
            var(--ov-bg-deep);
        animation: ovSplashOut 1.6s ease 1.1s forwards;
        pointer-events: none;
    }}
    .ov-splash-logo {{
        width: 64px;
        height: 64px;
        border-radius: 16px;
        background: linear-gradient(135deg, #42A5F5, #1565C0);
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 0 40px rgba(66, 165, 245, 0.5);
        animation: ovPulse 1.2s ease-in-out infinite;
    }}
    .ov-splash-title {{
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: var(--ov-text);
    }}
    .ov-splash-sub {{
        color: var(--ov-muted);
        font-size: 0.9rem;
    }}
    .ov-splash-bar {{
        width: 180px;
        height: 5px;
        border-radius: 999px;
        background: var(--ov-border);
        overflow: hidden;
    }}
    .ov-splash-bar::after {{
        content: "";
        display: block;
        width: 40%;
        height: 100%;
        border-radius: 999px;
        background: linear-gradient(90deg, transparent, var(--ov-primary), transparent);
        animation: ovSlide 1.1s ease-in-out infinite;
    }}
    @keyframes ovSplashOut {{
        to {{ opacity: 0; visibility: hidden; }}
    }}
    @keyframes ovPulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.06); }}
    }}
    @keyframes ovSlide {{
        0% {{ transform: translateX(-120%); }}
        100% {{ transform: translateX(420%); }}
    }}

    /* ---------- Entrance animation for page content ---------- */
    @keyframes ovFadeInUp {{
        from {{ opacity: 0; transform: translateY(12px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    [data-testid="stMain"] {{ animation: ovFadeInUp 0.5s cubic-bezier(0.22, 1, 0.36, 1) both; }}

    /* ---------- Modern interactive cards ---------- */
    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: var(--ov-card);
        border: 1px solid var(--ov-border);
        border-radius: 14px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        transition: transform 0.22s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.22s ease, border-color 0.22s ease, background 0.22s ease;
    }}
    [data-testid="stVerticalBlockBorderWrapper"]:hover {{
        transform: translateY(-3px);
        background: var(--ov-card-hover);
        border-color: var(--ov-border-strong);
        box-shadow: var(--ov-shadow);
    }}

    /* ---------- Interactive metric tiles ---------- */
    [data-testid="stMetric"] {{
        background: var(--ov-card);
        border: 1px solid var(--ov-border);
        border-radius: 14px;
        padding: 1rem 1.2rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
        transition: transform 0.22s cubic-bezier(0.22, 1, 0.36, 1), box-shadow 0.22s ease, border-color 0.22s ease;
        cursor: pointer;
    }}
    [data-testid="stMetric"]:hover {{
        transform: translateY(-2px);
        border-color: var(--ov-primary);
        box-shadow: var(--ov-shadow), 0 0 0 1px var(--ov-glow);
    }}
    [data-testid="stMetricLabel"] {{
        color: var(--ov-muted);
        font-size: 0.85rem;
        font-weight: 500;
        letter-spacing: 0.02em;
    }}
    [data-testid="stMetricValue"] {{
        color: var(--ov-text);
        font-size: 1.55rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }}

    /* ---------- Hero header (gradient title) ---------- */
    [data-testid="stKey-page_hero"] h3 {{
        background: linear-gradient(120deg, var(--ov-primary), var(--ov-primary-soft));
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-weight: 800;
        letter-spacing: -0.03em;
    }}
    [data-testid="stKey-page_hero"] p {{
        color: var(--ov-muted);
        font-size: 1.02rem;
    }}

    /* ---------- Interactive buttons ---------- */
    .stButton > button {{
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    .stButton > button:hover {{
        box-shadow: 0 6px 18px var(--ov-glow);
        transform: translateY(-2px);
    }}
    .stButton > button:active {{
        transform: translateY(0) scale(0.98);
    }}

    /* ---------- Page links (quick actions) ---------- */
    .stPageLink a {{
        border-radius: 10px;
        padding: 0.5rem 0.75rem;
        margin-bottom: 0.2rem;
        transition: all 0.2s ease;
    }}
    .stPageLink a:hover {{
        background: var(--ov-card-hover);
        box-shadow: 0 4px 14px var(--ov-glow);
        transform: translateX(3px);
    }}

    /* ---------- Tabs ---------- */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 6px;
        border-bottom: 1px solid var(--ov-border);
    }}
    .stTabs [data-baseweb="tab"] {{
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    .stTabs [data-baseweb="tab"]:hover {{
        background: var(--ov-card-hover);
    }}

    /* ---------- Progress bars ---------- */
    .stProgress > div > div > div {{
        border-radius: 999px;
    }}

    /* ---------- Custom scrollbar ---------- */
    ::-webkit-scrollbar {{ width: 10px; height: 10px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{
        background: var(--ov-border-strong);
        border-radius: 8px;
        border: 2px solid transparent;
        background-clip: content-box;
    }}
    ::-webkit-scrollbar-thumb:hover {{ background: var(--ov-primary); background-clip: content-box; }}
    </style>
    """)


def render_loading_splash() -> None:
    """Render a branded loading splash once per session using a session flag."""
    if st.session_state.get("ov_splash_shown"):
        return
    st.session_state["ov_splash_shown"] = True

    st.html("""
    <div class="ov-splash">
        <div class="ov-splash-logo">
            <svg width="34" height="34" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 3c1.6 0 2.6 1.2 2.6 2.8 0 .9-.4 1.7-1 2.2h-3.2c-.6-.5-1-1.3-1-2.2C9.4 4.2 10.4 3 12 3z" fill="white"/>
                <path d="M8.6 10h6.8l-1.4 8.2c-.1.5-.5.8-1 .8h-2c-.5 0-.9-.3-1-.8L8.6 10z" fill="white"/>
            </svg>
        </div>
        <div>
            <div class="ov-splash-title">Oral Vision</div>
            <div class="ov-splash-sub">AI-powered oral disease detection</div>
        </div>
        <div class="ov-splash-bar"></div>
    </div>
    """)
