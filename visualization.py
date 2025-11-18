import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

# Create the data
data = {
    'Dimension': [
        'Intent',
        'Access & Oversight',
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

# Display styled pandas DataFrame
print("=" * 150)
print("ETHICAL CONSIDERATIONS & FRAMEWORKS - Flock Safety ALPR Analysis")
print("=" * 150)
print("\nOur team analyzed the ethical dimensions of Flock Safety ALPR cameras.")
print("The system followed a utilitarian framework focused on maximizing safety,")
print("but often at the cost of privacy and fairness.\n")
print("=" * 150)

# Create styled output
styled_df = df.style\
    .set_properties(**{
        'text-align': 'left',
        'white-space': 'pre-wrap',
        'word-wrap': 'break-word'
    })\
    .set_table_styles([
        {'selector': 'th', 'props': [('background-color', '#2c3e50'), 
                                      ('color', 'white'), 
                                      ('font-weight', 'bold'),
                                      ('text-align', 'center'),
                                      ('padding', '12px')]},
        {'selector': 'td', 'props': [('padding', '10px'),
                                      ('border', '1px solid #ddd')]},
        {'selector': 'tr:nth-of-type(even)', 'props': [('background-color', '#f9f9f9')]},
        {'selector': 'tr:hover', 'props': [('background-color', '#f5f5f5')]},
    ])

# Print the table
print(df.to_string(index=False))
print("\n" + "=" * 150)

# Create a visual matplotlib figure
fig, ax = plt.subplots(figsize=(18, 10))
ax.axis('tight')
ax.axis('off')

# Add title and subtitle
fig.suptitle('Ethical Considerations & Frameworks', 
             fontsize=20, fontweight='bold', y=0.98)
plt.text(0.5, 0.94, 
         'Analysis of Flock Safety ALPR Cameras: Utilitarian vs. Rights-Based Approaches',
         ha='center', fontsize=11, style='italic', wrap=True,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.3))

# Create table with custom styling
table_data = []
for idx, row in df.iterrows():
    table_data.append([
        row['Dimension'],
        row['What They Got Right ✅'],
        row['What They Got Wrong ⚠️'],
        row['Ethical Framework Used'],
        row['Better Alternative Framework']
    ])

table = ax.table(cellText=table_data,
                 colLabels=['Dimension', 'What They Got Right ✅', 'What They Got Wrong ⚠️', 
                           'Ethical Framework Used', 'Better Alternative Framework'],
                 cellLoc='left',
                 loc='center',
                 colWidths=[0.12, 0.22, 0.22, 0.22, 0.22])

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 2.5)

# Color header row
for i in range(5):
    cell = table[(0, i)]
    cell.set_facecolor('#2c3e50')
    cell.set_text_props(weight='bold', color='white')

# Color alternating rows and dimension column
colors = ['#e8f4f8', '#f9f9f9']
for i in range(1, 6):
    for j in range(5):
        cell = table[(i, j)]
        cell.set_facecolor(colors[i % 2])
        cell.set_text_props(wrap=True)
        
        # Make dimension column bold
        if j == 0:
            cell.set_text_props(weight='bold', wrap=True)
            cell.set_facecolor('#d4e6f1')

# Add borders
for key, cell in table.get_celld().items():
    cell.set_linewidth(0.5)
    cell.set_edgecolor('#bbb')

plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.savefig('/tmp/ethical_analysis_table.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none')
print(f"\n✅ Visual table saved to: /tmp/ethical_analysis_table.png")
print("📊 Opening the visualization...\n")

plt.show()
