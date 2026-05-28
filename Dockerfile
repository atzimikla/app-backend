FROM python:3.12-slim

# Crear usuario no-root para correr la app (CIS-DI-0001).
RUN useradd --create-home --uid 1001 appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

USER appuser

EXPOSE 8080

# Healthcheck contra el endpoint /health expuesto por la app (CIS-DI-0006).
# Usamos urllib (Python stdlib) para no agregar curl/wget al image.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/health').read()" || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
