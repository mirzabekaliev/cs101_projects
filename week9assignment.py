def decode_packet(packet_string, required_fields):
    #Check format, ends with ;
    if not packet_string.endswith(";"):
        return "Error: Invalid packet format."
    
    #Remove last semicolon
    core = packet_string[:-1]
    
    #Split into key-value pairs
    pairs = core.split("|")
    data = {}
    
    for p in pairs:
        # Each pair contain one colon
        if ":" not in p:
            return "Error: Invalid packet format."
        
        key, value = p.split(":", 1)  
        data[key] = value
    
    #Checking fields
    missing = [field for field in required_fields if field not in data]
    
    if missing:
        return f"Error: Missing required fields: {missing}"
    
    #Return values in order
    return [data[field] for field in required_fields]
