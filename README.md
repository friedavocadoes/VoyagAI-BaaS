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
