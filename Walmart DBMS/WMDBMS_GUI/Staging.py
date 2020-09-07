import helper_funcs as hf
import SQL_queries as sql

def get_staging_info():
    '''
    - Input -
    None
    
    - Output -
    Loc -- String: Holds the location of where to stage.
    Totes -- List: Holds all of the totes in a row.
    curr_tote -- String: Holds the current tote being scanned in.
    
    - Return -
    Loc --- String
    Totes --- List
    '''
    curr_tote = ""
    Loc = ""
    Totes = []
    
    # Get location for totes in a single row
    Loc = input("Scan a location: ")
    
    # Clear and take in totes in row tied to location
    hf.clear()
    
    while(curr_tote != "END"):
        curr_tote = ""
        curr_tote = input("Scan tote: ")
        
        # Ensure duplicate totes are not scanned into same row
        if(curr_tote not in Totes and curr_tote != "END"):
            Totes.append(curr_tote)
            
    # Clear screen for next instructions
    hf.clear()
            
    # Send back list of totes in row and the location to stage
    return Loc, Totes

def get_query_stage(Loc, curr):
    '''
    - Input -
    Loc -- String: Holds the new location of the current tote
    curr -- String: Holds the current tote
    
    - Output -
    query -- String: Holds the returned proper query
    
    - Return -
    query --- String
    '''
    query = ""
    
    query = sql.stage_curr_tote(Loc, curr)
    
    return query