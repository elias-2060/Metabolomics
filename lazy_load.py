import pandas as pd

chunk_size = 100  # Adjust this based on your system's memory
file_path = 'spectrum_annotaties/annotatie1.tsv'

# Set display options to show all columns
pd.set_option('display.max_columns', None)

# Read the TSV file lazily into a generator
chunk_generator = pd.read_csv(file_path, sep='\t', chunksize=chunk_size)

# Process chunks selectively based on user input or specific conditions
# For example, let's say you want to process chunks based on user input
process_chunks = True

while process_chunks:
    user_input = input("Press Enter to process next chunk, or 'q' to quit: ")

    if user_input.lower() == 'q':
        process_chunks = False
    else:
        try:
            chunk = next(chunk_generator)
            # Process the chunk as needed
            print(chunk.to_string(index=False))  # Display the entire chunk without index
        except StopIteration:
            print("End of file reached.")
            break
