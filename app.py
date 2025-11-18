import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Ethical Analysis - Flock Safety ALPR",
    page_icon="🔒",
    layout="wide"
)

# Custom CSS for black and white styling
st.markdown("""
<style>
    /* Dark theme background */
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* Main content styling */
    .main .block-container {
        padding-top: 2rem;
    }
    
    /* Custom table styling */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 14px;
        background-color: #2a2a2a;
        border: 1px solid #444;
    }
    
    .custom-table thead {
        background-color: #1a1a1a;
        border-bottom: 2px solid #555;
    }
    
    .custom-table th {
        padding: 12px 15px;
        text-align: left;
        font-weight: 600;
        font-size: 13px;
        color: #999;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .custom-table td {
        padding: 15px;
        border-bottom: 1px solid #333;
        color: #ddd;
        vertical-align: top;
    }
    
    .custom-table tbody tr {
        background-color: #2a2a2a;
    }
    
    .custom-table tbody tr:hover {
        background-color: #333;
    }
    
    .custom-table tbody tr td:first-child {
        font-weight: 600;
        color: #fff;
        background-color: #252525;
        width: 50px;
        text-align: center;
    }
    
    /* Title styling */
    h1 {
        color: #ffffff !important;
        font-size: 2.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Subtitle box */
    .subtitle-box {
        background-color: #2a2a2a;
        padding: 20px;
        border-left: 3px solid #555;
        margin-bottom: 30px;
        border-radius: 5px;
    }
    
    .subtitle-box h3 {
        color: #ccc;
        margin-top: 0;
        font-size: 1.1rem;
    }
    
    .subtitle-box p {
        color: #bbb;
        line-height: 1.6;
        margin-bottom: 0;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background-color: #444;
        margin: 2rem 0;
    }
    
    /* Metrics */
    div[data-testid="stMetricValue"] {
        font-size: 20px;
        color: #fff;
    }
    
    div[data-testid="metric-container"] {
        background-color: #2a2a2a;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #444;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #2a2a2a !important;
        color: #fff !important;
        border: 1px solid #444 !important;
        border-radius: 5px !important;
    }
    
    /* Success/Error boxes */
    .stSuccess, .stError, .stWarning, .stInfo {
        background-color: #2a2a2a !important;
        border-left: 3px solid #666 !important;
        color: #ddd !important;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1>🔒 Ethical Considerations & Frameworks</h1>', unsafe_allow_html=True)

# Subtitle box
st.markdown("""
<div class="subtitle-box">
    <h3>Analysis of Flock Safety ALPR Cameras</h3>
    <p>Our team analyzed the ethical dimensions of Flock Safety ALPR cameras. The system followed a utilitarian framework focused on maximizing safety, but often at the cost of privacy and fairness. A rights-based or justice-centered ethical lens could have addressed these concerns more equitably.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

# Create the data (matching screenshot exactly)
data = {
    '#': ['0', '1', '2', '3', '4'],
    'Dimension': [
        'Intent',
        'Access &\nOversight',
        'Data Retention',
        'Usage Scope',
        'Impact'
    ],
    'What They Got Right ✅': [
        'Reduced crime and improved safety',
        'Audit logs to trace misuse',
        '30-day auto-delete to reduce long-term risks',
        'Focused on cars, not facial recognition',
        'Solved crimes and assisted in public safety'
    ],
    'What They Got Wrong ⚠️': [
        'Overlooked privacy and individual rights',
        'No auto-flagging or independent monitoring',
        'Data can be exported/shared before deletion',
        'Enabled mass surveillance without user consent',
        'False alerts led to traumatic police stops'
    ],
    'Ethical Framework Used': [
        'Utilitarianism – outcome-driven',
        'Virtue Ethics – assumes good actors',
        'Rule-Based Logic – user-governed behavior',
        'Consequentialism – public safety benefit',
        'Ends-justify-means logic'
    ],
    'Better Alternative Framework': [
        'Rights-Based Ethics – prioritizes consent and autonomy',
        'Justice Ethics – supports external, unbiased oversight',
        'Deontological Ethics – enforce strict data controls',
        'Social Contract Theory – requires community-informed data governance',
        'Engineering Code of Ethics – "Avoid harm"; "Protect public welfare"'
    ]
}

df = pd.DataFrame(data)

# Create HTML table
html_table = '<table class="custom-table"><thead><tr>'
for col in df.columns:
    html_table += f'<th>{col}</th>'
html_table += '</tr></thead><tbody>'

for idx, row in df.iterrows():
    html_table += '<tr>'
    for col in df.columns:
        html_table += f'<td>{row[col]}</td>'
    html_table += '</tr>'
    
html_table += '</tbody></table>'

# Display the HTML table
st.markdown(html_table, unsafe_allow_html=True)

st.markdown('<hr>', unsafe_allow_html=True)

# # Add expandable sections for each dimension
# st.subheader("📊 Detailed Analysis by Dimension")

# for idx, row in df.iterrows():
#     dimension = row['Dimension'].replace('\n', ' ')
#     with st.expander(f"**{dimension}**"):
#         col1, col2 = st.columns(2)
        
#         with col1:
#             st.success("**What They Got Right**")
#             st.write(row['What They Got Right ✅'])
#             st.info(f"**Framework Used:** {row['Ethical Framework Used']}")
        
#         with col2:
#             st.error("**What They Got Wrong**")
#             st.write(row['What They Got Wrong ⚠️'])
#             st.warning(f"**Better Alternative:** {row['Better Alternative Framework']}")

# # Summary metrics
# st.markdown('<hr>', unsafe_allow_html=True)
# st.subheader("📈 Summary Insights")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric(
#         label="Primary Framework Used",
#         value="Utilitarianism",
#         delta="Outcome-driven",
#         delta_color="off"
#     )

# with col2:
#     st.metric(
#         label="Key Issue",
#         value="Privacy Concerns",
#         delta="Individual rights overlooked",
#         delta_color="inverse"
#     )

# with col3:
#     st.metric(
#         label="Recommended Approach",
#         value="Rights-Based Ethics",
#         delta="Better balance needed",
#         delta_color="normal"
#     )

# # Footer
# st.markdown('<hr>', unsafe_allow_html=True)
# st.caption("🔍 This analysis examines the ethical implications of automated surveillance technology and proposes alternative frameworks for more equitable implementation.")
