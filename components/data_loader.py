import pandas as pd
from sample_data import generate_sample_data

def load_model_performance_data():
    """Load model performance metrics"""
    data = generate_sample_data()
    return data['models_df']

def load_drug_interactions():
    """Load sample drug interaction data"""
    data = generate_sample_data()
    return data['interactions_df']

def load_cold_start_data():
    """Load cold-start scenario data"""
    data = generate_sample_data()
    return data['cold_start_df']

def get_model_types():
    """Get unique model types for filtering"""
    df = load_model_performance_data()
    return df['Model_Type'].unique().tolist()

def filter_models_by_type(model_type):
    """Filter models by type"""
    df = load_model_performance_data()
    if model_type == 'All':
        return df
    return df[df['Model_Type'] == model_type]