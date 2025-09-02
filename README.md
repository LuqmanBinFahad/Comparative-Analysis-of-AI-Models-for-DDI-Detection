# Drug-Drug Interaction (DDI) Detection Tool
# Dr. Luqman Bin Fahad

## Overview
The Drug-Drug Interaction (DDI) Detection Tool is an interactive web application designed to analyze and compare various AI models for predicting drug-drug interactions. This tool provides insights into model performance, visualizations of sample interactions, and cold-start scenario analysis.

## Features
- **Interactive Model Comparison Dashboard**: Compare performance metrics of different AI models (Traditional ML, GNNs, Transformers).
- **Cold-Start Scenario Analysis**: Evaluate how models perform on completely new drugs.
- **Sample Drug Interaction Visualization**: View examples of known drug interactions and their severity levels.
- **User-Friendly Walkthrough Guide**: A guided introduction to help new users navigate the application.

## Installation
To run this application locally, ensure you have Python installed, then follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/LuqmanBinFahad/DDI-detection-tool.git
   cd ddi-detection-tool
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
- Launch the application by running the command above.
- Use the sidebar controls to filter models and select performance metrics.
- Explore different tabs for model comparisons, sample interactions, cold-start analysis, and insights.

## Contributing
Feel free to submit issues or pull requests to improve this tool. Your contributions are welcome!

## License
This project is licensed under the MIT License.

## Acknowledgments
This tool is developed based on research methodologies for predicting drug-drug interactions using AI models.

```