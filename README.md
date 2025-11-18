# 🔒 Ethical Analysis - Flock Safety ALPR

An interactive Streamlit dashboard analyzing the ethical dimensions of Flock Safety's Automated License Plate Reader (ALPR) cameras.

## 📊 Overview

This project examines the ethical frameworks used in the implementation of Flock Safety ALPR cameras, comparing utilitarian approaches against rights-based and justice-centered alternatives.

## 🚀 Features

- **Interactive Dashboard**: Beautiful Streamlit web interface
- **Comprehensive Analysis**: Covers 5 key ethical dimensions
- **Visual Comparisons**: Side-by-side view of what worked vs. what didn't
- **Framework Recommendations**: Suggests better ethical approaches
- **Expandable Details**: Deep dive into each dimension
- **Summary Metrics**: Key insights at a glance

## 📦 Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/EthicsFinal.git
cd EthicsFinal
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install streamlit pandas matplotlib numpy 'altair<6' 'pydeck<1'
```

> **Note**: The app uses `st.table()` which doesn't require pyarrow, avoiding compilation issues.

## 🎯 Usage

### Run the Streamlit App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Run the Matplotlib Visualization
```bash
python visualization.py
```

This generates a high-resolution PNG visualization saved to your current directory.

## 📁 Project Structure

```
EthicsFinal/
├── app.py                  # Main Streamlit application
├── visualization.py        # Matplotlib static visualization
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🔍 Ethical Dimensions Analyzed

1. **🎯 Intent** - Purpose and goals of the system
2. **👁️ Access & Oversight** - Monitoring and accountability
3. **💾 Data Retention** - How long data is kept
4. **📡 Usage Scope** - What the system actually tracks
5. **⚡ Impact** - Real-world consequences

## 🎨 Technologies Used

- **Streamlit** - Interactive web application framework
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Static visualization generation
- **Python 3.14+** - Programming language

## 📈 Key Findings

- **Primary Framework Used**: Utilitarianism (outcome-driven)
- **Key Issue**: Privacy concerns and overlooked individual rights
- **Recommended Approach**: Rights-based ethics with community-informed governance

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Authors

- Your Team Name

## 🙏 Acknowledgments

- Analysis based on real-world case study of Flock Safety ALPR technology
- Built as part of an ethical considerations in technology course

---

Made with ❤️ for ethical technology implementation
