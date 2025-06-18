def run_research(location, center_type, services):
    active_services = [name.replace('_', ' ').title() for name, selected in services.items() if selected]
    
    service_list = ", ".join(active_services) if active_services else "no specific services selected"
    
    return f"""
Research initialized for: {center_type or 'Unspecified Type'} at {location}

Services identified: {service_list}

(Note: This is a placeholder. Future versions will provide actual licensing, inspection, and permitting requirements based on this data.)
"""
