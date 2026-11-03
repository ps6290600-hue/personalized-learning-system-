import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for cleaner graphs
sns.set_theme(style="whitegrid")

# 1. Load the Dataset
print("Loading dataset...")
df = pd.read_csv('personalized_learning_dataset.csv')

# 2. Display Basic Information & Summary Statistics
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Summary Statistics (Ratings & Study Hours) ---")
print(df[['rating', 'completion_pct', 'prior_gpa', 'weekly_study_hours']].describe())

# 3. Generate Visualizations for Your Project Report / Presentation

# Figure 1: Distribution of Student Prior GPA
plt.figure(figsize=(8, 5))
sns.histplot(df['prior_gpa'], kde=True, color='purple', bins=20)
plt.title('Distribution of Student Prior GPA', fontsize=14, fontweight='bold')
plt.xlabel('Prior GPA', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.savefig('gpa_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

# Figure 2: Average Rating by Resource Type & Difficulty
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='resource_type', y='rating', hue='difficulty_level', palette='viridis')
plt.title('Average Student Rating by Resource Type and Difficulty', fontsize=14, fontweight='bold')
plt.xlabel('Resource Type', fontsize=12)
plt.ylabel('Average Rating (1-5)', fontsize=12)
plt.legend(title='Difficulty Level')
plt.savefig('resource_ratings_by_type.png', dpi=300, bbox_inches='tight')
plt.show()

# Figure 3: Correlation Heatmap of Numerical Features
plt.figure(figsize=(8, 6))
numeric_cols = ['rating', 'completion_pct', 'time_spent_mins', 'prior_gpa', 'weekly_study_hours', 'completed_topics_count']
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of Student Behavior & Performance', fontsize=14, fontweight='bold')
plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nEDA completed! Charts saved as PNG images for your report.")