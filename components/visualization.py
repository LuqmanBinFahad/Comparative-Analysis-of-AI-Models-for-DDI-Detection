import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def create_model_comparison_chart(df, metric='AUC_ROC'):
    """Create bar chart comparing model performance by metric"""
    fig = px.bar(df, 
                 x='Model', 
                 y=metric,
                 color='Model_Type',
                 title=f'Model Comparison - {metric}',
                 labels={metric: metric, 'Model': 'AI Model'},
                 hover_data=['Precision', 'Recall', 'F1_Score'])
    
    fig.update_layout(
        xaxis_tickangle=-45,
        height=500,
        showlegend=True
    )
    return fig

def create_radar_chart(df):
    """Create radar chart for comprehensive model comparison"""
    metrics = ['AUC_ROC', 'F1_Score', 'Precision', 'Recall']
    
    fig = go.Figure()
    
    for _, row in df.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=[row[metric] for metric in metrics],
            theta=metrics,
            fill='toself',
            name=row['Model']
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0.7, 1.0]
            )),
        showlegend=True,
        title='Comprehensive Model Performance Radar Chart'
    )
    
    return fig

def create_cold_start_comparison(df):
    """Create comparison chart for cold-start scenarios"""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # AUC-ROC on primary y-axis
    fig.add_trace(
        go.Bar(x=df['Scenario'], y=df['AUC_ROC'], name='AUC-ROC', marker_color='blue'),
        secondary_y=False,
    )
    
    # Success Rate on secondary y-axis
    fig.add_trace(
        go.Scatter(x=df['Scenario'], y=df['Success_Rate'], name='Success Rate (%)', mode='lines+markers', line=dict(color='red')),
        secondary_y=True,
    )
    
    fig.update_layout(
        title_text='Cold-Start Scenario Performance',
        xaxis_title='Model Type',
        height=400
    )
    
    fig.update_yaxes(title_text="AUC-ROC", secondary_y=False)
    fig.update_yaxes(title_text="Success Rate (%)", secondary_y=True)
    
    return fig

def create_interaction_severity_chart(df):
    """Create chart showing interaction severity distribution"""
    severity_counts = df['Severity'].value_counts()
    fig = px.pie(values=severity_counts.values, 
                 names=severity_counts.index,
                 title='Drug Interaction Severity Distribution',
                 hole=0.3)
    return fig