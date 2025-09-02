import pandas as pd
import streamlit as st

def display_model_insights(df):
    """Display key insights about model performance"""
    
    best_auc = df.loc[df['AUC_ROC'].idxmax()]
    best_f1 = df.loc[df['F1_Score'].idxmax()]
    
    st.subheader("🔍 Key Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            label="Best Overall Model (AUC-ROC)",
            value=best_auc['Model'],
            delta=f"AUC: {best_auc['AUC_ROC']:.3f}"
        )
        st.caption(f"Type: {best_auc['Model_Type']}")
    
    with col2:
        st.metric(
            label="Best Balanced Model (F1-Score)",
            value=best_f1['Model'],
            delta=f"F1: {best_f1['F1_Score']:.3f}"
        )
        st.caption(f"Type: {best_f1['Model_Type']}")
    
    # Performance by model type
    st.subheader("📊 Performance by Model Type")
    type_stats = df.groupby('Model_Type').agg({
        'AUC_ROC': 'mean',
        'F1_Score': 'mean',
        'Precision': 'mean',
        'Recall': 'mean'
    }).round(3)
    
    st.dataframe(type_stats.style.highlight_max(axis=0))

def display_model_recommendations():
    """Display model recommendations based on research"""
    
    st.subheader("🎯 Model Recommendations")
    
    recommendations = [
        {
            "Use Case": "General DDI Prediction",
            "Recommended": "Transformer Models",
            "Reason": "Superior multimodal data integration and interpretability",
            "Expected AUC": "0.95-0.98"
        },
        {
            "Use Case": "Network-based Prediction",
            "Recommended": "GNN (GAT)",
            "Reason": "Excellent for leveraging drug interaction graphs",
            "Expected AUC": "0.92-0.96"
        },
        {
            "Use Case": "Resource-constrained",
            "Recommended": "XGBoost",
            "Reason": "Good performance with lower computational cost",
            "Expected AUC": "0.85-0.90"
        },
        {
            "Use Case": "Cold-start Scenarios",
            "Recommended": "Transformer + Pre-training",
            "Reason": "Best generalization to novel drugs",
            "Expected AUC": "0.85-0.90"
        }
    ]
    
    rec_df = pd.DataFrame(recommendations)
    st.dataframe(rec_df, hide_index=True)

def display_limitations():
    """Display limitations and challenges"""
    
    st.subheader("⚠️ Limitations & Challenges")
    
    limitations = [
        "Data Quality: Models depend on incomplete DDI databases",
        "Cold-start Problem: Predicting interactions for completely new drugs remains challenging",
        "Validation: In silico predictions require clinical validation",
        "Computational Cost: Transformers are resource-intensive to train",
        "Interpretability: Despite attention mechanisms, some black-box nature remains"
    ]
    
    for limitation in limitations:
        st.write(f"• {limitation}")