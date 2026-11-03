import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

class PersonalizedLearningRecommender:
    def __init__(self, student_profiles_path, resources_path, interactions_path):
        print("Initializing Recommendation System...")
        self.df_students = pd.read_csv(student_profiles_path)
        self.df_resources = pd.read_csv(resources_path)
        self.df_interactions = pd.read_csv(interactions_path)
        
    def recommend_for_student(self, student_id, top_n=5):
        """
        Generates personalized learning resource recommendations for a given student ID.
        """
        # 1. Fetch student details
        student_match = self.df_students[self.df_students['student_id'] == student_id]
        if student_match.empty:
            return f"Student ID '{student_id}' not found!"
        
        student = student_match.iloc[0]
        print(f"\n--- Student Profile ---")
        print(f"ID: {student['student_id']} | GPA: {student['prior_gpa']} | Interest: {student['primary_interest']} | Style: {student['learning_style']}")
        
        # 2. Filter out resources the student has already completed/interacted with
        interacted_resources = self.df_interactions[
            self.df_interactions['student_id'] == student_id
        ]['resource_id'].tolist()
        
        available_resources = self.df_resources[
            ~self.df_resources['resource_id'].isin(interacted_resources)
        ].copy()
        
        if available_resources.empty:
            available_resources = self.df_resources.copy() # Fallback if all interacted
            
        # 3. Calculate Match Score based on Student Profile
        scores = []
        for _, res in available_resources.iterrows():
            score = 0.0
            
            # Rule 1: Primary Interest match (Highest weight)
            if student['primary_interest'] == res['topic']:
                score += 3.0
                
            # Rule 2: Learning Style & Resource Type compatibility
            style = student['learning_style']
            rtype = res['resource_type']
            if (style == 'Visual' and rtype in ['Video', 'Interactive Quiz']) or \
               (style == 'Reading/Writing' and rtype == 'Article/Textbook') or \
               (style == 'Kinesthetic' and rtype == 'Hands-on Project') or \
               (style == 'Auditory' and rtype == 'Video'):
                score += 2.0
                
            # Rule 3: Academic level (GPA-based difficulty matching)
            gpa = student['prior_gpa']
            diff = res['difficulty_level']
            if gpa >= 3.5 and diff == 'Advanced':
                score += 1.5
            elif 2.7 <= gpa < 3.5 and diff == 'Intermediate':
                score += 1.5
            elif gpa < 2.7 and diff == 'Beginner':
                score += 1.5
            else:
                score += 0.5 # Default baseline
                
            # Add small bonus for overall resource average rating
            score += (res['avg_rating'] / 5.0) * 0.5
            
            scores.append(score)
            
        available_resources['match_score'] = scores
        
        # 4. Sort and get Top N recommendations
        recommendations = available_resources.sort_values(by='match_score', ascending=False).head(top_n)
        return recommendations[['resource_id', 'title', 'topic', 'resource_type', 'difficulty_level', 'avg_rating', 'match_score']]

# --- Execution Example ---
if __name__ == "__main__":
    # Initialize the recommender
    recommender = PersonalizedLearningRecommender(
        'student_profiles.csv', 
        'learning_resources.csv', 
        'student_interactions.csv'
    )
    
    # Test with a sample student ID from your dataset (e.g., 'STU_101')
    sample_student_id = 'STU_101'
    recommended_resources = recommender.recommend_for_student(sample_student_id, top_n=5)
    
    print(f"\nTop Personalized Recommendations for {sample_student_id}:")
    print(recommended_resources.to_string(index=False))