# TikTok Algorithms (X-Gorgon, X-Khronos, XLOG 02, TTEncrypt 05)

These are just few of TikTok algorithms that is used by the mobile application. It might be useful for your next TikTok project.

## Contains?
- X-Gorgon and X-Khronos v0404
- XLOG 02 encrypt/decrypt
- TTEncrypt (also often called Device Register/Applog) encrypt/decrypt
- Captcha Solver

## Requirements
- Check `requirements.txt`

## How to use?
- `pip install -r requirements.txt`
- `uvicorn main:app --reload --host 0.0.0.0 --port 8100`
- You now have FastAPI rest client on port 8100 (http://127.0.0.1:8100)

See `main.py` file and see usage example of each algorithm classes.

## Want to contribute?

Sure, make a pull request.

## Disclaimer

Won't be responsible if use this for other purposes than educational. 

Again, **USE THIS FOR EDUCATIONAL PURPOSES ONLY**
