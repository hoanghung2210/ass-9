def convert_to_uppercase(input_file):
    with open(input_file, 'r') as infile, open('output.txt', 'w') as outfile:
        for line in infile:
            outfile.write(line.upper())