from openai import OpenAI
import os
from agents.geocode import get_jurisdiction

# Initialize OpenAI client using new SDK interface
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_research(location, center_type, services=None, center_code=None, center_name=None):
    # Step 1: Geolocation
    jurisdiction = get_jurisdiction(location)
    if isinstance(jurisdiction, str):  # Error case
        return jurisdiction

    city = jurisdiction.get("city", "N/A")
    county = jurisdiction.get("county", "N/A")
    state = jurisdiction.get("state", "N/A")
    country = jurisdiction.get("country", "USA")
    formatted_address = jurisdiction.get("formatted", location)

    # Step 2: Header
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
"""

    # Step 3: Compliance Sections
    local_section = f"""## LOCAL ({city})
- Business License from the City of {city}
- Zoning Permit from the City of {city}
- Health Department Permit for handling animals
- Sign Permit for any outdoor signage
- Waste Disposal Permit for handling animal waste
- ⚠️ Local Business Tax Receipt or Municipal Tax License
"""

    county_section = f"""## COUNTY ({county})
- Kennel or Pet Facility License (if applicable)
- Health Dept Certificate (if county-regulated)
"""

    state_section = f"""## STATE ({state})
- Sales/Use Tax Registration with Department of Revenue
- Pet Facility or Kennel License (if required)
- ⚠️ State Unemployment Insurance Registration
- ⚠️ Withholding Tax Account (if employing staff)
"""

    federal_section = """## FEDERAL (United States)
- Employer Identification Number (EIN) from the IRS
- Occupational Safety and Health Administration (OSHA) Compliance
- ⚠️ Environmental Protection Agency (EPA) Permit (if chemicals used)
"""

    vet_section = ""
    if center_type == "Vet Center":
        vet_section = """## VET CENTER-SPECIFIC
- Medical Waste Generator Permit
- Hazardous Waste Registration
- X-Ray Facility and Machine Registration
- State Controlled Substance Registration
- DEA License for Controlled Substances
- Compressed Gas Storage Permit (e.g. Oxygen)
"""

    # Step 4: Final output
    footer = "\nPlease verify with official government portals. This advisory tool offers a strong starting point for research."

    return header + "\n" + local_section + county_section + state_section + federal_section + vet_section + footer
