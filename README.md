# 🚨 Evac AI: Anticipatory Disaster Response Platform on IBM LinuxONE (s390x)
**Team Z-etta Bytes** | *IBM Z Datathon — Real-Time AI for Critical Decisions*

## Overview
Evac AI is a deterministic geospatial triage, topographic routing, and multilingual emergency broadcast engine running natively on **IBM Z / LinuxONE (`s390x`)**.

### Key Capabilities
- **Topographical & Geological Physics:** Computes net elevation gain above Mean Sea Level (MSL), slope gradient stability, and soil saturation thresholds.
- **Dynamic Telemetry Protocols:** Adapts evacuation logistics in real time based on wind velocity (Beaufort scale) and hydrostatic inundation depth.
- **Machine-Readable JSON API & Multilingual SMS:** Outputs structured government directives (`.json`) alongside localized Tamil, Hindi, and English public safety broadcasts.

## Quick Start on IBM LinuxONE (`s390x`)
```bash
conda activate evac_ai_env
uvicorn backend:app --host 127.0.0.1 --port 8000 &
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
