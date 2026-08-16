# Resume Parser

`resume-parser` is a notebook-first prototype for parsing PDF resumes and comparing them against a target job description with the Groq API. It extracts structured data from both the job posting and each candidate resume, then produces a score and short fit summary for every resume in the `resumes/` folder.

## What It Does

The workflow in [resume_parser.ipynb](/C:/Users/Dhruv/OneDrive/Desktop/ai/resume-parser/resume_parser.ipynb) is:

1. Define a job description in plain text.
2. Ask the model to convert that posting into a structured `Job_D` object.
3. Read PDF resumes from the `resumes/` directory.
4. Extract resume text with `pypdf`.
5. Ask the model to normalize each resume into a structured `Resume` object.
6. Compare the job and resume objects to generate a `MatchResult` with a score from `0` to `100`.

## Tech Stack

- Python 3.12+
- [Groq Python SDK](https://github.com/groq/groq-python)
- `pypdf` for PDF text extraction
- `pydantic` for schema validation
- `python-dotenv` for environment variable loading

## Project Structure

```text
.
|- resume_parser.ipynb   # Primary workflow: parse, score, and inspect resumes
|- resumes/              # Sample PDF resumes to evaluate
|- main.py               # Placeholder script; the notebook is the real entry point today
|- pyproject.toml        # Project metadata and dependencies
|- uv.lock               # Locked dependency graph for uv
```

## Requirements

- Python `3.12` or newer
- A Groq API key exposed as `GROQ_API_KEY`
- PDF resumes with extractable text

## Installation

### Using `uv`

```bash
uv sync
```

Copy `.env.example` to `.env`:

```powershell
Copy-Item .env.example .env
```

Then add your API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

If you want to run the notebook outside an IDE with built-in notebook support, you can launch Jupyter ad hoc with:

```bash
uv run --with jupyter jupyter lab
```

### Using `pip`

```bash
python -m venv .venv
source .venv/bin/activate
pip install groq python-dotenv pydantic pypdf
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## How To Use

1. Place one or more PDF resumes in the `resumes/` directory.
2. Open [resume_parser.ipynb](/C:/Users/Dhruv/OneDrive/Desktop/ai/resume-parser/resume_parser.ipynb).
3. Update the `job_description` cell with the role you want to screen for.
4. Run the notebook cells from top to bottom.
5. Review the final printed `results` list.

Each result looks like:

```python
{
    "name": "Candidate Name",
    "score": 78.0,
    "details": {...}
}
```

## How The Scoring Works

The notebook uses the LLM three times:

- Once to convert the job post into structured JSON.
- Once per resume to extract normalized candidate data.
- Once per resume to judge fit and assign a final score.

Pydantic models act as guardrails so the notebook can validate the JSON returned by the model before moving to the next step.

## Notes And Limitations

- This project is currently notebook-driven; `main.py` is only a placeholder.
- Resume quality depends heavily on whether the source PDF contains clean extractable text.
- LLM scoring is useful for screening and prioritization, but it should not be treated as a final hiring decision.
- The notebook includes `time.sleep(5)` pauses between API calls, which may help reduce bursty requests during batch processing.

## Future Improvements

- Export ranked results to CSV or JSON.
- Add stronger error handling for malformed PDFs and API failures.
- Support multiple job descriptions without editing notebook cells.
- Turn the notebook workflow into a reusable CLI or web app.
