from flask import Flask, render_template,request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
import plotly.express as px
import dash_core_components as dcc
from dash import Dash
import dash_html_components as html


app = Flask(__name__)
# Initialize Dash app within Flask
dash_app = Dash(__name__, server=app, url_base_pathname='/dash/')

# Load your cleaned dataset (replace 'cleaned_indian_food.csv' with the actual file path)
df = pd.read_csv('indian_food.csv')

num_rows_to_display=20

@app.route('/')
def index():
    return render_template('front.html')

@app.route('/course_chart', methods=['GET', 'POST'])
def course_chart():
    course_counts = df['course'].value_counts()
    plt.figure(figsize=(8, 6))
    course_counts.plot(kind='bar')
    plt.title('Distribution of Courses')
    plt.xlabel('Course')
    plt.ylabel('Count')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('course_chart.html', plot_url=plot_url)

@app.route('/flavor_chart', methods=['GET', 'POST'])
def flavor_chart():
    flavor_counts = df['flavor_profile'].value_counts()
    plt.figure(figsize=(8, 6))
    flavor_counts.plot(kind='bar')
    plt.title('Distribution of Flavor Profiles')
    plt.xlabel('Flavor Profile')
    plt.ylabel('Count')

    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return render_template('flavor_chart.html', plot_url=plot_url)

@app.route('/scatter', methods=['GET', 'POST'])
def scatter_plot():
    # Create a scatter plot for prep_time vs. cook_time
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='prep_time', y='cook_time', hue='region')
    plt.title('Preparation Time vs. Cooking Time')
    plt.xlabel('Preparation Time')
    plt.ylabel('Cooking Time')

    # Save the scatter plot as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.read()).decode()

    return render_template('scatter.html', plot_url=plot_url)


@app.route('/piechart',methods=['GET', 'POST'])
def pie_chart():
    # Create a pie chart for the distribution of dishes by "course"
    course_counts = df['course'].value_counts()

    plt.figure(figsize=(8, 6))
    plt.pie(course_counts, labels=course_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Dishes by Course')

    # Save the pie chart as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.read()).decode()

    return render_template('piechart.html', plot_url=plot_url)


@app.route('/linechart',  methods=['GET', 'POST'])
def line_chart():
    # Create a line chart for the relationship between "prep_time" and "cook_time"
    plt.figure(figsize=(8, 6))
    plt.plot(df['prep_time'], df['cook_time'])
    plt.title('Relationship Between Preparation Time and Cooking Time')
    plt.xlabel('Preparation Time')
    plt.ylabel('Cooking Time')

    # Save the line chart as an image
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.read()).decode()

    return render_template('linechart.html', plot_url=plot_url)


@app.route('/about', methods=['GET', 'POST'])
def abouthello():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process the form data (e.g., save to database, send email)
        # Add your code here
        
        # Redirect to a thank you page
        return "Thank You!"
    
    return render_template('contact.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/front', methods=['GET', 'POST'])
def front():
    return render_template('front.html')






    

scenes = [
    {
        'title': 'Scene 1: Introduction',
        'content': 'This report presents the findings and insights derived from an in-depth Exploratory Data Analysis (EDA) on a comprehensive dataset of Indian food. The aim of this analysis is to explore the diverse flavors, regional variations, popular dishes, and nutritional aspects of Indian cuisine. By employing EDA techniques, we unravel the complexities of Indian food, shedding light on its cultural significance, culinary traditions, and the impact of regional diversity.',
    },
    {
        'title': 'Scene 2: Descriptive Statistics',
        'content': 'Descriptive statistics for the Indian food dataset:',
        'data': df.head(num_rows_to_display).to_dict('records'),  # Pass the dataset to Scene 2
    },
    {
        'title': 'Scene 3: Ingredient Analysis',
        'content': 'Analyzing the most commonly used ingredients in Indian cuisine:',
       'data': df.head(num_rows_to_display).to_dict('records'), # Pass the dataset to Scene 3
    },
    # Add more scenes as needed
]

@app.route('/report')
def indexreport():
    return render_template('report.html', scenes=scenes)







if __name__ == '__main__':
    app.run(debug=True)
