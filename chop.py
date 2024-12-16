import csv

def filter_ligands(input_csv, output_csv, include_ligands):
    """Filter the results to include only specific ligands."""
    filtered_results = []
    
    # Read the input CSV file
    with open(input_csv, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header
        filtered_results.append(header)  # Keep the header in the output file
        
        for row in reader:
            ligand = row[2]  # Assuming the ligand is in the 3rd column (index 2)
            if ligand in include_ligands:
                filtered_results.append(row)
    
    # Write the filtered results to a new output CSV (no extra newlines)
    with open(output_csv, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(filtered_results)

# List of ligands to include
include_ligands = [
    "001", "002", "003", "004", "005", "010", "016", "017", "018", "019", "020",
    "021", "022", "023", "025", "026", "028", "030", "031", "034", "035", "037",
    "038", "039", "043", "044", "046", "047", "048", "049", "050", "052", "054",
    "055", "057", "058", "064", "066", "067", "068", "069", "070", "071", "073",
    "074", "075", "076", "077", "079", "080", "082", "083", "084", "085", "087",
    "089", "090", "091", "092", "093", "094", "095", "098", "100", "101", "102",
    "103", "105", "108", "109", "112", "113", "114", "116", "117", "118", "119",
    "120", "121", "122", "123", "124", "125", "126", "129", "130", "131", "133",
    "134", "135", "136", "139", "140", "141", "144", "145", "146", "147", "148",
    "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159",
    "160", "161", "162", "164", "165", "166", "167", "168", "169", "170", "171",
    "172", "174", "176", "177", "178", "179", "182", "183", "184", "185", "186",
    "187", "188", "189", "190", "191", "193", "194", "195", "196", "197"
]

# Example usage
input_csv = "averaged_coordinates_with_affinity.csv"  # Your input file
output_csv = "filtered_coordinates.csv"  # Output file with only the included ligands

filter_ligands(input_csv, output_csv, include_ligands)
