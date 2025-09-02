import pandas as pd
import numpy as np

# Sample drug interaction data based on research document
def generate_sample_data():
    # Model performance metrics
    models_data = {
        'Model': ['Random Forest', 'SVM', 'XGBoost', 'GCN', 'GAT', 'GraphSAGE', 'ChemBERTa', 'Custom Transformer'],
        'AUC_ROC': [0.87, 0.85, 0.89, 0.93, 0.95, 0.94, 0.96, 0.97],
        'F1_Score': [0.82, 0.80, 0.84, 0.88, 0.90, 0.89, 0.91, 0.92],
        'Precision': [0.85, 0.83, 0.87, 0.90, 0.92, 0.91, 0.93, 0.94],
        'Recall': [0.80, 0.78, 0.82, 0.86, 0.88, 0.87, 0.89, 0.90],
        'Model_Type': ['Traditional', 'Traditional', 'Traditional', 'GNN', 'GNN', 'GNN', 'Transformer', 'Transformer']
    }
    
    # Sample drug interaction pairs
    drug_interactions = [
        {'Drug_A': 'Warfarin', 'Drug_B': 'Aspirin', 'Interaction_Type': 'Increased bleeding risk', 'Severity': 'High'},
        {'Drug_A': 'Simvastatin', 'Drug_B': 'Clarithromycin', 'Interaction_Type': 'Increased myopathy risk', 'Severity': 'High'},
        {'Drug_A': 'Digoxin', 'Drug_B': 'Quinidine', 'Interaction_Type': 'Increased digoxin levels', 'Severity': 'Moderate'},
        {'Drug_A': 'Metformin', 'Drug_B': 'Cimetidine', 'Interaction_Type': 'Increased metformin levels', 'Severity': 'Low'},
        {'Drug_A': 'Sertraline', 'Drug_B': 'Tramadol', 'Interaction_Type': 'Serotonin syndrome risk', 'Severity': 'Moderate'}
    ]
    
    # Cold-start scenario data
    cold_start_data = {
        'Scenario': ['Traditional ML', 'GNN', 'Transformer'],
        'AUC_ROC': [0.75, 0.85, 0.90],
        'Success_Rate': [60, 78, 85]
    }
    
    return {
        'models_df': pd.DataFrame(models_data),
        'interactions_df': pd.DataFrame(drug_interactions),
        'cold_start_df': pd.DataFrame(cold_start_data)
    }