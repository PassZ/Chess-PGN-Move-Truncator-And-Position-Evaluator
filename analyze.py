#!/usr/bin/env python
'''
    analyze.py: Analyze a PGN file of many chess games with an engine using UCI engine communication 
                Writes the games to a new PGN file based on the desired evaluation threshold.
                                                                                                    '''
__author__ = "PassZ"
__version__ = "1.0.0"

# Imports
import chess
import chess.pgn
import subprocess
import sys

# Make sure the user provides the correct number of command-line arguments
if len(sys.argv) < 3:
    print("Usage: python analyze.py input.pgn output.pgn")
    sys.exit(1)

# Get the input and output file names from the command line
input_file = sys.argv[1]
output_file = sys.argv[2]

# Set up the engine and its filepath
engine = chess.engine.SimpleEngine.popen_uci("stockfish15win.exe")

# Open the input PGN file that we are reading from
# May need to play around with the encodings to see what works for your files
# Examples: "utf-8-sig", "utf-8", "latin-1", "cp1252"
with open(input_file, "r", encoding="utf-8-sig") as input_pgn:

    # Open the output PGN file that we are writing to
    with open(output_file, "w", encoding="utf-8-sig") as output_pgn:

        # Loop through the games in the input PGN file
        while True:

            # Try catch block to handle any errors that may occur such as:
            # Illegal position or encoding errors (Some of the games in my .pgn file had strange characters)
            try:

                # Read the next game from the input PGN file
                game = chess.pgn.read_game(input_pgn)

                # If the game is None, then we have reached the end of the file
                if game is None:
                    break

                # Get the board from the game
                board = game.board()

                # Run the chess engine on the board
                info = engine.analyse(board, chess.engine.Limit(depth=20))

                # Pull the score from the info
                evaluation = info["score"].relative.score()

                # Check if evaluation is greater than or equal to 0 (White has an advantage)
                if evaluation >= 0:

                    # Write the game to the output PGN file
                    output_pgn.write(str(game) + "\n\n")
            except:
                pass
            
# Close the engine
engine.quit()