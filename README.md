# poc-chainlit
## How to run?

1. Create a virtual environment

```bash
python -m venv env
```

2. Activate the environment

```bash
env\Scripts\activate

```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Add your OPENAI_API_KEY to the .env file
Create a .env file in the root directory and add the following line

```bash
OPENAI_API_KEY=your_api_key
```

5. Start the app
```bash
chainlit run app.py -w
```