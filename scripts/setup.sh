#!/bin/bash
# Setup script for ML Zoomcamp project
uv venv --python 3.12
source .venv/bin/activate
uv pip install -r requirements.txt
python -m ipykernel install --user --name=ml-zoomcamp
echo "✅ ML Zoomcamp environment setup complete!"
