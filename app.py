from flask import Flask, jsonify, request

app = Flask(__name__)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_palindrome(word: str) -> bool:
    normalized = "".join(c.lower() for c in word if c.isalnum())
    return bool(normalized) and normalized == normalized[::-1]


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/is-prime")
def check_prime():
    raw = request.args.get("n")
    if raw is None:
        return jsonify(error="missing query param 'n'"), 400
    try:
        n = int(raw)
    except ValueError:
        return jsonify(error=f"'{raw}' is not a valid integer"), 400
    return jsonify(n=n, is_prime=is_prime(n))


@app.get("/is-palindrome")
def check_palindrome():
    raw = request.args.get("word")
    if raw is None:
        return jsonify(error="missing query param 'word'"), 400
    if not raw.strip():
        return jsonify(error="'word' must not be empty"), 400
    return jsonify(word=raw, is_palindrome=is_palindrome(raw))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
