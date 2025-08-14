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
	git clone https://github.com/Sujan122321/AI_Job_Recommender_system_with_MCP.git
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
	```powershell
	pip install -r requirements.txt
	```
4. Run the application:
	```powershell
	python app.py
	```

### Project Structure
- `app.py`: Main application entry point
- `mcp_server.py`: MCP server implementation
- `src/`: Source code including helpers and job API integration

### License
This project is licensed under the MIT License.
