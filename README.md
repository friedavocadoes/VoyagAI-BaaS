ml:

```bash
# create a virtual environment
python -m venv venv
# activate the virtual environment
venv\Scripts\activate # Windows
# Install dependencies
pip install -r requirements.txt
#run the app (/app)
uvicorn app.main:app --reload
```

to test, send `post` api requests to `http://127.0.0.1:8000/recommend/`
sample json data:

```json
{
  "sentiment": "happy",
  "location": "here",
  "budget": "20000"
}
```
