def render_compliance_sections(center_type, city, state):
    city_key = city or "Local"
    state_key = state or "State"

    pet_local = [
        f"Business License from the City of {city_key} (https://example.com/{city_key.lower()}/business-license)",
        f"Zoning Permit from the City of {city_key} (https://example.com/{city_key.lower()}/zoning)",
        f"Health Department Permit for handling animals (https://example.com/{city_key.lower()}/animal-health)",
        f"Sign Permit for any outdoor signage (https://example.com/{city_key.lower()}/signs)",
        f"Waste Disposal Permit for handling animal waste (https://example.com/{city_key.lower()}/waste)"
    ]

    pet_state = [
        f"{state_key} Department of Agriculture license for animal-related businesses (https://example.com/{state_key.lower().replace(' ', '-')}/agriculture)",
        f"⚠️ X-Ray Registration for any x-ray equipment used in the center (https://example.com/{state_key.lower().replace(' ', '-')}/radiology)",
        f"⚠️ DEA License if dispensing controlled substances (https://dea.gov)",
        f"⚠️ Hazardous Waste Permit for handling hazardous materials (https://example.com/{state_key.lower().replace(' ', '-')}/hazardous-waste)"
    ]

    pet_federal = [
        "Employer Identification Number (EIN) from the IRS (https://irs.gov)",
        "Occupational Safety and Health Administration (OSHA) Standards compliance (https://osha.gov)",
        "⚠️ USDA Animal Welfare License for certain animal-related activities (https://www.aphis.usda.gov/)",
        "⚠️ Environmental Protection Agency (EPA) Permit for any chemical usage (https://epa.gov)"
    ]

    vet_extras = [
        "Medical Waste Generator Permit (https://example.com/medical-waste)",
        "Hazardous Waste Registration (https://example.com/hazardous-waste)",
        "X-Ray Facility and Machine Registration (https://example.com/xray-reg)",
        "State Controlled Substance Registration (https://example.com/state-controlled-substances)",
        "DEA License for controlled drug handling (https://www.deadiversion.usdoj.gov/)",
        "Compressed Gas Storage Permit (https://example.com/oxygen-storage)"
    ]

    def bullet_list(items):
        return "\n".join([f"- {item}" for item in items])

    text = f"""
# Compliance Requirements for {center_type or 'Pet Center'} in {city_key}, {state_key}

## LOCAL ({city_key})
{bullet_list(pet_local)}

## STATE ({state_key})
{bullet_list(pet_state)}

## FEDERAL (United States)
{bullet_list(pet_federal)}
"""

    if center_type == "Vet Center":
        text += f"\n## VET CENTER-SPECIFIC\n{bullet_list(vet_extras)}"

    text += "\n\nPlease note that additional requirements may apply based on the specific services offered by the center. It is recommended to verify with the relevant authorities for the most up-to-date compliance information."

    return text.strip()
