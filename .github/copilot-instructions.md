# AI Coding Agent Instructions - EthicsFinal

## Project Overview
This is an **ethical analysis dashboard** for Flock Safety ALPR cameras using Streamlit. It presents a 5-dimension comparative analysis of utilitarian vs. rights-based ethical frameworks. The project consists of two visualization approaches: an interactive web dashboard (`app.py`) and a static matplotlib visualization (`visualization.py`).

## Architecture & Data Flow
- **Single source of truth**: The 5-dimension ethical analysis data is duplicated in both `app.py` and `visualization.py` as hardcoded dictionaries
- **No external data sources**: All content is embedded directly in code
- **Two output modes**:
  - Interactive web UI via Streamlit (port 8501)
  - Static PNG export via matplotlib (`/tmp/ethical_analysis_table.png`)

## Development Workflow

### Running the Application
```bash
# Always activate venv first (already created in project)
source venv/bin/activate

# Run interactive dashboard
streamlit run app.py

# Generate static visualization
python visualization.py
```

### Dependencies Management
- Install via: `pip install -r requirements.txt`
- **Critical constraint**: Use `altair<6` and `pydeck<1` to avoid version conflicts with Streamlit
- Python 3.14+ compatible (per README)

## Project-Specific Conventions

### Styling Pattern (app.py)
- **Dark theme enforced**: All UI uses custom CSS with black (`#1a1a1a`) background and white text
- Custom CSS embedded via `st.markdown()` with `unsafe_allow_html=True`
- Table styling uses `.custom-table` class with specific hover states and alternating backgrounds
- **Never** use Streamlit's default light theme or standard dataframe styling

### Data Structure Pattern
The core data is a 5-row dictionary with these exact keys (maintain consistency):
```python
{
    'Dimension': [...],  # 5 ethical dimensions
    'What They Got Right ✅': [...],
    'What They Got Wrong ⚠️': [...],
    'Ethical Framework Used': [...],
    'Better Alternative Framework': [...]
}
```

### HTML Table Generation (app.py)
- Build HTML manually rather than using `st.dataframe()` or `st.table()`
- Include `#` column with indices 0-4 for row numbering
- Handle newlines in 'Access &\nOversight' dimension name explicitly

### Matplotlib Export Pattern (visualization.py)
- Always save to `/tmp/ethical_analysis_table.png` at 300 DPI
- Use alternating row colors: `['#e8f4f8', '#f9f9f9']`
- Header row background: `#2c3e50` with white bold text
- Dimension column (first column) gets special treatment: bold text with `#d4e6f1` background

## Key Files

- **`app.py`** (264 lines): Streamlit dashboard with embedded CSS, HTML table generation, expandable sections, and summary metrics
- **`visualization.py`** (147 lines): Matplotlib-based static export with pandas styling and PNG output
- **`requirements.txt`**: Pin streamlit, pandas, matplotlib, numpy with version constraints

## Common Modifications

### Adding a New Ethical Dimension
1. Update data dictionary in **both** `app.py` and `visualization.py`
2. Increment row count in both files (currently 5 rows indexed 0-4)
3. Update summary metrics in `app.py` if framework counts change

### Styling Changes
- All custom CSS lives in the top `st.markdown()` block in `app.py`
- Color scheme is grayscale: backgrounds (`#1a1a1a`, `#2a2a2a`), borders (`#444`, `#333`), text (`#fff`, `#ddd`, `#ccc`)
- Hover effects require explicit `.custom-table tbody tr:hover` rules

### Testing Changes
- No automated tests exist; validation is visual
- Check both Streamlit app AND matplotlib output after data changes
- Verify dark theme renders correctly in browser at `localhost:8501`

## Troubleshooting

### "pyarrow compilation error"
- Already avoided: app uses `st.markdown()` + HTML instead of `st.dataframe()`
- Don't add pyarrow as a dependency

### Virtual Environment Issues
- Venv exists at `./venv/` - always activate before running commands
- If packages missing: `pip install -r requirements.txt` from activated venv

### Streamlit Port Already in Use
```bash
# Kill existing Streamlit process
pkill -f streamlit
# Or specify different port
streamlit run app.py --server.port 8502
```
