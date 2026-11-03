import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(page_title="Personalized Learning Recommendation System", layout="wide")

# Comprehensive Sub-Topic Mapping with Direct Learning Resources (Tutorials, Guides & Documentation)
subtopic_mapping = {
    'Artificial Intelligence': {
        'Beginner': [
            {"sub": "Introduction to AI and Turing Test", "title": "Google Developers ML Crash Course Overview", "type": "Textbook Chapter", "duration": 45, "rating": 4.8, "link": "https://developers.google.com/machine-learning/crash-course"},
            {"sub": "Uninformed and Informed Search Strategies", "title": "Stanford AI Search Algorithms Guide", "type": "Textbook Chapter", "duration": 60, "rating": 4.7, "link": "https://ai.stanford.edu/~pabbeel/cs221-lectures.html"},
            {"sub": "Propositional Logic and Knowledge Representation", "title": "GeeksforGeeks Knowledge Representation Tutorial", "type": "Article", "duration": 30, "rating": 4.5, "link": "https://www.geeksforgeeks.org/knowledge-representation-in-ai/"},
            {"sub": "Introduction to Expert Systems", "title": "Tutorialspoint Expert Systems Guide", "type": "Textbook Chapter", "duration": 40, "rating": 4.4, "link": "https://www.tutorialspoint.com/artificial_intelligence/artificial_intelligence_expert_systems.htm"}
        ],
        'Intermediate': [
            {"sub": "Constraint Satisfaction Problems", "title": "UC Berkeley CS188 CSP Lecture Notes", "type": "Textbook Chapter", "duration": 60, "rating": 4.9, "link": "https://ai.berkeley.edu/"},
            {"sub": "Adversarial Search and Minimax Algorithm", "title": "GeeksforGeeks Minimax Algorithm in Game Theory", "type": "Article", "duration": 50, "rating": 4.9, "link": "https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/"},
            {"sub": "Probabilistic Reasoning and Bayesian Networks", "title": "Probabilistic Graphical Models Study Guide", "type": "Textbook Chapter", "duration": 90, "rating": 4.8, "link": "https://www.coursera.org/learn/probabilistic-graphical-models"},
            {"sub": "Introduction to Natural Language Processing", "title": "Hugging Face NLP Free Learning Course Chapters", "type": "Textbook Chapter", "duration": 75, "rating": 4.9, "link": "https://huggingface.co/course/chapter1/1"}
        ],
        'Advanced': [
            {"sub": "Deep Learning Architectures (CNN, RNN)", "title": "DeepLearning.AI Specialization Documentation", "type": "Textbook Chapter", "duration": 120, "rating": 4.9, "link": "https://www.deeplearning.ai/"},
            {"sub": "Reinforcement Learning and Q-Learning", "title": "OpenAI Spinning Up in Deep Reinforcement Learning Guide", "type": "Textbook Chapter", "duration": 90, "rating": 4.8, "link": "https://spinningup.openai.com/en/latest/"},
            {"sub": "Computer Vision Fundamentals", "title": "PyTorch Official Computer Vision Tutorials", "type": "Textbook Chapter", "duration": 80, "rating": 4.7, "link": "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html"},
            {"sub": "AI Ethics, Safety, and Alignment", "title": "Stanford Institute for Human-Centered AI Research Papers", "type": "Article", "duration": 45, "rating": 4.6, "link": "https://hai.stanford.edu/"}
        ]
    },
    'Data Structures & Algorithms': {
        'Beginner': [
            {"sub": "Arrays and Strings Fundamentals", "title": "LeetCode Arrays 101 Learning Documentation", "type": "Textbook Chapter", "duration": 60, "rating": 4.9, "link": "https://leetcode.com/explore/learn/card/arrays-101/"},
            {"sub": "Singly and Doubly Linked Lists", "title": "Programiz Linked List Tutorial with Code Examples", "type": "Article", "duration": 40, "rating": 4.7, "link": "https://www.programiz.com/dsa/linked-list"},
            {"sub": "Stacks Implementation & Applications", "title": "GeeksforGeeks Stack Data Structure Guide", "type": "Article", "duration": 45, "rating": 4.8, "link": "https://www.geeksforgeeks.org/stack-data-structure/"},
            {"sub": "Queues and Circular Queues", "title": "Programiz Queue Data Structure Tutorial", "type": "Textbook Chapter", "duration": 30, "rating": 4.6, "link": "https://www.programiz.com/dsa/queue"}
        ],
        'Intermediate': [
            {"sub": "Binary Trees and Tree Traversals", "title": "VisuAlgo Binary Search Tree Reference Guide", "type": "Textbook Chapter", "duration": 45, "rating": 4.9, "link": "https://visualgo.net/en/bst"},
            {"sub": "Binary Search Trees (BST)", "title": "Programiz Binary Search Tree Operations Guide", "type": "Textbook Chapter", "duration": 60, "rating": 4.8, "link": "https://www.programiz.com/dsa/binary-search-tree"},
            {"sub": "Heaps and Priority Queues", "title": "GeeksforGeeks Heap Data Structure Tutorial", "type": "Article", "duration": 50, "rating": 4.7, "link": "https://www.geeksforgeeks.org/heap-data-structure/"},
            {"sub": "Hashing and Collision Resolution", "title": "Real Python Dictionary Internals & Hashing Guide", "type": "Textbook Chapter", "duration": 60, "rating": 4.9, "link": "https://realpython.com/python-dicts/"}
        ],
        'Advanced': [
            {"sub": "AVL Trees and Red-Black Trees", "title": "USFCA Data Structure Visualizations Reference", "type": "Textbook Chapter", "duration": 90, "rating": 4.7, "link": "https://www.cs.usfca.edu/~galles/visualization/AVL.html"},
            {"sub": "Dynamic Programming (Knapsack, LCS)", "title": "GeeksforGeeks Dynamic Programming Study Notes", "type": "Textbook Chapter", "duration": 120, "rating": 4.9, "link": "https://www.geeksforgeeks.org/dynamic-programming/"},
            {"sub": "Shortest Path Algorithms (Dijkstra, Bellman-Ford)", "title": "MIT OpenCourseWare Graph Algorithms Notes", "type": "Textbook Chapter", "duration": 90, "rating": 4.9, "link": "https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/"},
            {"sub": "Graph Traversals and Applications", "title": "HackerRank Graph Theory Study Reference", "type": "Textbook Chapter", "duration": 60, "rating": 4.8, "link": "https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=graph-theory"}
        ]
    },
    'Machine Learning': {
        'Beginner': [
            {"sub": "Supervised vs Unsupervised Learning", "title": "Google Machine Learning Crash Course Guide", "type": "Textbook Chapter", "duration": 45, "rating": 4.9, "link": "https://developers.google.com/machine-learning/crash-course"},
            {"sub": "Linear Regression and Cost Functions", "title": "Scikit-Learn Linear Regression User Guide", "type": "Textbook Chapter", "duration": 30, "rating": 4.9, "link": "https://scikit-learn.org/stable/modules/linear_model.html"},
            {"sub": "Logistic Regression Classification", "title": "Scikit-Learn Logistic Regression Documentation", "type": "Textbook Chapter", "duration": 60, "rating": 4.8, "link": "https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html"},
            {"sub": "Data Preprocessing and Scikit-Learn Basics", "title": "Kaggle Intro to Machine Learning Tutorial", "type": "Textbook Chapter", "duration": 60, "rating": 4.9, "link": "https://www.kaggle.com/learn/intro-to-machine-learning"}
        ],
        'Intermediate': [
            {"sub": "Decision Trees and Random Forests", "title": "Scikit-Learn Ensemble Methods Reference", "type": "Textbook Chapter", "duration": 60, "rating": 4.8, "link": "https://scikit-learn.org/stable/modules/ensemble.html"},
            {"sub": "Support Vector Machines (SVM)", "title": "Scikit-Learn Support Vector Machines Documentation", "type": "Textbook Chapter", "duration": 40, "rating": 4.9, "link": "https://scikit-learn.org/stable/modules/svm.html"},
            {"sub": "Model Evaluation Metrics (Precision, Recall, F1)", "title": "Scikit-Learn Model Evaluation Metrics Guide", "type": "Article", "duration": 30, "rating": 4.7, "link": "https://scikit-learn.org/stable/modules/model_evaluation.html"},
            {"sub": "K-Means and Hierarchical Clustering", "title": "Scikit-Learn Clustering Reference Documentation", "type": "Textbook Chapter", "duration": 50, "rating": 4.8, "link": "https://scikit-learn.org/stable/modules/clustering.html"}
        ],
        'Advanced': [
            {"sub": "Gradient Boosting and XGBoost", "title": "XGBoost Official Python Documentation", "type": "Textbook Chapter", "duration": 90, "rating": 4.9, "link": "https://xgboost.readthedocs.io/en/stable/python/python_intro.html"},
            {"sub": "Hyperparameter Tuning and Grid Search", "title": "Scikit-Learn Hyperparameter Tuning Reference Guide", "type": "Textbook Chapter", "duration": 60, "rating": 4.8, "link": "https://scikit-learn.org/stable/modules/grid_search.html"},
            {"sub": "Dimensionality Reduction (PCA)", "title": "Scikit-Learn PCA Decomposition Documentation", "type": "Textbook Chapter", "duration": 45, "rating": 4.9, "link": "https://scikit-learn.org/stable/modules/decomposition.html"},
            {"sub": "Model Deployment and Serialization", "title": "Streamlit App Deployment Documentation", "type": "Textbook Chapter", "duration": 75, "rating": 4.9, "link": "https://docs.streamlit.io/deploy/streamlit-community-cloud"}
        ]
    },
    'HTML & CSS': {
        'Beginner': [
            {"sub": "HTML5 Document Structure and Semantic Tags", "title": "MDN Web Docs: Introduction to HTML", "type": "Textbook Chapter", "duration": 40, "rating": 4.9, "link": "https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML"},
            {"sub": "Forms, Inputs, and Validation", "title": "W3Schools HTML Forms Reference Guide", "type": "Textbook Chapter", "duration": 45, "rating": 4.8, "link": "https://www.w3schools.com/html/html_forms.asp"},
            {"sub": "CSS Selectors, Colors, and Typography", "title": "MDN Web Docs: CSS First Steps Tutorial", "type": "Textbook Chapter", "duration": 50, "rating": 4.9, "link": "https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps"},
            {"sub": "CSS Box Model and Display Properties", "title": "CSS-Tricks Complete Guide to the Box Model", "type": "Article", "duration": 30, "rating": 4.8, "link": "https://css-tricks.com/the-css-box-model/"}
        ],
        'Intermediate': [
            {"sub": "CSS Flexbox Layout Module", "title": "CSS-Tricks Complete Guide to Flexbox", "type": "Article", "duration": 45, "rating": 5.0, "link": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/"},
            {"sub": "CSS Grid Layout Systems", "title": "CSS-Tricks Complete Guide to Grid", "type": "Article", "duration": 50, "rating": 5.0, "link": "https://css-tricks.com/snippets/css/complete-guide-grid/"},
            {"sub": "Responsive Web Design and Media Queries", "title": "freeCodeCamp Responsive Web Design Curriculum", "type": "Textbook Chapter", "duration": 90, "rating": 4.9, "link": "https://www.freecodecamp.org/learn/2022/responsive-web-design/"},
            {"sub": "CSS Transitions, Transforms, and Animations", "title": "MDN Web Docs: CSS Animations Guide", "type": "Textbook Chapter", "duration": 60, "rating": 4.7, "link": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations"}
        ],
        'Advanced': [
            {"sub": "CSS Preprocessors (Sass/SCSS)", "title": "Sass Official Guide & Documentation", "type": "Textbook Chapter", "duration": 45, "rating": 4.8, "link": "https://sass-lang.com/guide"},
            {"sub": "Tailwind CSS and Utility-First Frameworks", "title": "Tailwind CSS Official Documentation", "type": "Textbook Chapter", "duration": 60, "rating": 4.9, "link": "https://tailwindcss.com/docs/installation"},
            {"sub": "Web Accessibility (WCAG Standards)", "title": "W3C Web Accessibility Guidelines Overview", "type": "Article", "duration": 40, "rating": 4.7, "link": "https://www.w3.org/WAI/standards-guidelines/wcag/"},
            {"sub": "Cross-Browser Compatibility and Performance", "title": "Google web.dev Performance Optimization Guide", "type": "Textbook Chapter", "duration": 60, "rating": 4.8, "link": "https://web.dev/learn/performance/"}
        ]
    }
}

# List of all available subjects
all_available_subjects = list(subtopic_mapping.keys()) + [
    'Compiler Design', 'Computer Networks', 'Database Management Systems', 
    'Java', 'JavaScript', 'Operating Systems', 'Software Engineering', 'Theory of Computation',
    'Constitutional Law', 'Corporate Tax', 'Cost Accounting', 'Criminal Law (IPC)', 
    'Financial Accounting', 'Financial Management', 'Genetic Engineering', 'Journalism and Mass Communication', 
    'Law of Contracts', 'Macroeconomics', 'Marketing Management', 'Organic Chemistry', 
    'Pharmaceutics', 'Political Science', 'Principles of Management', 'Quantum Physics', 
    'Structural Analysis', 'Thermodynamics and Heat Transfer'
]

learning_styles = ['Visual', 'Auditory', 'Reading/Writing', 'Kinesthetic']
difficulty_levels = ['Beginner', 'Intermediate', 'Advanced']

# Application Title & Description
st.title("Personalized Learning Recommendation System")
st.write("Select your preferences and subject to receive recommended sub-topics and best study documentation and tutorials.")

# Student Profile & Preferences Section
st.header("Student Preferences and Subject Search")

col1, col2, col3 = st.columns(3)

with col1:
    prior_gpa = st.number_input("CGPA (1.0 to 10.0):", min_value=1.0, max_value=10.0, value=8.0, step=0.1)

with col2:
    learning_style = st.selectbox("Preferred Learning Style:", learning_styles)

with col3:
    selected_difficulty = st.selectbox("Target Difficulty Level:", difficulty_levels)

st.markdown("---")

# Single Clean Subject Selection Box
st.subheader("Select Subject")
selected_topic = st.selectbox("Select Subject:", all_available_subjects)

# Recommendation Logic Function
def get_recommendations(focus_topic, style, diff_filter, top_n=4):
    if focus_topic in subtopic_mapping and diff_filter in subtopic_mapping[focus_topic]:
        items = subtopic_mapping[focus_topic][diff_filter]
    else:
        items = [
            {"sub": f"Core Concept 1 in {focus_topic}", "title": "Python Official Documentation & Tutorials", "type": "Textbook Chapter", "duration": 45, "rating": 4.7, "link": "https://docs.python.org/3/tutorial/index.html"},
            {"sub": f"Core Concept 2 in {focus_topic}", "title": "W3Schools Reference and Detailed Guides", "type": "Textbook Chapter", "duration": 60, "rating": 4.8, "link": "https://www.w3schools.com/"},
            {"sub": f"Practical Application of {focus_topic}", "title": "GeeksforGeeks Comprehensive Study Notes", "type": "Article", "duration": 75, "rating": 4.6, "link": "https://www.geeksforgeeks.org/"},
            {"sub": f"Advanced Reference in {focus_topic}", "title": "Python Developer Reference Manual", "type": "Textbook Chapter", "duration": 30, "rating": 4.9, "link": "https://docs.python.org/3/"}
        ]
    
    available = pd.DataFrame(items)
    
    scores = []
    for _, res in available.iterrows():
        score = 0.0
        rtype = res['type']
        if (style == 'Visual' and rtype in ['Video Lecture', 'Textbook Chapter']) or \
           (style == 'Reading/Writing' and rtype in ['Textbook Chapter', 'Article']) or \
           (style == 'Kinesthetic' and rtype == 'Article') or \
           (style == 'Auditory' and rtype == 'Video Lecture'):
            score += 2.0
            
        score += (res['rating'] / 5.0) * 1.0
        scores.append(score)
        
    available['match_score'] = scores
    return available.sort_values(by=['match_score', 'rating'], ascending=False).head(top_n)

# Generate Recommendations
recommendations = get_recommendations(selected_topic, learning_style, selected_difficulty, top_n=4)

st.markdown("---")

# Display Recommendations Table
st.header("Recommended Learning Modules")
st.dataframe(
    recommendations[['sub', 'type', 'duration', 'rating', 'match_score']],
    use_container_width=True,
    hide_index=True,
    column_config={
        "sub": "Specific Sub-Topic / Module",
        "type": "Format",
        "duration": "Duration (mins)",
        "rating": "Rating",
        "match_score": "Match Score"
    }
)

# Curated Study Resources & Direct Links Section
st.markdown("---")
st.header("Best Available Study Resources & Documentation")
st.write("Access recommended study materials, official documentation, and tutorial chapters to learn from below:")

for _, row in recommendations.iterrows():
    with st.container():
        st.subheader(f"Module: {row['sub']}")
        st.write(f"**Format:** {row['type']} | **Duration:** {row['duration']} mins | **Rating:** {row['rating']}/5.0")
        st.markdown(f"**Read & Learn Here:** [{row['title']}]({row['link']})")
        st.markdown("---")

