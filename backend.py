from fastapi import FastAPI
from pydantic import BaseModel
import time
import platform
from datetime import datetime

app = FastAPI(title="Evac AI - LinuxONE Topographic & JSON Engine")

class TelemetryInput(BaseModel):
    zone_name: str
    lat: float
    lon: float
    wind_speed_kmh: float
    rainfall_mm_hr: float
    flood_level_m: float
    target_language: str

@app.post("/analyze-crisis")
def analyze_crisis(data: TelemetryInput):
    start_time = time.time()
    
    # Simulate deep multi-variable mainframe inference (2.8 seconds)
    time.sleep(2.8)
    
    # 1. Multi-Factor Deterministic Triage Score
    score = min(100.0, round((data.rainfall_mm_hr * 0.35) + (data.flood_level_m * 30.0) + (data.wind_speed_kmh * 0.25), 1))
    severity = "CRITICAL (RED ALERT)" if score >= 75 else "HIGH (ORANGE ALERT)" if score >= 45 else "MODERATE (YELLOW ALERT)"
    
    is_landslide = "Landslide" in data.zone_name
    is_cyclone = "Cyclone" in data.zone_name
    
    # 2. Topographical & Geological Profile per Zone
    if is_landslide:
        safe_lat, safe_lon = round(data.lat + 0.028, 4), round(data.lon + 0.032, 4)
        topo = {
            "base_elevation_msl_m": 485.0,
            "shelter_elevation_msl_m": 542.0,
            "required_elevation_gain_m": 57.0,
            "terrain_classification": "Steep Lateritic Escarpment (Western Ghats)",
            "slope_gradient_deg": 32.5,
            "soil_composition": "Weathering Lateritic Clay over Gneiss Bedrock",
            "drainage_threshold_mm_hr": 75.0,
            "shelter_designation": "Thondamuthur Bedrock Plateau Command Camp"
        }
    elif is_cyclone:
        safe_lat, safe_lon = round(data.lat + 0.035, 4), round(data.lon - 0.045, 4)
        topo = {
            "base_elevation_msl_m": 2.1,
            "shelter_elevation_msl_m": 16.4,
            "required_elevation_gain_m": 14.3,
            "terrain_classification": "Low-Lying Coastal Alluvial Plain (Coromandel Coast)",
            "slope_gradient_deg": 0.8,
            "soil_composition": "Saturated Marine Alluvial Sand",
            "drainage_threshold_mm_hr": 45.0,
            "shelter_designation": "Egmore High-Ground Multi-Storey Cyclone Bunker"
        }
    else:
        safe_lat, safe_lon = round(data.lat + 0.032, 4), round(data.lon - 0.025, 4)
        topo = {
            "base_elevation_msl_m": 6.4,
            "shelter_elevation_msl_m": 22.0,
            "required_elevation_gain_m": 15.6,
            "terrain_classification": "Estuarine Riverine Floodplain (Adyar Basin)",
            "slope_gradient_deg": 1.4,
            "soil_composition": "Impervious Urban Clayey Silt",
            "drainage_threshold_mm_hr": 55.0,
            "shelter_designation": "Guindy Elevated Relief & Medical Complex"
        }

    # 3. Dynamic Wind Speed Physics & Protocol Options
    if data.wind_speed_kmh >= 120:
        wind_class = "Cyclonic Super-Gale ( Beaufort Scale 12 )"
        wind_option = (
            f"EXTREME WIND LOCKDOWN ({data.wind_speed_kmh} km/h): Aerodynamic overturning risk for buses and ambulances. "
            "Halt all elevated flyover transit. Deploy low-center-of-gravity tracked armored military carriers or mandate immediate vertical sheltering in reinforced concrete cores."
        )
    elif data.wind_speed_kmh >= 65:
        wind_class = "Severe Gale Force ( Beaufort Scale 8-11 )"
        wind_option = (
            f"HIGH WIND CORRIDOR RESTRICTION ({data.wind_speed_kmh} km/h): Ban two-wheelers and high-profile canvas trucks. "
            "Reroute evacuation convoys through wind-shielded inland avenues; active hazard of snapping 11kV overhead cables and uprooted avenue trees."
        )
    else:
        wind_class = "Moderate Breeze / Safe Transit ( Beaufort Scale 1-7 )"
        wind_option = (
            f"STANDARD AERODYNAMIC CLEARANCE ({data.wind_speed_kmh} km/h): Wind velocity is within safe operational limits. "
            "State Transport (TNSTC) bus fleets, medical ambulances, and aerial surveillance drones are cleared for rapid deployment."
        )

    # 4. Dynamic Water Depth / Flood Level Mobility Options
    if data.flood_level_m >= 2.2:
        hydro_status = "Catastrophic Submergence (Ground Floor Inundated)"
        mobility_option = (
            f"WHEELED TRANSIT IMPOSSIBLE ({data.flood_level_m}m depth): Ground infrastructure completely submerged. "
            "Activate NDRF Inflatable Zodiac Boat corridors and Indian Air Force rooftop winch extraction for trapped citizens."
        )
    elif data.flood_level_m >= 0.7:
        hydro_status = "Deep Hydrostatic Inundation (Civilian Vehicles Stalled)"
        mobility_option = (
            f"HEAVY HIGH-CLEARANCE EXTRACTION ONLY ({data.flood_level_m}m depth): Buoyancy risk will sweep away civilian cars. "
            "Restrict evacuation strictly to NDRF high-clearance 4x4 Ashok Leyland Stallion trucks and tractor-trailers."
        )
    else:
        hydro_status = "Surface Sheet Runoff (Arterial Roads Passable)"
        mobility_option = (
            f"WHEELED CONVOY CLEARANCE ({data.flood_level_m}m depth): Crown of elevated arterial highways remains passable. "
            "Execute rapid civilian and state bus convoy movement along central medians; barricade dipped railway underpasses."
        )

    # 5. Dynamic Rainfall & Soil Saturation Calculation
    drainage_surplus = round(max(0.0, data.rainfall_mm_hr - topo["drainage_threshold_mm_hr"]), 1)
    soil_saturation_pct = min(100.0, round(45.0 + (data.rainfall_mm_hr * 0.25) + (data.flood_level_m * 8.0), 1))
    
    if is_landslide:
        slope_stability = "IMMINENT SHEAR FAILURE" if soil_saturation_pct >= 80 else "MODERATE CREEP RISK"
        route_instruction = (
            f"Ascend +{topo['required_elevation_gain_m']}m laterally across the {topo['slope_gradient_deg']}° contour line toward "
            f"{topo['shelter_designation']} ({safe_lat}, {safe_lon}). Avoid valley thalwegs where pore-water pressure is at {soil_saturation_pct}%."
        )
    else:
        slope_stability = "STABLE FLATLAND / HIGH HYDRO-RUNOFF"
        route_instruction = (
            f"Ascend +{topo['required_elevation_gain_m']}m inland from {topo['base_elevation_msl_m']}m MSL to {topo['shelter_elevation_msl_m']}m MSL "
            f"at {topo['shelter_designation']} ({safe_lat}, {safe_lon}). Stormwater grid is surcharged by +{drainage_surplus} mm/hr."
        )

    # 6. Dynamic Data-Driven Multilingual SMS Broadcast
    if "Tamil" in data.target_language:
        sms = (
            f"[TN GOVT ALERT - EVAC AI] {severity}: {data.zone_name} பகுதியில் {data.rainfall_mm_hr}mm/hr மழை, "
            f"{data.wind_speed_kmh}km/h காற்று மற்றும் {data.flood_level_m}m நீர்மட்டம் பதிவாகியுள்ளது. "
            f"உடனடியாக +{topo['required_elevation_gain_m']}m உயரத்தில் உள்ள அரசு பாதுகாப்பு முகாமிற்கு ({safe_lat}, {safe_lon}) செல்லவும். அவசர உதவி: 1070."
        )
    elif "Hindi" in data.target_language:
        sms = (
            f"[GOVT ALERT - EVAC AI] {severity}: {data.zone_name} में {data.rainfall_mm_hr}mm/hr बारिश, "
            f"{data.wind_speed_kmh}km/h हवा और {data.flood_level_m}m जल स्तर दर्ज किया गया है। "
            f"तुरंत +{topo['required_elevation_gain_m']}m ऊंचाई पर स्थित सरकारी राहत शिविर ({safe_lat}, {safe_lon}) में जाएं। सहायता: 1070।"
        )
    else:
        sms = (
            f"[GOVT ALERT - EVAC AI] {severity} in {data.zone_name}: Telemetry confirms {data.rainfall_mm_hr}mm/hr rain, "
            f"{data.wind_speed_kmh}km/h winds, and {data.flood_level_m}m water depth. Evacuate +{topo['required_elevation_gain_m']}m uphill "
            f"to {topo['shelter_designation']} ({safe_lat}, {safe_lon}). Helpline: 1070."
        )

    latency_ms = round((time.time() - start_time) * 1000, 1)

    # 7. Construct Official Machine-Readable JSON Directive
    json_directive = {
        "directive_id": f"TN-SDMA-{int(time.time())}",
        "timestamp_utc": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "compute_node": {
            "platform": "IBM LinuxONE (s390x)",
            "architecture": platform.machine(),
            "inference_latency_ms": latency_ms,
            "engine_mode": "Deterministic Geospatial & Topographic Triage v2.4"
        },
        "hazard_assessment": {
            "zone_name": data.zone_name,
            "composite_risk_score": score,
            "alert_classification": severity,
            "section_144_curfew_active": bool(score >= 45)
        },
        "topography_and_geology": {
            "origin_coordinates": {"lat": data.lat, "lon": data.lon},
            "safe_shelter_coordinates": {"lat": safe_lat, "lon": safe_lon},
            "shelter_name": topo["shelter_designation"],
            "origin_elevation_msl_m": topo["base_elevation_msl_m"],
            "shelter_elevation_msl_m": topo["shelter_elevation_msl_m"],
            "net_elevation_gain_required_m": topo["required_elevation_gain_m"],
            "terrain_type": topo["terrain_classification"],
            "slope_gradient_degrees": topo["slope_gradient_deg"],
            "soil_composition": topo["soil_composition"],
            "soil_saturation_index_pct": soil_saturation_pct,
            "geological_stability": slope_stability
        },
        "meteorological_telemetry_options": {
            "wind_speed_kmh": data.wind_speed_kmh,
            "wind_scale_classification": wind_class,
            "wind_based_tactical_option": wind_option,
            "rainfall_intensity_mm_hr": data.rainfall_mm_hr,
            "stormwater_drainage_surplus_mm_hr": drainage_surplus,
            "water_inundation_depth_m": data.flood_level_m,
            "hydro_mobility_status": hydro_status,
            "flood_based_extraction_option": mobility_option
        },
        "state_mandated_protocol": {
            "step_1_topographic_routing": route_instruction,
            "step_2_wind_adapted_logistics": wind_option,
            "step_3_hydro_extraction_mode": mobility_option,
            "step_4_agency_deployment": (
                "NDRF Marine & IAF Rotary Wing" if data.flood_level_m >= 2.2
                else "SDRF Heavy 4x4 Convoy & TNEB Grid Isolation Squads" if score >= 45
                else "District Collectorate Rapid Response & Traffic Police Corridors"
            )
        },
        "public_broadcast_dispatch": {
            "target_language": data.target_language,
            "emergency_helpline": "1070 / 112",
            "sms_character_length": len(sms),
            "broadcast_message": sms
        }
    }

    # Human-readable summary alongside the JSON
    ai_text = (
        f"**[GOVERNMENT DIRECTIVE: {json_directive['directive_id']}]** Topographic & Meteorological Triage for **{data.zone_name}**\n\n"
        f"**⛰️ TOPOGRAPHIC & GEOLOGICAL PROFILE:**\n"
        f"- **Terrain & Soil:** {topo['terrain_classification']} ({topo['soil_composition']}) | **Slope:** `{topo['slope_gradient_deg']}°` | **Saturation:** `{soil_saturation_pct}%` ({slope_stability})\n"
        f"- **Elevation Vector:** Ascend **`+{topo['required_elevation_gain_m']}m`** (from `{topo['base_elevation_msl_m']}m MSL` to `{topo['shelter_elevation_msl_m']}m MSL`) toward **{topo['shelter_designation']}** `({safe_lat}, {safe_lon})`.\n\n"
        f"**🗺️ TELEMETRY-DRIVEN EVACUATION OPTIONS:**\n"
        f"1. **Topographic Route:** {route_instruction}\n"
        f"2. **Wind-Adapted Protocol (`{data.wind_speed_kmh} km/h` - {wind_class}):** {wind_option}\n"
        f"3. **Hydro-Extraction Mode (`{data.flood_level_m}m` depth - {hydro_status}):** {mobility_option}\n"
        f"4. **Drainage & Grid Directive (`{data.rainfall_mm_hr} mm/hr`):** Urban drainage exceeded by `+{drainage_surplus} mm/hr`. Deployed: **{json_directive['state_mandated_protocol']['step_4_agency_deployment']}**.\n\n"
        f"**📱 PUBLIC SMS BROADCAST ({data.target_language}):**\n"
        f"> {sms}"
    )

    return {
        "risk_score": score,
        "severity": severity,
        "safe_lat": safe_lat,
        "safe_lon": safe_lon,
        "latency_ms": latency_ms,
        "ai_dispatch": ai_text,
        "json_directive": json_directive
    }
