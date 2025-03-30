import subprocess
import sys

# List of required packages
required_packages = ["uagents", "groq"]

# Install missing packages
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        print(f"Installing missing package: {package}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


import os
import subprocess
from groq import Groq
from uagents import Agent, Context

# Create an agent named Alice
alice = Agent(name="alice", seed="YOUR NEW PHRASE", port=8000, endpoint="http://localhost:8000/submit")
context = """19-March-2025, Clothing, 3500
15-March-2025, Travel, 3000
06-March-2025, Dining Out, 900"""

# Initialize Groq API client
client = Groq(api_key="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")

# Global variable to store the response
budget_summary_response = None  

# Define a periodic task for Alice
@alice.on_interval(period=100.0)
async def fetch_budget_summary(ctx: Context):
    global budget_summary_response  # Access the global variable

    query = "Give a detailed description of my budget expenses in the month of March."
    context_data = context

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a financial assistant providing detailed budget summaries based on user data."},
            {"role": "user", "content": f"Here is the context and the query which is to be answered using the context:\n{context_data}\n\nNow, {query}"},
        ],
        model="llama-3.3-70b-versatile",
    )

    budget_summary_response = chat_completion.choices[0].message.content  # Store response in variable

    # Write response to file
    with open("budget_summary.txt", "w", encoding="utf-8") as f:
        f.write(budget_summary_response)

    ctx.logger.info(f"Generated Budget Summary:\n{budget_summary_response}")

    if os.path.getsize("budget_summary.txt") > 0:
        ctx.logger.info("Budget summary file is populated. Terminating script...")
        subprocess.Popen(["taskkill", "/F", "/PID", str(os.getpid())], shell=True)

# Run the agent
if __name__ == "__main__":
    alice.run()
