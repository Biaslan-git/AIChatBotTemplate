FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv
    # uv pip install --no-cache-dir -e .

COPY . .

ENV PYTHONPATH=/app

CMD ["uv", "run", "src/main.py"]
