import streamlit as st
import requests
import pandas as pd
import platform
import psutil
import json

st.set_page_config(page_title="Evac AI | IBM LinuxONE", layout="wide")

st.sidebar.header("🖥️ IBM LinuxONE Telemetry")
st.sidebar.caption("Team Z-etta Bytes | Real-Time AI")
st.sidebar.metric("System Architecture", platform.machine())
st.sidebar.metric("CPU Utilization", f"{psutil.cpu_percent(interval=0.2)}%")
st.sidebar.metric("Memory Usage", f"{psutil.virtual_memory().percent}%")
st.sidebar.success("Engine: Topographic & JSON Triage Active")

st.title("🚨 Evac AI: Anticipatory Disaster Response Platform")
st.markdown("Topographic elevation routing, dynamic wind/hydro tactical options, and structured JSON dispatch running natively on **IBM Z / LinuxONE (`s390x`)**.")

col1, col2 = st.columns([1, 1.35])

with col1:
    st.subheader("📡 Live Meteorological & Topographic Feed")
    preset = st.selectbox("Select Disaster Scenario", [
        "Chennai Coastal Cyclone Surge",
        "Adyar River Basin Flash Flood",
        "Coimbatore Western Ghats Landslide Risk"
    ])
    
    if preset == "Chennai Coastal Cyclone Surge":
        default_lat, default_lon = 13.0827, 80.2707
    elif preset == "Adyar River Basin Flash Flood":
        default_lat, default_lon = 13.0012, 80.2565
    else:
        default_lat, default_lon = 11.0168, 76.9558

    lat = st.number_input("Origin Latitude", value=default_lat, format="%.4f")
    lon = st.number_input("Origin Longitude", value=default_lon, format="%.4f")
    rainfall = st.slider("Rainfall Intensity (mm/hr)", 0.0, 250.0, 110.0)
    flood_level = st.slider("Water / Inundation Depth (meters)", 0.0, 5.0, 1.4)
    wind_speed = st.slider("Wind Speed (km/h)", 0.0, 200.0, 95.0)
    language = st.selectbox("Public SMS Alert Language", ["Tamil and English", "Hindi and English", "English Only"])

    analyze_btn = st.button("⚡ Execute Real-Time Topographic & JSON Triage", type="primary", use_container_width=True)

with col2:
    st.subheader("🗺️ Geospatial Command & JSON API Dispatch")
    if analyze_btn:
        with st.spinner("Computing topographic elevation vectors, wind load thresholds & JSON payload on LinuxONE..."):
            payload = {
                "zone_name": preset,
                "lat": lat,
                "lon": lon,
                "wind_speed_kmh": wind_speed,
                "rainfall_mm_hr": rainfall,
                "flood_level_m": flood_level,
                "target_language": language
            }
            try:
                res = requests.post("http://127.0.0.1:8000/analyze-crisis", json=payload, timeout=60).json()
                
                m1, m2, m3 = st.columns(3)
                m1.metric("Hazard Severity", res["severity"])
                m2.metric("Triage Risk Score", f"{res['risk_score']} / 100")
                m3.metric("Mainframe Compute Time", f"{res['latency_ms']} ms")
                
                tab1, tab2 = st.tabs(["📄 JSON API Payload (Machine-Readable)", "📢 Formatted State Directive"])
                
                with tab1:
                    json_str = json.dumps(res["json_directive"], indent=2, ensure_ascii=False)
                    st.download_button(
                        label="⬇️ Download Official Government JSON Directive (.json)",
                        data=json_str,
                        file_name=f"{res['json_directive']['directive_id']}.json",
                        mime="application/json",
                        use_container_width=True
                    )
                    st.json(res["json_directive"], expanded=True)
                    
                with tab2:
                    st.markdown(res["ai_dispatch"])
                
                map_df = pd.DataFrame([
                    {"lat": lat, "lon": lon},
                    {"lat": res["safe_lat"], "lon": res["safe_lon"]}
                ])
                st.map(map_df, zoom=11)
            except Exception as e:
                st.error(f"Backend connection error: Make sure backend.py is running! ({e})")
    else:
        st.map(pd.DataFrame([{"lat": default_lat, "lon": default_lon}]), zoom=11)
        st.caption("Adjust the telemetry sliders and click 'Execute Real-Time Topographic & JSON Triage' to generate the JSON payload.")
