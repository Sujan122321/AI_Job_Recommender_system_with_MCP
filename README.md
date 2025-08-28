# AI_Job_Recommender_system_with_MCP
## Readme

Welcome to the AI Job Recommender System with MCP!

This project leverages artificial intelligence to recommend jobs to users based on their profiles, preferences, and market trends. It utilizes the Model Context Protocol (MCP) for efficient data handling and integration.

### Features
- Intelligent job recommendations
- User profile management
- Integration with job APIs
- Scalable architecture using MCP

### Getting Started
1. Clone the repository:
	```powershell
	git clone https://github.com/Sujan122321/AI_Job_Recommender_system_with_MCP
	```
2. Create and activate a virtual environment (recommended):
	You can use either Python's built-in venv or [uv](https://github.com/astral-sh/uv) for faster environment creation.

	**Using Python venv:**
	```powershell
	python -m venv venv
	.\venv\Scripts\Activate.ps1
	```

	**Using uv:**
	```powershell
	uv venv venv
	.\venv\Scripts\Activate.ps1
	```
3. Install dependencies:
	You can use either pip or uv:

	**Using pip:**
	```powershell
	pip install -r requirements.txt
	```

	**Using uv:**
	```powershell
	uv pip install -r requirements.txt
	```

4. Run the application:
	You can use either python or uv:

	**Using python:**
	```powershell
	python app.py
	```

	**Using uv:**
	```powershell
	uv run app.py
	```

### Project Structure
- `app.py`: Main application entry point
- `src/`: Source code including helpers and job API integration

### License
This project is licensed under the MIT License.\

### Used Resources
-  Gemini LLM 
- Apify for the job scraping from the linkedin and nakuri
