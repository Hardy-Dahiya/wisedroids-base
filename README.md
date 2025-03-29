# WiseDroidAI Agent Template

This template provides a foundation for creating custom AI agents using WiseDroidAI. It includes all necessary boilerplate code and structure for building and deploying your agent.

## Structure

```
wisedroid-agent-template/
├── app/
│   ├── agent/         # Agent-specific code
│   ├── api/           # API routes
│   └── config/        # Configuration
├── tests/             # Test files
├── .env.example       # Environment variables template
└── requirements.txt   # Python dependencies
```

## Setup

1. Clone this repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your values
5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Development

The main agent logic should be implemented in `app/agent/base.py`. WiseDroidAI will generate and insert the necessary code in this file.

## Testing

Run tests using pytest:
```bash
pytest
```

## Deployment

This template is ready to be deployed to platforms like Render.com. Make sure to set up your environment variables in your deployment platform.