FROM agrigorev/zoomcamp-model:2025

# Copy uv binary
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory (already /code in base image)
WORKDIR /code

# Add venv to PATH
ENV PATH="/code/.venv/bin:$PATH"

# Copy dependency files
COPY pyproject.toml uv.lock .python-version ./

# Install dependencies
RUN uv sync --locked

# Copy application code
COPY app_docker.py ./app.py

# Expose port
EXPOSE 9696

# Run the application
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9696"]