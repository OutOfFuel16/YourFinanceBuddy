# YourFinanceBuddy

YourFinanceBuddy is an AI-powered financial assistant that provides budget summaries based on user queries. It leverages AI agents to process queries, retrieve relevant financial data, and generate insights.

## Features

- Uses FetchAI uAgents framework to handle agent communication.
- Integrates with Groq for AI-powered financial assistance.
- Implements Pathway dynamic vector store for efficient similarity-based search.
- Provides real-time budget insights, summaries, and tips based on user queries.

## Technologies Used

- Python
- Pathway Vectorstore
- Anvil-Uplink
- uAgents
- Groq

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Anvil Uplink
- Environment variables for `GROQ_API_KEY` and `ANVIL_SERVER`

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd budget-assistant
   ```

2. Set up environment variables:

   ```sh
   export GROQ_API_KEY="your-api-key"
   export ANVIL_SERVER="your-anvil-server"
   ```

## Usage

Run the application with the following command:

```sh
python main.ipynb
```

## File Structure

```
YourFinanceBuddy/
├── main.ipynb                 # Jupyter Notebook with main logic
├── README.md                  # Documentation
├── budget_breakdown.py         # Budget Breakdown Agent
```

## Contribution

Feel free to submit issues or pull requests to improve the project.

## License

This project is open-source and available under the MIT License.
