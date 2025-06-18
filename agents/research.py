from agents.geocode import get_jurisdiction

def run_research(location, center_type, services=None, center_code=None, center_name=None):
    # 1. Geolocate jurisdiction info
    jurisdiction = get_jurisdiction(location)
    if isinstance(jurisdiction, str):  # Error message
        return jurisdiction

    city = jurisdiction.get("city", "N/A")
    county = jurisdiction.get("county", "N/A")
    state = jurisdiction.get("state", "N/A")
    country = jurisdiction.get("country", "USA")
    formatted_address = jurisdiction.get("formatted", location)

    # 2. Compose service list (optional for memory/logging, not filtering yet)
    active_services = [name.replace('_', ' ').title() for name, selected in (services or {}).items() if selected]
    service_list = ", ".join(active_services) if active_services else "Not specified"

    # 3. Begin structured output
    header = f"""📍 **Regulatory Research Report**
------------------------------------------------------------
🆔 Center Code: {center_code or 'N/A'}
🏢 Center Name: {center_name or 'N/A'}
🏷️ Center Type: {center_type or 'Not specified'}
📍 Location: {formatted_address}
🏙️ City: {city}
🏞️ County: {county}
📍 State: {state}
🌐 Country: {country}
🔧 Services: {service_list}

"""

    # 4. Core Requirements (These will be replaced with real API/data results later)
    local_section = f"""🏛️ **Local/City Requirements** ({city})
- Certificate of Occupancy: 🔍 CHECK REQUIRED
- Fire/Life Safety Inspection: 🔍 CHECK REQUIRED
- Alarm Permit (Fire/Security): 🔍 CHECK REQUIRED
- Sign Permit: 🔍 CHECK REQUIRED
- Business License or Tax Receipt: 🔍 CHECK REQUIRED
"""

    county_section = f"""🏞️ **County Requirements** ({county})
- Business Registration/License: 🔍 CHECK REQUIRED
- Kennel/Grooming Licenses (if applicable): 🔍 CHECK REQUIRED
"""

    state_section = f"""🏛️ **State Requirements** ({state})
- Sales Tax/Use Tax Account: 🔍 CHECK REQUIRED
- Pet Business Licenses: 🔍 CHECK REQUIRED
"""

    vet_extras = ""
    if center_type == "Vet Center":
        vet_extras = """
💉 **Vet Center-Specific Requirements**
- Medical Waste Generator Permit: 🔍 CHECK REQUIRED
- Hazardous Waste Registration: 🔍 CHECK REQUIRED
- X-Ray Facility and Machine Registration: 🔍 CHECK REQUIRED
- State Controlled Substance Registration: 🔍 CHECK REQUIRED
- DEA License (Federal): 🔍 CHECK REQUIRED
- Compressed Gas Storage Permit: 🔍 CHECK REQUIRED
"""

    # 5. Final output
    return header + local_section + county_section + state_section + vet_extras
