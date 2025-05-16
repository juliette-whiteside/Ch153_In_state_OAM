# This file contains direct product tables for various point groups

# D4h point group data
d4h_data = {
    "irreps": [
        "A1g", "A2g", "B1g", "B2g", "Eg",  # Gerade (even) irreps
        "A1u", "A2u", "B1u", "B2u", "Eu"   # Ungerade (odd) irreps
    ],
    "Lz_irrep": "A2g",  # Lz transforms as A2g in D4h
    "Lx_irrep": "Eg", 
    "Ly_irrep": "Eg", 
    "totally_symmetric": "A1g",  # The totally symmetric irrep in D4h
    
    # Direct product table for D4h
    "direct_products": {
        # Products with A1g (totally symmetric)
        ("A1g", "A1g"): "A1g",
        ("A1g", "A2g"): "A2g",
        ("A1g", "B1g"): "B1g",
        ("A1g", "B2g"): "B2g",
        ("A1g", "Eg"): "Eg",
        ("A1g", "A1u"): "A1u",
        ("A1g", "A2u"): "A2u",
        ("A1g", "B1u"): "B1u",
        ("A1g", "B2u"): "B2u",
        ("A1g", "Eu"): "Eu",
        
        # Products with A2g
        ("A2g", "A2g"): "A1g",
        ("A2g", "B1g"): "B2g",
        ("A2g", "B2g"): "B1g",
        ("A2g", "Eg"): "Eg",
        ("A2g", "A1u"): "A2u",
        ("A2g", "A2u"): "A1u",
        ("A2g", "B1u"): "B2u",
        ("A2g", "B2u"): "B1u",
        ("A2g", "Eu"): "Eu",
        
        # Products with B1g
        ("B1g", "B1g"): "A1g",
        ("B1g", "B2g"): "A2g",
        ("B1g", "Eg"): "Eg",
        ("B1g", "A1u"): "B1u",
        ("B1g", "A2u"): "B2u",
        ("B1g", "B1u"): "A1u",
        ("B1g", "B2u"): "A2u",
        ("B1g", "Eu"): "Eu",
        
        # Products with B2g
        ("B2g", "B2g"): "A1g",
        ("B2g", "Eg"): "Eg",
        ("B2g", "A1u"): "B2u",
        ("B2g", "A2u"): "B1u",
        ("B2g", "B1u"): "A2u",
        ("B2g", "B2u"): "A1u",
        ("B2g", "Eu"): "Eu",
        
        # Products with Eg
        ("Eg", "Eg"): "A1g + A2g + B1g + B2g",
        ("Eg", "A1u"): "Eu",
        ("Eg", "A2u"): "Eu",
        ("Eg", "B1u"): "Eu",
        ("Eg", "B2u"): "Eu",
        ("Eg", "Eu"): "A1u + A2u + B1u + B2u",
        
        # Products with ungerade irreps
        ("A1u", "A1u"): "A1g",
        ("A1u", "A2u"): "A2g",
        ("A1u", "B1u"): "B1g",
        ("A1u", "B2u"): "B2g",
        ("A1u", "Eu"): "Eg",
        
        ("A2u", "A2u"): "A1g",
        ("A2u", "B1u"): "B2g",
        ("A2u", "B2u"): "B1g",
        ("A2u", "Eu"): "Eg",
        
        ("B1u", "B1u"): "A1g",
        ("B1u", "B2u"): "A2g",
        ("B1u", "Eu"): "Eg",
        
        ("B2u", "B2u"): "A1g",
        ("B2u", "Eu"): "Eg",
        
        ("Eu", "Eu"): "A1g + A2g + B1g + B2g"
    }
}

