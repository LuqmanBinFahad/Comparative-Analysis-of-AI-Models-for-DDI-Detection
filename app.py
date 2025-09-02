import streamlit as st
import pandas as pd
from components.data_loader import load_model_performance_data, load_drug_interactions, load_cold_start_data, get_model_types, filter_models_by_type
from components.visualization import create_model_comparison_chart, create_radar_chart, create_cold_start_comparison, create_interaction_severity_chart
from components.model_comparison import display_model_insights, display_model_recommendations, display_limitations

# Page configuration
st.set_page_config(
    page_title="DDI Detection Tool",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #2E86AB;
    }
    .walkthrough-card {
        background-color: #f0f8ff;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4B9CD3;
        margin-bottom: 1rem;
    }
    .feature-title {
        font-weight: bold;
        color: #2E86AB;
    }
    .section-header {
        background-color: rgba(46, 134, 171, 0.1);
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

def show_walkthrough():
    """Display walkthrough guide for new users"""
    st.markdown('<div class="walkthrough-card">', unsafe_allow_html=True)
    st.markdown("# 🚶‍♂️ DDI Detection Tool - Walkthrough Guide")
    st.markdown("""
    Welcome to the Drug-Drug Interaction (DDI) Detection Tool! This guide will help you navigate through the application's features.
    
    ## How to Use This Tool
    
    This interactive dashboard demonstrates the comparative analysis of different AI models for drug-drug interaction prediction.
    Let's walk through the main features:
    """)
    
    st.markdown('<div class="section-header">', unsafe_allow_html=True)
    st.markdown("### 🎮 Control Panel (Sidebar)")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""
    - **Filter by Model Type**: Select from Traditional ML, GNNs, or Transformers to focus on specific model categories
    - **Performance Metric**: Choose which metric to visualize (AUC-ROC, F1-Score, Precision, Recall)
    
    **Example**: Select "GNN" to focus only on Graph Neural Network models and their performance.
    """)
    
    st.markdown('<div class="section-header">', unsafe_allow_html=True)
    st.markdown("### 📊 Model Comparison Tab")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""
    - Compare different AI models on key performance metrics
    - View the radar chart for multi-metric comparison
    - Check detailed metrics table
    
    **Example**: The radar chart shows that Transformer models generally outperform traditional models on all metrics.
    """)
    
    st.markdown('<div class="section-header">', unsafe_allow_html=True)
    st.markdown("### 💊 Sample Interactions Tab")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""
    - View examples of known drug-drug interactions
    - Explore the distribution of interaction severity levels
    
    **Example**: Warfarin and Aspirin have a high-severity interaction with increased bleeding risk.
    """)
    
    st.markdown('<div class="section-header">', unsafe_allow_html=True)
    st.markdown("### ❄️ Cold-Start Analysis Tab")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""
    - Understand how models perform on completely new drugs
    - Compare success rates across model categories
    
    **Example**: Traditional ML models show significant performance drop (60% success rate) in cold-start scenarios,
    while Transformers maintain 85% success rate.
    """)
    
    st.markdown('<div class="section-header">', unsafe_allow_html=True)
    st.markdown("### 📋 Insights & Recommendations Tab")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""
    - Review key insights about model performance
    - See specific model recommendations for different use cases
    - Understand limitations of the current approaches
    
    **Example**: Transformer models are recommended for general DDI prediction with expected AUC of 0.95-0.98.
    """)
    
    st.markdown("""
    ## 🎯 Quick Tips
    
    1. Start with the Model Comparison tab to get an overview
    2. Use the sidebar to filter models based on your interest
    3. Check the Cold-Start Analysis tab to understand generalization capabilities
    4. Review the Insights tab for practical recommendations
    """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write("")
    with col2:
        if st.button("Continue to Dashboard →", type="primary"):
            st.session_state.show_walkthrough = False
            st.rerun()

def main():
    # Initialize session state for walkthrough
    if 'show_walkthrough' not in st.session_state:
        st.session_state.show_walkthrough = True
    
    # Show walkthrough if it's the first visit
    if st.session_state.show_walkthrough:
        show_walkthrough()
        return
    
    # Header
    st.markdown('<h1 class="main-header">💊 Drug-Drug Interaction Detection Tool</h1>', unsafe_allow_html=True)
    st.markdown("""
    **Comparative Analysis of AI Models for DDI Prediction**
    
    This interactive tool demonstrates the performance comparison of various AI models in predicting drug-drug interactions,
    based on the research methodology outlined in the provided document.
    """)
    
    # Add button to show walkthrough again
    if st.button("Show Walkthrough Guide"):
        st.session_state.show_walkthrough = True
        st.rerun()
    
    # Load data
    models_df = load_model_performance_data()
    interactions_df = load_drug_interactions()
    cold_start_df = load_cold_start_data()
    model_types = get_model_types()
    
    # Sidebar
    st.sidebar.title("🔧 Controls")
    selected_model_type = st.sidebar.selectbox("Filter by Model Type", ["All"] + model_types)
    selected_metric = st.sidebar.selectbox("Performance Metric", ["AUC_ROC", "F1_Score", "Precision", "Recall"])
    
    # Filter data
    filtered_df = filter_models_by_type(selected_model_type)
    
    # Main content tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Model Comparison", 
        "💊 Sample Interactions", 
        "❄️ Cold-Start Analysis",
        "📋 Insights & Recommendations"
    ])
    
    with tab1:
        st.header("AI Model Performance Comparison")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Performance metrics chart
            fig = create_model_comparison_chart(filtered_df, selected_metric)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.metric("Total Models", len(filtered_df))
            st.metric("Best AUC-ROC", f"{filtered_df['AUC_ROC'].max():.3f}")
            st.metric("Best F1-Score", f"{filtered_df['F1_Score'].max():.3f}")
        
        # Radar chart
        st.subheader("Comprehensive Performance Overview")
        radar_fig = create_radar_chart(filtered_df)
        st.plotly_chart(radar_fig, use_container_width=True)
        
        # Data table
        st.subheader("Performance Metrics Table")
        st.dataframe(filtered_df.style.highlight_max(axis=0, color='lightgreen'), use_container_width=True)
    
    with tab2:
        st.header("Sample Drug Interaction Data")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Interaction Examples")
            st.dataframe(interactions_df, use_container_width=True)
        
        with col2:
            st.subheader("Severity Distribution")
            severity_fig = create_interaction_severity_chart(interactions_df)
            st.plotly_chart(severity_fig, use_container_width=True)
        
        st.info("""
        💡 **Note**: This is sample data demonstrating the types of interactions that AI models are trained to predict.
        Real-world applications would use comprehensive databases like DrugBank and TWOSIDES.
        """)
    
    with tab3:
        st.header("Cold-Start Scenario Analysis")
        st.markdown("""
        **Cold-start scenario** tests model performance on completely new drugs not seen during training.
        This is the ultimate challenge in DDI prediction.
        """)
        
        fig = create_cold_start_comparison(cold_start_df)
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(cold_start_df.style.highlight_max(axis=0, color='lightgreen'), use_container_width=True)
        
        st.warning("""
        ⚠️ **Challenge**: Traditional models struggle with cold-start scenarios due to reliance on hand-engineered features.
        Modern architectures (GNNs, Transformers) show better generalization capabilities.
        """)
    
    with tab4:
        display_model_insights(filtered_df)
        st.divider()
        display_model_recommendations()
        st.divider()
        display_limitations()
    
    # Footer
    st.divider()
    st.caption("""
    **Research-Based Implementation**: This tool is based on the comparative analysis methodology described in the research document.
    Performance metrics are simulated based on expected outcomes from the study.
    """)

if __name__ == "__main__":
    main()