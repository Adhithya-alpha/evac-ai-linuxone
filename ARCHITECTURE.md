# 🏗️ Evac AI: System Architecture & Decision Flowchart
**Team Z-etta Bytes** | *IBM Z Datathon — Real-Time AI for Critical Decisions*

---

## 1. End-to-End System Architecture (`s390x`)

```mermaid
flowchart TB
    subgraph Inputs["1. Telemetry & Geospatial Ingestion"]
        A["Meteorological Sensors<br/>(Wind km/h, Rain mm/hr, Flood m)"]
        B["Topographical Profile<br/>(Origin Lat/Lon, MSL Elevation, Slope °)"]
        C["Operator Parameters<br/>(Disaster Preset & Target Language)"]
    end

    subgraph Mainframe["2. IBM LinuxONE (s390x) Compute Node"]
        D["Streamlit Command UI<br/>(Port 8501 + psutil Telemetry)"]
        E["FastAPI ASGI Engine<br/>(Uvicorn Worker - Port 8000)"]
        F["Deterministic Physics & Triage Core<br/>(Composite Risk Score 0-100)"]
        G["Topographic & Hydro Solver<br/>(Net Elevation Gain + Soil Saturation)"]
        H["Protocol & Multilingual Synthesizer<br/>(Tamil / Hindi / English + Sec 144)"]
    end

    subgraph Outputs["3. Actionable State Dispatch"]
        I["Machine-Readable JSON API<br/>(TN-SDMA Schema + .json Download)"]
        J["Geospatial Relief Vector Map<br/>(Origin to Safe Shelter Coordinates)"]
        K["Public Emergency SMS Broadcast<br/>(1070 Helpline + Uphill Routing)"]
    end

    A & B & C --> D
    D -- "HTTP POST /analyze-crisis" --> E
    E --> F
    F --> G
    G --> H
    H -- "JSON Payload" --> D
    D --> I & J & K
```

---

## 2. Solution Decision Flowchart (Physics & Triage Logic)

```mermaid
flowchart TD
    Start(["Ingest Live Telemetry Payload"]) --> Score["Calculate Composite Risk Score<br/>(0.35*Rain + 30.0*Flood + 0.25*Wind)"]
    
    Score --> SevCheck{"Risk Score Threshold"}
    SevCheck -- "Score >= 75" --> Crit["CRITICAL (RED ALERT)<br/>Enforce Section 144 Curfew"]
    SevCheck -- "45 <= Score < 75" --> High["HIGH (ORANGE ALERT)<br/>Enforce Section 144 Curfew"]
    SevCheck -- "Score < 45" --> Mod["MODERATE (YELLOW ALERT)<br/>Standard Advisory"]

    Crit & High & Mod --> ZoneCheck{"Evaluate Hazard Zone Topography"}
    
    ZoneCheck -- "Landslide (Western Ghats)" --> TopoL["Ascend +57.0m (485m to 542m MSL)<br/>32.5 deg Escarpment Lateritic Clay"]
    ZoneCheck -- "Cyclone (Chennai Coast)" --> TopoC["Ascend +14.3m (2.1m to 16.4m MSL)<br/>Coastal Alluvial Plain"]
    ZoneCheck -- "Flash Flood (Adyar Basin)" --> TopoF["Ascend +15.6m (6.4m to 22.0m MSL)<br/>Estuarine Floodplain"]

    TopoL & TopoC & TopoF --> WindCheck{"Evaluate Wind Speed (km/h)"}
    WindCheck -- ">= 120 km/h" --> W1["Beaufort 12 Lockdown:<br/>Tracked Military Carriers Only"]
    WindCheck -- "65 to 119 km/h" --> W2["Beaufort 8-11 Restriction:<br/>Ban 2-Wheelers & High-Profile Trucks"]
    WindCheck -- "< 65 km/h" --> W3["Beaufort 1-7 Clearance:<br/>TNSTC Bus Fleets & Drones Cleared"]

    W1 & W2 & W3 --> HydroCheck{"Evaluate Flood Depth (m)"}
    HydroCheck -- ">= 2.2m" --> H1["Catastrophic Submergence:<br/>NDRF Zodiac Boats & IAF Winch"]
    HydroCheck -- "0.7m to 2.1m" --> H2["Deep Hydrostatic Inundation:<br/>High-Clearance 4x4 Stallion Trucks"]
    HydroCheck -- "< 0.7m" --> H3["Surface Sheet Runoff:<br/>Elevated Arterial Highway Convoys"]

    H1 & H2 & H3 --> Dispatch(["Generate TN-SDMA JSON Directive & Multilingual SMS"])
```

---

## 3. Request / Response Sequence Flow

```mermaid
sequenceDiagram
    autonumber
    actor Operator as Emergency Operator
    participant UI as Streamlit Dashboard (8501)
    participant API as FastAPI Engine (8000)
    participant S390X as IBM LinuxONE (s390x Kernel)

    Operator->>UI: Adjusts Wind, Rain, Flood Sliders & Clicks Execute
    UI->>S390X: Queries psutil CPU, RAM & s390x Architecture
    UI->>API: POST /analyze-crisis (TelemetryInput JSON)
    API->>API: Computes Topographic Elevation Gain & Soil Saturation
    API->>API: Selects Wind & Hydro-Extraction Tactical Options
    API->>API: Formats Tamil/Hindi/English SMS & JSON Schema
    API-->>UI: Returns 200 OK (json_directive + latency_ms)
    UI-->>Operator: Renders Interactive JSON Tree, Map Vector & .json Download
```