# Oh point group data
oh_data = {
    "irreps": [
        "A1g", "A2g", "Eg", "T1g", "T2g",  # Gerade (even) irreps
        "A1u", "A2u", "Eu", "T1u", "T2u"   # Ungerade (odd) irreps
    ],
    "Lz_irrep": "T1g",  # Lz transforms as T1g in Oh
    "Ly_irrep": "T1g", 
    "Lx_irrep": "T1g",  
    "totally_symmetric": "A1g",  # The totally symmetric irrep in Oh
    
    # Complete direct product table for Oh
    "direct_products": {
        # Products with A1g (totally symmetric)
        ("A1g", "A1g"): "A1g",
        ("A1g", "A2g"): "A2g",
        ("A1g", "Eg"): "Eg",
        ("A1g", "T1g"): "T1g",
        ("A1g", "T2g"): "T2g",
        ("A1g", "A1u"): "A1u",
        ("A1g", "A2u"): "A2u",
        ("A1g", "Eu"): "Eu",
        ("A1g", "T1u"): "T1u",
        ("A1g", "T2u"): "T2u",
        
        # Products with A2g
        ("A2g", "A2g"): "A1g",
        ("A2g", "Eg"): "Eg",
        ("A2g", "T1g"): "T2g",
        ("A2g", "T2g"): "T1g",
        ("A2g", "A1u"): "A2u",
        ("A2g", "A2u"): "A1u",
        ("A2g", "Eu"): "Eu",
        ("A2g", "T1u"): "T2u",
        ("A2g", "T2u"): "T1u",
        
        # Products with Eg
        ("Eg", "Eg"): "A1g + A2g + Eg",
        ("Eg", "T1g"): "T1g + T2g",
        ("Eg", "T2g"): "T1g + T2g",
        ("Eg", "A1u"): "Eu",
        ("Eg", "A2u"): "Eu",
        ("Eg", "Eu"): "A1u + A2u + Eu",
        ("Eg", "T1u"): "T1u + T2u",
        ("Eg", "T2u"): "T1u + T2u",
        
        # Products with T1g
        ("T1g", "T1g"): "A1g + Eg + T1g + T2g",
        ("T1g", "T2g"): "A2g + Eg + T1g + T2g",
        ("T1g", "A1u"): "T1u",
        ("T1g", "A2u"): "T2u",
        ("T1g", "Eu"): "T1u + T2u",
        ("T1g", "T1u"): "A1u + Eu + T1u + T2u",
        ("T1g", "T2u"): "A2u + Eu + T1u + T2u",
        
        # Products with T2g
        ("T2g", "T2g"): "A1g + Eg + T1g + T2g",
        ("T2g", "A1u"): "T2u",
        ("T2g", "A2u"): "T1u",
        ("T2g", "Eu"): "T1u + T2u",
        ("T2g", "T1u"): "A2u + Eu + T1u + T2u",
        ("T2g", "T2u"): "A1u + Eu + T1u + T2u",
        
        # Products with ungerade irreps
        ("A1u", "A1u"): "A1g",
        ("A1u", "A2u"): "A2g",
        ("A1u", "Eu"): "Eg",
        ("A1u", "T1u"): "T1g",
        ("A1u", "T2u"): "T2g",
        
        ("A2u", "A2u"): "A1g",
        ("A2u", "Eu"): "Eg",
        ("A2u", "T1u"): "T2g",
        ("A2u", "T2u"): "T1g",
        
        ("Eu", "Eu"): "A1g + A2g + Eg",
        ("Eu", "T1u"): "T1g + T2g",
        ("Eu", "T2u"): "T1g + T2g",
        
        ("T1u", "T1u"): "A1g + Eg + T1g + T2g",
        ("T1u", "T2u"): "A2g + Eg + T1g + T2g",
        
        ("T2u", "T2u"): "A1g + Eg + T1g + T2g"
    }
}

# D3h point group data
d3h_data = {
    "irreps": [
        "A1'", "A2'", "E'",     # Symmetric with respect to σh (')
        "A1\"", "A2\"", "E\""   # Antisymmetric with respect to σh (")
    ],
    "Lz_irrep": "A2'",  # Lz transforms as A2' in D3h
    "Lx_irrep": "E\"",  
    "Ly_irrep": "E\"", 
    "totally_symmetric": "A1'",  # The totally symmetric irrep in D3h
    
    # Direct product table for D3h
    "direct_products": {
        # Products with A1' (totally symmetric)
        ("A1'", "A1'"): "A1'",
        ("A1'", "A2'"): "A2'",
        ("A1'", "E'"): "E'",
        ("A1'", "A1\""): "A1\"",
        ("A1'", "A2\""): "A2\"",
        ("A1'", "E\""): "E\"",
        
        # Products with A2'
        ("A2'", "A2'"): "A1'",
        ("A2'", "E'"): "E'",
        ("A2'", "A1\""): "A2\"",
        ("A2'", "A2\""): "A1\"",
        ("A2'", "E\""): "E\"",
        
        # Products with E'
        ("E'", "E'"): "A1' + A2' + E'",
        ("E'", "A1\""): "E\"",
        ("E'", "A2\""): "E\"",
        ("E'", "E\""): "A1\" + A2\" + E\"",
        
        # Products with A1"
        ("A1\"", "A1\""): "A1'",
        ("A1\"", "A2\""): "A2'",
        ("A1\"", "E\""): "E'",
        
        # Products with A2"
        ("A2\"", "A2\""): "A1'",
        ("A2\"", "E\""): "E'",
        
        # Products with E"
        ("E\"", "E\""): "A1' + A2' + E'"
    }
}

# Td point group data
td_data = {
    "irreps": [
        "A1", "A2", "E", "T1", "T2"  # Irreps of Td
    ],
    "Lz_irrep": "T1",  # Lz transforms as T1 in Td
    "Ly_irrep": "T1",  # Lz transforms as T1 in Td
    "Lx_irrep": "T1",  # Lz transforms as T1 in Td
    "totally_symmetric": "A1",  # The totally symmetric irrep in Td
    
    # Direct product table for Td
    "direct_products": {
        # Products with A1 (totally symmetric)
        ("A1", "A1"): "A1",
        ("A1", "A2"): "A2",
        ("A1", "E"): "E",
        ("A1", "T1"): "T1",
        ("A1", "T2"): "T2",
        
        # Products with A2
        ("A2", "A2"): "A1",
        ("A2", "E"): "E",
        ("A2", "T1"): "T2",
        ("A2", "T2"): "T1",
        
        # Products with E
        ("E", "E"): "A1 + A2 + E",
        ("E", "T1"): "T1 + T2",
        ("E", "T2"): "T1 + T2",
        
        # Products with T1
        ("T1", "T1"): "A1 + E + T1 + T2",
        ("T1", "T2"): "A2 + E + T1 + T2",
        
        # Products with T2
        ("T2", "T2"): "A1 + E + T1 + T2"
    }
}

# Dictionary mapping point group names to their data
point_groups = {
    "D4h": d4h_data,
    "Oh": oh_data,
    "D3h": d3h_data,
    "Td": td_data
}
