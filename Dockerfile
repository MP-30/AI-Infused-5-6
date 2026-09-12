# 1. Base image = rent a ready-made kitchen (from Docker Hub)
FROM python:3.14-slim

# Grab the uv binary itself (Astral ships it as a tiny standalone image)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 2. Set up your counter inside that kitchen
WORKDIR /app

# 3. Copy ONLY the shopping list first (caching trick — explained below)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# 4. NOW copy the rest of your code
COPY . .
RUN uv sync --frozen --no-dev

# Put the venv's bin folder on PATH so plain commands (uvicorn, python) find it
ENV PATH="/app/.venv/bin:$PATH"

## 5. Train the model INSIDE the image (baked in at build time)
#RUN python train.py
#
# 6. Declare which window the food comes out of (documentation)
EXPOSE 8000

# 7. What runs the moment the tiffin is opened
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]