"""
ENTRESTO (Sacubitril/Valsartan) - Professional Drug Information App
Pre-Pharmacode V2.5 Standard
FDA-verified | Evidence-based | Updated February 2026
Reference ID: FDA-Entresto-2024
"""

import streamlit as st
import os
from datetime import datetime

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="ENTRESTO (Sacubitril/Valsartan) Info",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CUSTOM CSS (LIGHT + DARK MODE) ====================
st.markdown("""
<style>
    /* إخفاء القائمة الجانبية تماماً */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* إخفاء زر المشاركة والقائمة العلوية */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden; height: 0 !important; padding: 0 !important; margin: 0 !important; min-height: 0 !important;}
    footer {visibility: hidden;}
    
    /* تحسين الهوامش الرئيسية للموبايل */
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
        max-width: 100% !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #0460A9;
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, #0460A9 0%, #035C96 50%, #0878C8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #3C4C5A;
        text-align: center;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #E8F1FA;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #0460A9;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .warning-box {
        background-color: #FDF0F0;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #C72C35;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .success-box {
        background-color: #EEF7F1;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #1B8A4A;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .critical-box {
        background-color: #FDF0F0;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #C72C35;
        margin: 0.8rem 0;
        border: 2px solid #C72C35;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* تحسين التبويبات للموبايل */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        flex-wrap: wrap !important;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        padding: 0 12px;
        background-color: #EDF2F7;
        border-radius: 8px;
        font-size: 0.9rem;
        white-space: nowrap;
        flex: 0 1 auto;
        margin: 2px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #0460A9;
        color: white;
    }
    /* إخفاء الخط السفلي للتبويبة النشطة */
    .stTabs [data-baseweb="tab-highlight"] {
        display: none !important;
    }
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }
    
    /* تحسين العرض على الموبايل */
    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        
        .main-header {
            font-size: 1.6rem;
            padding: 0.5rem 0;
        }
        
        .sub-header {
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 3px;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.75rem;
            padding: 0 6px;
            height: 38px;
            min-width: auto;
        }
        
        .info-box, .warning-box, .success-box, .critical-box {
            padding: 0.8rem;
            font-size: 0.9rem;
        }
        
        .info-box h3, .warning-box h3, .success-box h3, .critical-box h3,
        .info-box h4, .warning-box h4, .success-box h4, .critical-box h4 {
            font-size: 1rem;
        }
        
        /* جعل الأعمدة تتراص عمودياً على الموبايل */
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
        
        /* تحسين حجم النصوص */
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.3rem !important; }
        h3 { font-size: 1.1rem !important; }
        h4 { font-size: 1rem !important; }
        
        .element-container {
            margin-bottom: 0.5rem;
        }
    }
    
    /* شاشات أصغر (هواتف صغيرة) */
    @media (max-width: 480px) {
        .main-header {
            font-size: 1.3rem;
        }
        
        .sub-header {
            font-size: 0.85rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.7rem;
            padding: 0 4px;
            height: 34px;
        }
        
        .info-box, .warning-box, .success-box, .critical-box {
            padding: 0.6rem;
            font-size: 0.85rem;
            border-radius: 8px;
        }
    }
    
    /* تنسيق صورة الدواء */
    .drug-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0.5rem 0;
        margin-bottom: 1rem;
    }
    
    /* تنسيق المصادر */
    .reference-item {
        background-color: #F5F8FB;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 3px solid #0460A9;
    }
    .reference-item strong { color: #0460A9; font-size: 1.05rem; }
    .reference-item a { color: #0878C8; text-decoration: none; word-break: break-all; display: block; margin-top: 0.3rem; }
    .reference-item a:hover { color: #0460A9; text-decoration: underline; }
    
    /* بطاقات المعلومات بدل الجداول */
    .card-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.6rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        transition: box-shadow 0.3s ease, transform 0.2s ease;
    }
    .card-item:hover { box-shadow: 0 4px 12px rgba(212, 165, 32, 0.2); transform: translateY(-1px); }
    .card-item h4 { margin: 0 0 0.5rem 0; color: #0460A9; font-size: 1.05rem; }
    .card-item .card-detail { font-size: 0.92rem; color: #3C4C5A; margin: 0.25rem 0; line-height: 1.5; }
    .card-item .card-detail strong { color: #475569; }
    .card-item .card-badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.82rem; font-weight: 600; margin-right: 4px; }
    .card-badge-red { background: #FDEAEA; color: #C72C35; }
    .card-badge-green { background: #E5F5EC; color: #1B8A4A; }
    .card-badge-blue { background: #E0EEF9; color: #0460A9; }
    .card-badge-yellow { background: #FBF7EC; color: #B8920E; }
    .card-badge-purple { background: #f3e8ff; color: #7c3aed; }
    
    @media (max-width: 768px) {
        .card-item { padding: 0.8rem; margin: 0.4rem 0; }
        .card-item h4 { font-size: 0.95rem; }
        .card-item .card-detail { font-size: 0.85rem; }
    }
    
    /* ============================== DARK MODE ============================== */
    @media (prefers-color-scheme: dark) {
        .main-header {
            background: linear-gradient(135deg, #5AAEE6 0%, #7EC4F0 50%, #E8C45A 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .sub-header { color: #94a3b8; }
        
        /* ---- Info Box (brand blue) ---- */
        .info-box { background-color: #0C1C2E; border-left-color: #5AAEE6; color: #e2e8f0; }
        .info-box h3, .info-box h4, .info-box h5 { color: #7EC4F0 !important; }
        .info-box p, .info-box li, .info-box em { color: #cbd5e1; }
        .info-box strong { color: #f1f5f9; }
        .info-box a { color: #5AAEE6; }
        
        /* ---- Warning Box (harmonized red) ---- */
        .warning-box { background-color: #2A1215; border-left-color: #E85B5B; color: #e2e8f0; }
        .warning-box h3, .warning-box h4, .warning-box h5 { color: #F0908F !important; }
        .warning-box p, .warning-box li, .warning-box em { color: #cbd5e1; }
        .warning-box strong { color: #f1f5f9; }
        
        /* ---- Success Box (harmonized green) ---- */
        .success-box { background-color: #0E1F14; border-left-color: #3DBF6E; color: #e2e8f0; }
        .success-box h3, .success-box h4, .success-box h5 { color: #6ED99A !important; }
        .success-box p, .success-box li, .success-box em { color: #cbd5e1; }
        .success-box strong { color: #f1f5f9; }
        
        /* ---- Critical Box (harmonized dark red) ---- */
        .critical-box { background-color: #2D1114; border-color: #C72C35; border-left-color: #C72C35; color: #e2e8f0; }
        .critical-box h2, .critical-box h3, .critical-box h4, .critical-box h5 { color: #F0908F !important; }
        .critical-box p, .critical-box li, .critical-box em { color: #cbd5e1; }
        .critical-box strong { color: #f1f5f9; }
        .critical-box span { color: #F0908F !important; }
        
        /* ---- Cards ---- */
        .card-item { background: #1A2536; border-color: #2D3D50; box-shadow: 0 1px 3px rgba(0,0,0,0.4); }
        .card-item:hover { box-shadow: 0 4px 12px rgba(212, 165, 32, 0.15); transform: translateY(-1px); }
        .card-item h4 { color: #7EC4F0; }
        .card-item .card-detail { color: #cbd5e1; }
        .card-item .card-detail strong { color: #e2e8f0; }
        
        /* ---- Badges ---- */
        .card-badge-red { background: #3D0F12; color: #F0908F; }
        .card-badge-green { background: #0A2814; color: #6ED99A; }
        .card-badge-blue { background: #0C2642; color: #7EC4F0; }
        .card-badge-yellow { background: #332508; color: #E8C45A; }
        .card-badge-purple { background: #2e1065; color: #c4b5fd; }
        
        /* ---- Metric Card ---- */
        .metric-card { background: #1A2536; box-shadow: 0 2px 4px rgba(0,0,0,0.4); color: #e2e8f0; }
        
        /* ---- References ---- */
        .reference-item { background-color: #1A2536; border-left-color: #5AAEE6; }
        .reference-item strong { color: #7EC4F0; }
        .reference-item a { color: #5AAEE6; }
        .reference-item a:hover { color: #7EC4F0; }
        
        /* ---- Links inside boxes ---- */
        .info-box a:hover, .warning-box a:hover,
        .success-box a:hover, .critical-box a:hover { color: #7EC4F0; }
        
        /* ---- Tabs (unselected) ---- */
        .stTabs [data-baseweb="tab"] { background-color: #1A2536; color: #cbd5e1; }
        .stTabs [aria-selected="true"] { background-color: #0460A9; color: white; }
    }

    /* ===== EXPANDER / ACCORDION STYLES ===== */
    /* Legacy Streamlit class names */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #0460A9, #0878C8) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        border: none !important;
    }
    .streamlit-expanderHeader:hover {
        background: linear-gradient(135deg, #035C96, #0460A9) !important;
        box-shadow: 0 4px 12px rgba(4, 96, 169, 0.35) !important;
        transform: translateY(-1px) !important;
    }
    .streamlit-expanderHeader p { color: white !important; margin: 0 !important; }
    .streamlit-expanderHeader svg { fill: white !important; }
    .streamlit-expanderContent {
        border: 1px solid #D0DDE8 !important;
        border-top: none !important;
        border-radius: 0 0 10px 10px !important;
        padding: 1rem !important;
    }

    /* data-testid selectors (modern Streamlit) */
    [data-testid="stExpander"] {
        border: none !important;
        border-radius: 10px !important;
        margin-bottom: 0.8rem !important;
        overflow: hidden !important;
        box-shadow: 0 2px 6px rgba(4, 96, 169, 0.1) !important;
    }
    [data-testid="stExpander"] details {
        border: none !important;
    }
    [data-testid="stExpander"] summary {
        background: linear-gradient(135deg, #0460A9, #0878C8) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stExpander"] summary:hover {
        background: linear-gradient(135deg, #035C96, #0460A9) !important;
        box-shadow: 0 4px 12px rgba(4, 96, 169, 0.35) !important;
    }
    [data-testid="stExpander"] summary span { color: white !important; }
    [data-testid="stExpander"] summary svg { fill: white !important; color: white !important; }
    [data-testid="stExpander"] details[open] summary {
        border-radius: 10px 10px 0 0 !important;
    }
    [data-testid="stExpander"] [data-testid="stExpanderDetails"] {
        border: 2px solid #0878C8 !important;
        border-top: none !important;
        border-radius: 0 0 10px 10px !important;
        padding: 1rem !important;
    }

    /* Broad fallback selectors for any Streamlit version */
    .st-expander {
        border: none !important;
        border-radius: 10px !important;
        margin-bottom: 0.8rem !important;
        overflow: hidden !important;
        box-shadow: 0 2px 6px rgba(4, 96, 169, 0.1) !important;
    }
    .st-expander details {
        border: none !important;
    }
    .st-expander summary {
        background: linear-gradient(135deg, #0460A9, #0878C8) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    .st-expander summary:hover {
        background: linear-gradient(135deg, #035C96, #0460A9) !important;
        box-shadow: 0 4px 12px rgba(4, 96, 169, 0.35) !important;
    }
    .st-expander summary span { color: white !important; }
    .st-expander summary svg { fill: white !important; color: white !important; }
    .st-expander details[open] summary {
        border-radius: 10px 10px 0 0 !important;
    }

    @media (max-width: 768px) {
        .streamlit-expanderHeader,
        [data-testid="stExpander"] summary,
        .st-expander summary {
            font-size: 0.9rem !important;
            padding: 0.6rem 0.8rem !important;
        }
    }
    @media (prefers-color-scheme: dark) {
        [data-testid="stExpander"],
        .st-expander { box-shadow: 0 2px 6px rgba(0,0,0,0.3) !important; }

        [data-testid="stExpander"] summary,
        .st-expander summary { background: linear-gradient(135deg, #035C96, #0460A9) !important; }

        [data-testid="stExpander"] summary:hover,
        .st-expander summary:hover { background: linear-gradient(135deg, #024A7A, #035C96) !important; }

        [data-testid="stExpander"] [data-testid="stExpanderDetails"],
        .streamlit-expanderContent,
        .st-expander [data-testid="stExpanderDetails"] { border-color: #2D3D50 !important; background-color: #0C1520 !important; }
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER WITH DRUG IMAGE ====================
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ENTRESTO.png")
if not os.path.exists(image_path):
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ENTRESTO.png")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        st.warning("⚠️ Drug box image not found. Please place ENTRESTO.png in the app folder.")

st.markdown('<h1 class="main-header">💊 ENTRESTO (Sacubitril/Valsartan)</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">✅ FDA-verified • 🔬 Evidence-based • 📅 Updated February 2026</p>', unsafe_allow_html=True)

st.markdown("---")

# ==================== MAIN TABS ====================
tabs = st.tabs([
    "📖 Overview",
    "⚗️ Mechanism",
    "💊 Dosage",
    "⚖️ Pharmacokinetics",
    "🚫 Contraindications",
    "⚠️ Side Effects",
    "💊⚖️ Interactions",
    "📊 Comparison",
    "📚 References",
    "🏢 Novartis AG"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.header("📖 Overview of ENTRESTO (Sacubitril/Valsartan)")

    st.markdown("""
    <div class="info-box">
    <h4>ℹ️ Basic Information</h4>
    <p class="card-detail">🧪 <strong>Generic Name:</strong> Sacubitril / Valsartan</p>
    <p class="card-detail">🏷️ <strong>Brand Name:</strong> ENTRESTO®</p>
    <p class="card-detail">🏭 <strong>Manufacturer:</strong> Novartis Pharmaceuticals</p>
    <p class="card-detail">💊 <strong>Drug Class:</strong> Angiotensin Receptor-Neprilysin Inhibitor (ARNI)</p>
    <p class="card-detail">📅 <strong>FDA Approval:</strong> July 2015</p>
    <p class="card-detail">📋 <strong>REMS Program:</strong> None required</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🎯 Indications & Available Strengths"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="info-box">
            <h4>👨‍⚕️ Adult Heart Failure:</h4>
            <ul>
                <li><strong>To reduce the risk of cardiovascular death and hospitalization for heart failure in adult patients with chronic heart failure</strong></li>
                <li><em>Benefit:</em> Most clearly evident in patients with left ventricular ejection fraction (LVEF) below normal</li>
                <li><em>Guideline Status:</em> First-line therapy (ARNI) preferred over ACEi/ARB for HFrEF (ACC/AHA Guidelines)</li>
            </ul>
            <h4>👶 Pediatric Heart Failure:</h4>
            <ul>
                <li><strong>Treatment of symptomatic heart failure with systemic left ventricular systolic dysfunction in pediatric patients aged ≥1 year</strong></li>
                <li><em>Effect:</em> Reduces NT-proBNP and is expected to improve cardiovascular outcomes</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card-item">
                <h4>💊 24 mg / 26 mg — Film-coated Tablet</h4>
                <p class="card-detail">Sacubitril 24 mg / Valsartan 26 mg — Starting dose for special populations</p>
            </div>
            <div class="card-item">
                <h4>💊 49 mg / 51 mg — Film-coated Tablet</h4>
                <p class="card-detail">Sacubitril 49 mg / Valsartan 51 mg — Standard starting dose</p>
            </div>
            <div class="card-item">
                <h4>💊 97 mg / 103 mg — Film-coated Tablet</h4>
                <p class="card-detail">Sacubitril 97 mg / Valsartan 103 mg — Target maintenance dose</p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("🏆 Key Clinical Points"):
        st.markdown("""
        <div class="success-box">
        <h4>✅ Efficacy:</h4>
        <ul>
            <li>🎯 20% reduction in cardiovascular death vs. Enalapril (PARADIGM-HF)</li>
            <li>📊 21% reduction in heart failure hospitalization vs. Enalapril</li>
            <li>📅 First-line ARNI therapy for HFrEF per ACC/AHA Guidelines</li>
        </ul>
        <h4>⚠️ Critical Safety Notes:</h4>
        <ul>
            <li>🚨 Do NOT use with ACEi — 36-hour washout required</li>
            <li>⚠️ Do NOT use in pregnancy — fetal toxicity risk</li>
            <li>🔬 Monitor blood pressure, potassium, and renal function</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 2: MECHANISM ====================
with tabs[1]:
    st.header("⚗️ Mechanism of Action")

    st.markdown("### 🔬 ARNI Overview")
    st.markdown("""
    <div class="info-box">
    <h3 style="color: #1e3a8a;">🔬 Dual-Acting Angiotensin Receptor-Neprilysin Inhibitor (ARNI)</h3>
    <p>Entresto combines two mechanisms: Sacubitril (a neprilysin inhibitor prodrug) and Valsartan (an angiotensin II receptor blocker). Together, they enhance the natriuretic peptide system while blocking the harmful effects of the RAAS, providing superior cardiovascular protection compared to RAAS blockade alone.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("⚙️ Detailed Mechanism"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 1️⃣ Neprilysin Inhibition (Sacubitril → LBQ657)")
            st.markdown("""
            <div class="success-box">
            <h4>🎯 Neprilysin Enzyme Inhibition</h4>
            <h5>Mechanism:</h5>
            <ul>
                <li>Sacubitril is converted by esterases to LBQ657, the active neprilysin inhibitor</li>
                <li>LBQ657 inhibits neprilysin, preventing degradation of natriuretic peptides (ANP, BNP, CNP), bradykinin, and adrenomedullin</li>
            </ul>
            <h5>Clinical Effect:</h5>
            <ul>
                <li>✅ Increased natriuretic peptide levels → vasodilation, natriuresis, diuresis</li>
                <li>✅ Reduced cardiac fibrosis and hypertrophy</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("### 2️⃣ AT1 Receptor Blockade (Valsartan)")
            st.markdown("""
            <div class="success-box">
            <h4>🎯 Angiotensin II Type 1 (AT1) Receptor Blockade</h4>
            <h5>Mechanism:</h5>
            <ul>
                <li>Valsartan selectively blocks the AT1 receptor, preventing angiotensin II-mediated vasoconstriction</li>
                <li>Blocks aldosterone secretion and sympathetic activation driven by angiotensin II</li>
            </ul>
            <h5>Clinical Effect:</h5>
            <ul>
                <li>✅ Reduced afterload and preload → improved cardiac output</li>
                <li>✅ Reduced sodium/water retention and cardiac remodeling</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 3: DOSAGE ====================
with tabs[2]:
    st.header("💊 Dosage and Administration")
    st.markdown("""
    <div class="warning-box">
    <h3>⚠️ Critical: ACE Inhibitor Washout Required</h3>
    <p style="font-size: 1.1rem; font-weight: bold;">
    Do NOT administer Entresto within 36 hours of switching from an ACE inhibitor. Concomitant use increases the risk of angioedema.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 👨‍⚕️ Adult Dosing")
    st.markdown("""
    <div class="card-item">
        <h4>1️⃣ Starting Dose</h4>
        <p class="card-detail"><strong>Dose:</strong> 49/51 mg (sacubitril/valsartan)</p>
        <p class="card-detail"><strong>Schedule:</strong> Twice Daily (BID)</p>
        <p class="card-detail"><strong>Note:</strong> For patients NOT currently on ACEi/ARB or on low doses</p>
    </div>
    <div class="card-item">
        <h4>2️⃣ Alternative Starting Dose</h4>
        <p class="card-detail"><strong>Dose:</strong> 24/26 mg (sacubitril/valsartan)</p>
        <p class="card-detail"><strong>Schedule:</strong> Twice Daily (BID)</p>
        <p class="card-detail"><strong>Note:</strong> For patients with severe renal impairment (eGFR &lt;30), moderate hepatic impairment (Child-Pugh B), or low prior ACEi/ARB dose</p>
    </div>
    <div class="card-item">
        <h4>3️⃣ Target Maintenance Dose</h4>
        <p class="card-detail"><strong>Dose:</strong> 97/103 mg (sacubitril/valsartan)</p>
        <p class="card-detail"><strong>Schedule:</strong> Twice Daily (BID)</p>
        <p class="card-detail"><strong>Note:</strong> Double the dose every 2-4 weeks as tolerated to reach this target</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("👶 Pediatric Dosing (≥1 year)"):
        st.markdown("""
        <div class="card-item">
            <h4>📏 Weight &lt;40 kg</h4>
            <p class="card-detail"><strong>Starting:</strong> 1.6 mg/kg BID</p>
            <p class="card-detail"><strong>Target:</strong> 3.1 mg/kg BID</p>
            <p class="card-detail"><strong>Titration:</strong> Every 2 weeks</p>
        </div>
        <div class="card-item">
            <h4>📏 Weight ≥40 kg</h4>
            <p class="card-detail"><strong>Starting:</strong> 49/51 mg BID</p>
            <p class="card-detail"><strong>Target:</strong> 97/103 mg BID</p>
            <p class="card-detail"><strong>Titration:</strong> Every 2 weeks</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("📉 Dose Adjustments"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🟡 Renal Impairment")
            st.markdown("""
            <div class="card-item">
                <h4>🟡 Severe Renal Impairment (eGFR &lt;30)</h4>
                <p class="card-detail"><strong>Dose:</strong> Start with 24/26 mg BID</p>
                <p class="card-detail"><strong>Note:</strong> Titrate with close monitoring of renal function and potassium</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("#### 🔴 Hepatic Impairment")
            st.markdown("""
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>🟡 Moderate (Child-Pugh B)</h4>
                <p class="card-detail"><strong>Dose:</strong> Start with 24/26 mg BID</p>
                <p class="card-detail"><strong>Note:</strong> Use with caution</p>
            </div>
            <div class="card-item" style="border-left: 4px solid #dc2626;">
                <h4>🚫 Severe (Child-Pugh C)</h4>
                <p class="card-detail"><span class="card-badge card-badge-red">NOT RECOMMENDED</span></p>
                <p class="card-detail"><strong>Note:</strong> No clinical data available; avoid use</p>
            </div>
            """, unsafe_allow_html=True)

    with st.expander("📋 Administration Instructions"):
        st.success("""
        ✅ Swallow tablets whole; do not crush or chew

        ✅ May be taken with or without food

        ❌ Do NOT double the dose if a dose is missed

        ✅ Take next dose at regularly scheduled time if a dose is missed
        """)

# ==================== TAB 4: PHARMACOKINETICS ====================
with tabs[3]:
    st.header("⚖️ Pharmacokinetics")
    st.markdown("### 📊 Pharmacokinetic Parameters Summary")
    st.markdown("""
    <div class="card-item">
        <h4>📊 Sacubitril</h4>
        <p class="card-detail"><strong>Bioavailability:</strong> >60%</p>
        <p class="card-detail"><strong>Tmax:</strong> 0.5 hours</p>
        <p class="card-detail"><strong>Half-life:</strong> 1.4 hours (prodrug)</p>
        <p class="card-detail"><strong>Protein Binding:</strong> 94-97%</p>
        <p class="card-detail"><strong>Metabolism:</strong> Rapidly converted by esterases to LBQ657 (active metabolite)</p>
        <p class="card-detail"><strong>Excretion:</strong> Urine (52-68%)</p>
    </div>
    <div class="card-item">
        <h4>📊 LBQ657 (Active Metabolite of Sacubitril)</h4>
        <p class="card-detail"><strong>Tmax:</strong> 2 hours</p>
        <p class="card-detail"><strong>Half-life:</strong> 11.5 hours</p>
        <p class="card-detail"><strong>Protein Binding:</strong> 94-97%</p>
        <p class="card-detail"><strong>Metabolism:</strong> Minimal further metabolism</p>
        <p class="card-detail"><strong>Excretion:</strong> Urine and Feces</p>
    </div>
    <div class="card-item">
        <h4>📊 Valsartan</h4>
        <p class="card-detail"><strong>Bioavailability:</strong> 23%</p>
        <p class="card-detail"><strong>Tmax:</strong> 1.5 hours</p>
        <p class="card-detail"><strong>Half-life:</strong> 9.9 hours</p>
        <p class="card-detail"><strong>Protein Binding:</strong> 94-97%</p>
        <p class="card-detail"><strong>Metabolism:</strong> Minimal (~20%)</p>
        <p class="card-detail"><strong>Excretion:</strong> Feces (86%)</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🧬 Distribution, Metabolism & Elimination"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🧬 Distribution")
            st.info("""
            **Protein Binding:** 94-97% for all components

            **Volume of Distribution:** Moderate tissue distribution

            **Tissue Distribution:**
            - Sacubitril/LBQ657: Crosses blood-brain barrier minimally
            - Valsartan: Limited tissue distribution, primarily plasma-bound
            """)
            st.markdown("### 🔄 Metabolism")
            st.warning("""
            **CYP Enzymes Involved:**
            - Sacubitril: NOT metabolized by CYP450 — converted by esterases
            - Valsartan: Minimally metabolized by **CYP2C9** (~20%)

            **Key Points:**
            - Does NOT inhibit CYP1A2, 2C9, 2C19, 2D6, or 3A4
            - Does NOT induce CYP450 enzymes
            - Low CYP-mediated interaction risk
            """)
        with col2:
            st.markdown("### 🚰 Elimination")
            st.markdown("""
            <div class="card-item">
                <h4>🚰 Sacubitril/LBQ657 — Renal (52-68%)</h4>
                <p class="card-detail">Primarily eliminated via urine as LBQ657</p>
            </div>
            <div class="card-item">
                <h4>💩 Valsartan — Fecal (86%)</h4>
                <p class="card-detail">Primarily eliminated unchanged in feces; ~13% via urine</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("### 👥 Special Populations")
            st.warning("""
            **Renal Impairment:**
            - Severe (eGFR <30): Increased exposure; start at 24/26 mg BID

            **Hepatic Impairment:**
            - Moderate (Child-Pugh B): Increased exposure; start at 24/26 mg BID
            - Severe (Child-Pugh C): Not recommended

            **Pediatric:**
            - ≥1 year: Weight-based dosing available

            **Elderly:**
            - No dose adjustment required based on age alone
            """)

# ==================== TAB 5: CONTRAINDICATIONS ====================
with tabs[4]:
    st.header("🚫 Contraindications and Warnings")

    st.markdown("""
    <div class="critical-box">
    <h2 style="color: #dc2626; text-align: center;">🚨 BOXED WARNING — FETAL TOXICITY 🚨</h2>
    <p style="font-size: 1.1rem; text-align: center; font-weight: bold;">
    When pregnancy is detected, discontinue Entresto as soon as possible. Drugs that act directly on the renin-angiotensin system can cause injury and death to the developing fetus.
    </p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🚨 Absolute Contraindications"):
        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>🚨 1. Concomitant ACE Inhibitor Use</h4>
            <p class="card-detail"><strong>Risk:</strong> Increased risk of angioedema due to dual RAAS/neprilysin blockade</p>
            <p class="card-detail"><strong>Action:</strong> 36-hour washout period mandatory when switching from an ACEi</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>🚨 2. Prior Angioedema with ACEi or ARB</h4>
            <p class="card-detail"><strong>Risk:</strong> Recurrent angioedema, potentially life-threatening</p>
            <p class="card-detail"><strong>Action:</strong> Do not initiate Entresto in patients with history of angioedema related to ACEi/ARB</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>🚨 3. Aliskiren Co-administration in Diabetic Patients</h4>
            <p class="card-detail"><strong>Risk:</strong> Increased risk of hypotension, hyperkalemia, and renal impairment</p>
            <p class="card-detail"><strong>Action:</strong> Contraindicated in patients with diabetes; avoid in eGFR &lt;60</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>🚨 4. Pregnancy</h4>
            <p class="card-detail"><strong>Risk:</strong> Fetal toxicity — injury and death to the developing fetus</p>
            <p class="card-detail"><strong>Action:</strong> Discontinue as soon as pregnancy is detected</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>🚨 5. Hypersensitivity</h4>
            <p class="card-detail"><strong>Risk:</strong> Anaphylaxis or severe allergic reaction</p>
            <p class="card-detail"><strong>Action:</strong> Do not use in patients with known hypersensitivity to any component</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("⚠️ Warnings and Precautions"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🔴 Angioedema")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>Incidence: 0.5% overall (vs 0.2% Enalapril)</li>
                <li>Higher risk in Black patients (2.4%)</li>
                <li>Discontinue immediately and treat if angioedema occurs</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("#### 🔴 Hypotension")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>Most common adverse reaction (18%)</li>
                <li>Higher risk in volume-/salt-depleted patients</li>
                <li>Correct volume depletion before initiating</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("#### 🟠 Hyperkalemia")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>Monitor serum potassium periodically</li>
                <li>Higher risk with renal impairment, potassium supplements, or potassium-sparing diuretics</li>
                <li>Reduce dose or discontinue if persistent hyperkalemia</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("#### 🟠 Renal Impairment")
            st.markdown("""
            <div class="warning-box">
            <ul>
                <li>Monitor renal function periodically</li>
                <li>May cause decline in renal function, especially with NSAIDs</li>
                <li>Consider dose reduction in severe impairment</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 6: SIDE EFFECTS ====================
with tabs[5]:
    st.header("⚠️ Adverse Reactions (Side Effects)")
    st.markdown("### 📊 Common Side Effects (PARADIGM-HF Trial)")
    st.markdown("""
    <div class="card-item">
        <h4>🩸 Hypotension <span class="card-badge card-badge-red">18%</span></h4>
        <p class="card-detail">💡 More common than Enalapril (12%). Monitor BP closely; correct volume depletion before starting.</p>
    </div>
    <div class="card-item">
        <h4>⚗️ Hyperkalemia <span class="card-badge card-badge-red">12%</span></h4>
        <p class="card-detail">💡 Less common than Enalapril (14%); favorable profile. Monitor serum potassium.</p>
    </div>
    <div class="card-item">
        <h4>🤧 Cough <span class="card-badge card-badge-yellow">9%</span></h4>
        <p class="card-detail">💡 Significantly less than ACE inhibitors (Enalapril 13%). Related to bradykinin accumulation.</p>
    </div>
    <div class="card-item">
        <h4>💫 Dizziness <span class="card-badge card-badge-yellow">6%</span></h4>
        <p class="card-detail">💡 Related to blood pressure reduction. Similar to Enalapril (5%).</p>
    </div>
    <div class="card-item">
        <h4>🏥 Renal Failure / Elevated Creatinine <span class="card-badge card-badge-yellow">5%</span></h4>
        <p class="card-detail">💡 Similar to Enalapril (5%). Monitor renal function periodically.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🔴 Serious Reactions & Hematologic Effects"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🔴 Serious Adverse Reactions")
            st.markdown("""
            <div class="warning-box">
            <h4>Life-threatening / Rare:</h4>
            <ul>
                <li><strong>Angioedema</strong> — 0.5% overall; higher in Black patients (2.4%)</li>
                <li><strong>Orthostatic Hypotension</strong> — 2.1%; risk of falls</li>
                <li><strong>Falls</strong> — 1.9%; related to hypotension/dizziness</li>
                <li><strong>Hemoglobin Decrease (>2 g/dL)</strong> — 5%</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("### 🩸 Hematologic & Other Effects")
            st.info("""
            **Common:**
            - **Elevated serum creatinine**
            - **Elevated blood urea nitrogen (BUN)**

            **Rare/Serious:**
            - Significant hemoglobin decrease (>2 g/dL) in 5% of patients
            """)

    with st.expander("🩺 Monitoring & Emergency"):
        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>🩸 Blood Pressure</h4>
            <p class="card-detail"><strong>Baseline:</strong> Measure before initiation; correct volume depletion</p>
            <p class="card-detail"><strong>During Treatment:</strong> Monitor regularly, especially after dose changes</p>
            <p class="card-detail"><strong>If Abnormal:</strong> Reduce dose or temporarily withhold if symptomatic hypotension</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>⚗️ Serum Potassium</h4>
            <p class="card-detail"><strong>Baseline:</strong> Measure before initiation</p>
            <p class="card-detail"><strong>During Treatment:</strong> Monitor periodically, especially with concomitant potassium-sparing agents</p>
            <p class="card-detail"><strong>If Abnormal:</strong> Adjust dose of potassium supplements or Entresto; consider discontinuation if persistent</p>
        </div>
        <div class="card-item">
            <h4>🏥 Renal Function (SCr, BUN, eGFR)</h4>
            <p class="card-detail"><strong>Baseline:</strong> Measure before initiation</p>
            <p class="card-detail"><strong>During Treatment:</strong> Monitor periodically, especially in patients at risk</p>
            <p class="card-detail"><strong>If Abnormal:</strong> Consider dose reduction or discontinuation if significant decline</p>
        </div>
        """, unsafe_allow_html=True)

        st.error("""
        **🚨 Stop drug and seek emergency care if:**
        - Swelling of face, lips, tongue, or throat (angioedema)
        - Severe dizziness, fainting, or inability to stand
        - Signs of severe hyperkalemia: muscle weakness, irregular heartbeat, numbness/tingling
        """)

# ==================== TAB 7: DRUG INTERACTIONS ====================
with tabs[6]:
    st.header("💊⚖️ Drug Interactions")
    st.markdown("### 🔴 Contraindicated Combinations")
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚫 ACE Inhibitors (e.g., Enalapril, Lisinopril, Ramipril) <span class="card-badge card-badge-red">CONTRAINDICATED</span></h4>
        <p class="card-detail"><strong>Mechanism:</strong> Dual blockade of RAAS and neprilysin increases angioedema risk</p>
        <p class="card-detail"><strong>Consequence:</strong> Life-threatening angioedema</p>
        <p class="card-detail"><strong>Action:</strong> 36-hour washout period mandatory when switching</p>
        <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 7</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚫 Aliskiren (in Diabetic Patients) <span class="card-badge card-badge-red">CONTRAINDICATED</span></h4>
        <p class="card-detail"><strong>Mechanism:</strong> Dual RAAS blockade</p>
        <p class="card-detail"><strong>Consequence:</strong> Increased risk of hypotension, hyperkalemia, and renal impairment</p>
        <p class="card-detail"><strong>Action:</strong> Contraindicated in diabetes; avoid in eGFR &lt;60</p>
        <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 7</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🟡 Monitor Closely"):
        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #eab308;">
            <h4>🟡 Potassium-Sparing Diuretics (Spironolactone, Eplerenone) <span class="card-badge card-badge-yellow">MONITOR</span></h4>
            <p class="card-detail"><strong>Mechanism:</strong> Additive potassium-retaining effects</p>
            <p class="card-detail"><strong>Consequence:</strong> Hyperkalemia</p>
            <p class="card-detail"><strong>Action:</strong> Monitor serum potassium closely</p>
            <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 7</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #eab308;">
            <h4>🟡 Potassium Supplements / Salt Substitutes <span class="card-badge card-badge-yellow">MONITOR</span></h4>
            <p class="card-detail"><strong>Mechanism:</strong> Additive potassium load</p>
            <p class="card-detail"><strong>Consequence:</strong> Hyperkalemia</p>
            <p class="card-detail"><strong>Action:</strong> Monitor serum potassium</p>
            <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 7</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #eab308;">
            <h4>🟡 NSAIDs (COX-2 Inhibitors, Aspirin) <span class="card-badge card-badge-yellow">MONITOR</span></h4>
            <p class="card-detail"><strong>Mechanism:</strong> NSAIDs reduce renal blood flow and GFR</p>
            <p class="card-detail"><strong>Consequence:</strong> Worsening renal function (acute renal failure) in elderly/volume-depleted patients</p>
            <p class="card-detail"><strong>Action:</strong> Monitor renal function periodically</p>
            <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 7</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #eab308;">
            <h4>🟡 Lithium <span class="card-badge card-badge-yellow">MONITOR</span></h4>
            <p class="card-detail"><strong>Mechanism:</strong> Reduced renal lithium clearance</p>
            <p class="card-detail"><strong>Consequence:</strong> Reversible increase in serum lithium concentrations (toxicity risk)</p>
            <p class="card-detail"><strong>Action:</strong> Monitor lithium levels strictly</p>
            <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 7</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 🔵 Transporter Interactions (OATP1B1/1B3)")
        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #3b82f6;">
            <h4>🔵 Statins (Atorvastatin, Simvastatin, Pravastatin) <span class="card-badge card-badge-blue">MONITOR</span></h4>
            <p class="card-detail"><strong>Mechanism:</strong> Sacubitril inhibits OATP1B1/1B3 transporters</p>
            <p class="card-detail"><strong>Consequence:</strong> May increase systemic exposure of statins</p>
            <p class="card-detail"><strong>Action:</strong> No dose adjustment needed; monitor for statin-related side effects (myalgia, rhabdomyolysis)</p>
            <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 12</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #3b82f6;">
            <h4>🔵 Sildenafil <span class="card-badge card-badge-blue">MONITOR</span></h4>
            <p class="card-detail"><strong>Mechanism:</strong> Additive vasodilatory effects</p>
            <p class="card-detail"><strong>Consequence:</strong> Additional blood pressure reduction</p>
            <p class="card-detail"><strong>Action:</strong> Monitor blood pressure</p>
            <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Label Section 7</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🟢 Verified Safe & CYP450 Profile"):
        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #22c55e;">
            <h4>✅ Warfarin <span class="card-badge card-badge-green">SAFE</span></h4>
            <p class="card-detail">No effect on INR or prothrombin time</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #22c55e;">
            <h4>✅ Digoxin <span class="card-badge card-badge-green">SAFE</span></h4>
            <p class="card-detail">No clinically relevant interaction</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #22c55e;">
            <h4>✅ Omeprazole <span class="card-badge card-badge-green">SAFE</span></h4>
            <p class="card-detail">No effect on pharmacokinetics</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #22c55e;">
            <h4>✅ Metformin <span class="card-badge card-badge-green">SAFE</span></h4>
            <p class="card-detail">No effect on pharmacokinetics</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <h4>Sacubitril/Valsartan CYP Metabolism:</h4>
        <ul>
            <li><strong>Substrates of:</strong> Sacubitril — Esterases (NOT CYP); Valsartan — CYP2C9 (minimal, ~20%)</li>
            <li><strong>Inhibits:</strong> Does NOT inhibit CYP1A2, 2C9, 2C19, 2D6, or 3A4</li>
            <li><strong>Induces:</strong> Does NOT induce CYP450 enzymes</li>
        </ul>
        <p><strong>Clinical Significance:</strong> Very low risk of CYP-mediated drug interactions. Main interaction concern is via OATP1B1/1B3 transporter inhibition (statins) and pharmacodynamic effects (RAAS blockade, potassium).</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 8: COMPARISON ====================
with tabs[7]:
    st.header("📊 Comparison with Similar Drugs")

    st.markdown("### 🔬 Sacubitril/Valsartan vs. Alternative HF Therapies")
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #e74c3c; border: 2px solid #e74c3c;">
        <h4>🏆 ENTRESTO (Sacubitril/Valsartan)</h4>
        <p class="card-detail"><strong>Class:</strong> Angiotensin Receptor-Neprilysin Inhibitor (ARNI)</p>
        <p class="card-detail"><strong>Use:</strong> Chronic heart failure (HFrEF) — adults and pediatrics ≥1 year</p>
        <p class="card-detail"><strong>Mechanism:</strong> Dual-acting: Neprilysin inhibition + AT1 receptor blockade</p>
        <p class="card-detail"><strong>Key Toxicity:</strong> Hypotension (18%), Angioedema (0.5%)</p>
        <p class="card-detail"><strong>Food:</strong> With or without food</p>
        <p class="card-detail"><strong>Efficacy:</strong> <span class="card-badge card-badge-green">Superior to Enalapril — 20% CV death reduction (PARADIGM-HF)</span></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-item">
        <h4>💊 Enalapril (ACE Inhibitor)</h4>
        <p class="card-detail"><strong>Class:</strong> ACE Inhibitor</p>
        <p class="card-detail"><strong>Use:</strong> Heart failure, hypertension</p>
        <p class="card-detail"><strong>Mechanism:</strong> ACE inhibition → reduces angiotensin II and aldosterone</p>
        <p class="card-detail"><strong>Key Toxicity:</strong> Cough (13%), Hyperkalemia (14%), Angioedema (0.2%)</p>
        <p class="card-detail"><strong>Food:</strong> With or without food</p>
        <p class="card-detail"><strong>Efficacy:</strong> Standard of care comparator; inferior to Entresto in PARADIGM-HF</p>
    </div>
    <div class="card-item">
        <h4>💊 Valsartan (ARB — Standalone)</h4>
        <p class="card-detail"><strong>Class:</strong> Angiotensin II Receptor Blocker (ARB)</p>
        <p class="card-detail"><strong>Use:</strong> Heart failure, hypertension, post-MI</p>
        <p class="card-detail"><strong>Mechanism:</strong> AT1 receptor blockade only</p>
        <p class="card-detail"><strong>Key Toxicity:</strong> Less cough than ACEi; Hyperkalemia, Hypotension</p>
        <p class="card-detail"><strong>Food:</strong> With or without food</p>
        <p class="card-detail"><strong>Efficacy:</strong> ACEi-equivalent for HF; lacks neprilysin inhibition benefit</p>
    </div>
    <div class="card-item">
        <h4>💊 Carvedilol (Beta-Blocker)</h4>
        <p class="card-detail"><strong>Class:</strong> Non-selective Beta-Blocker with Alpha-1 blockade</p>
        <p class="card-detail"><strong>Use:</strong> Heart failure (HFrEF), hypertension</p>
        <p class="card-detail"><strong>Mechanism:</strong> Beta-1/Beta-2 and Alpha-1 adrenergic blockade</p>
        <p class="card-detail"><strong>Key Toxicity:</strong> Bradycardia, Fatigue, Hypotension</p>
        <p class="card-detail"><strong>Food:</strong> Take with food to slow absorption</p>
        <p class="card-detail"><strong>Efficacy:</strong> Proven mortality benefit in HFrEF; used as adjunct to ARNI</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("🏆 When to Choose & Key Differentiators"):
        col1, col2 = st.columns(2)
    
        with col1:
            st.markdown("""
            <div class="success-box">
            <h4>✅ Choose Sacubitril/Valsartan When:</h4>
            <ul>
                <li>HFrEF patient on guideline-directed medical therapy</li>
                <li>Switching from ACEi/ARB for superior outcomes (after 36-hr washout from ACEi)</li>
                <li>Pediatric HF with systemic LV systolic dysfunction (≥1 year)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="warning-box">
            <h4>❌ Avoid Sacubitril/Valsartan When:</h4>
            <ul>
                <li>History of angioedema with ACEi/ARB</li>
                <li>Pregnancy (Boxed Warning — fetal toxicity)</li>
                <li>Concomitant ACEi use (36-hour washout not observed)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("### 📈 Key Differentiators")
        st.markdown("""
        <div class="info-box">
        <h4>What Makes Sacubitril/Valsartan Unique:</h4>
        </div>
        <div class="card-item" style="border-left: 4px solid #3b82f6;">
            <h4>🧬 First-in-Class ARNI</h4>
            <p class="card-detail">Only FDA-approved ARNI combining neprilysin inhibition with ARB — dual mechanism provides neurohormonal modulation beyond RAAS blockade alone</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #22c55e;">
            <h4>🏆 PARADIGM-HF Landmark Trial</h4>
            <p class="card-detail">Superior to Enalapril: 20% reduction in CV death, 21% reduction in HF hospitalization — trial stopped early due to overwhelming benefit</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #7c3aed;">
            <h4>👶 Pediatric Approval</h4>
            <p class="card-detail">Approved for pediatric patients ≥1 year with symptomatic HF and systemic LV systolic dysfunction — one of few HF therapies with pediatric labeling</p>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 9: REFERENCES ====================
with tabs[8]:
    st.header("📚 References and Sources")

    st.markdown("### 📋 1. Regulatory & Official Prescribing Information")
    st.markdown("""
    <div class="reference-item">
        <strong>FDA Drug Database (Application No. 207620)</strong>
        <p class="card-detail">Official U.S. Food and Drug Administration registry page containing the most up-to-date label, approval history, and clinical pharmacology reviews specifically for Sacubitril/Valsartan.</p>
        <a href="https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=207620" target="_blank">🔗 https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=207620</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>EMA European Public Assessment Report (EPAR)</strong>
        <p class="card-detail">The European Medicines Agency's comprehensive overview, clinical characteristics, and authorization details for Entresto.</p>
        <a href="https://www.ema.europa.eu/en/medicines/human/EPAR/entresto" target="_blank">🔗 https://www.ema.europa.eu/en/medicines/human/EPAR/entresto</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔬 2. Pivotal Clinical Trials")
    st.markdown("""
    <div class="reference-item">
        <strong>PARADIGM-HF Trial (NEJM - PMID: 25176015)</strong>
        <p class="card-detail">Angiotensin–Neprilysin Inhibition versus Enalapril in Heart Failure. The landmark study proving Entresto's superiority over ACE inhibitors in reducing cardiovascular mortality.</p>
        <a href="https://pubmed.ncbi.nlm.nih.gov/25176015/" target="_blank">🔗 https://pubmed.ncbi.nlm.nih.gov/25176015/</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>PARAGON-HF Trial (NEJM - PMID: 31475594)</strong>
        <p class="card-detail">Angiotensin-Neprilysin Inhibition in Heart Failure with Preserved Ejection Fraction. Evaluation of Sacubitril/Valsartan in HFpEF patients.</p>
        <a href="https://pubmed.ncbi.nlm.nih.gov/31475594/" target="_blank">🔗 https://pubmed.ncbi.nlm.nih.gov/31475594/</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>PIONEER-HF Trial (NEJM - PMID: 30415601)</strong>
        <p class="card-detail">Angiotensin-Neprilysin Inhibition in Acute Decompensated Heart Failure. Study on initiating Sacubitril/Valsartan in hospitalized patients.</p>
        <a href="https://pubmed.ncbi.nlm.nih.gov/30415601/" target="_blank">🔗 https://pubmed.ncbi.nlm.nih.gov/30415601/</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📖 3. Pharmacology & Drug Interactions")
    st.markdown("""
    <div class="reference-item">
        <strong>StatPearls (NCBI Bookshelf)</strong>
        <p class="card-detail">A comprehensive academic and clinical review of the Sacubitril/Valsartan mechanism of action, enzyme interactions, and toxicity.</p>
        <a href="https://www.ncbi.nlm.nih.gov/books/NBK507904/" target="_blank">🔗 https://www.ncbi.nlm.nih.gov/books/NBK507904/</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="reference-item">
        <strong>Drugs.com Professional Interaction Checker</strong>
        <p class="card-detail">A dedicated interaction checker page specifically for Entresto, categorizing interactions by severity.</p>
        <a href="https://www.drugs.com/drug-interactions/sacubitril-valsartan,entresto.html" target="_blank">🔗 https://www.drugs.com/drug-interactions/sacubitril-valsartan,entresto.html</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🌐 4. Healthcare Professional Guidelines")
    st.markdown("""
    <div class="reference-item">
        <strong>ENTRESTO HCP Official Portal</strong>
        <p class="card-detail">Novartis's official resource for healthcare providers, containing dosing algorithms, switching protocols from ACEi/ARBs, and safety guidelines for Entresto.</p>
        <a href="https://www.entrestohcp.com/" target="_blank">🔗 https://www.entrestohcp.com/</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.info("""
    **📊 Data Accuracy Statement**

    All information in this application has been verified against:
    - FDA Prescribing Information
    - Peer-reviewed clinical studies and guidelines

    **📅 Last Updated:** February 2026  
    **📌 Version:** 1.0.0  
    **✅ Verification Status:** All references checked and validated  
    **🔬 Methodology:** Pre-Pharmacode V2.5 Standard with Triple-Verification
    """)

# ==================== TAB 10: NOVARTIS AG ====================
with tabs[9]:
    st.header("🏢 Novartis AG — Manufacturer Profile")

    st.markdown("""
    <div class="info-box">
    <h4>🏛️ Corporate Overview</h4>
    <p class="card-detail">🏢 <strong>Company Name:</strong> Novartis AG</p>
    <p class="card-detail">📍 <strong>Headquarters:</strong> Basel, Switzerland</p>
    <p class="card-detail">📜 <strong>History:</strong> Formed in 1996 through the merger of two major Swiss companies, <strong>Ciba-Geigy</strong> and <strong>Sandoz</strong>.</p>
    <p class="card-detail">🌍 <strong>Global Standing:</strong> Consistently ranks as one of the largest and most highly valued multinational pharmaceutical companies in the world.</p>
    <p class="card-detail">🎯 <strong>Core Therapeutic Areas:</strong> Cardiovascular, Renal and Metabolism (CRM), Oncology, Immunology, and Neuroscience.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("❤️ Leadership in Cardiovascular Health"):

        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #e74c3c;">
            <h4>💊 The Entresto Innovation</h4>
            <p class="card-detail">Novartis developed <strong>Entresto (sacubitril/valsartan)</strong>, the first-in-class Angiotensin Receptor-Neprilysin Inhibitor (ARNI). It revolutionized the treatment of Heart Failure with reduced Ejection Fraction (HFrEF) by demonstrating significant superiority over the decades-old standard of care (enalapril).</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #22c55e;">
            <h4>🏆 Landmark Evidence (PARADIGM-HF)</h4>
            <p class="card-detail">Designed and sponsored by Novartis, the <strong>PARADIGM-HF trial</strong> was prematurely stopped due to overwhelming efficacy, showing a <strong>20% reduction in cardiovascular death</strong> and a <strong>21% reduction in heart failure hospitalizations</strong>.</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #3b82f6;">
            <h4>🔬 FortiHFy Clinical Program</h4>
            <p class="card-detail">Novartis manages one of the largest global clinical trial programs in the heart failure space. <strong>FortiHFy</strong> comprises over 40 active or planned studies (including <strong>PIONEER-HF</strong> and <strong>PARAGON-HF</strong>) aimed at generating robust data on symptom reduction and quality of life across the heart failure spectrum.</p>
        </div>
        <div class="card-item" style="border-left: 4px solid #7c3aed;">
            <h4>🌍 Population Health Initiatives</h4>
            <p class="card-detail">Novartis leads global initiatives (like <strong>CARDIO4Cities</strong>) aimed at improving cardiovascular and metabolic health in urban centers by systematically addressing blood pressure control and preventing strokes and heart attacks.</p>
        </div>
        """, unsafe_allow_html=True)

    with st.expander("💡 Quick Facts & Commitments"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div class="success-box">
            <h4>🔬 R&D Investment</h4>
            <p>The company invests <strong>billions annually</strong> in research and development to discover transformative treatments for diseases with high unmet medical needs.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="info-box">
            <h4>🤝 Healthcare Partnerships</h4>
            <p>Novartis frequently collaborates with national healthcare systems (such as the <strong>NHS in the UK</strong>) to implement innovative, population-level approaches to managing cardiovascular risk.</p>
            </div>
            """, unsafe_allow_html=True)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2rem 0;">
    <p><strong>ENTRESTO (Sacubitril/Valsartan) Professional Drug Information</strong></p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        ⚠️ <em>This information is for healthcare professionals only. 
        Always consult the full prescribing information and clinical judgment when making treatment decisions.</em>
    </p>
</div>
""", unsafe_allow_html=True)



