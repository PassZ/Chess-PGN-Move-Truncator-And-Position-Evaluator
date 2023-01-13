# Chess-PGN-Move-Truncator-And-Position-Evaluator
Truncate a PGN file of many chess games down to the first 20 moves (Or however many you want). Analyze a PGN file of many chess games with an engine using UCI engine communication and keeps games based on the desired evaluation threshold.

If you are anything like me, I have scowered the internet for a free PGN database of thorough opening lines. However, none of them are as in depth as I would like.
For example, they may only go up to ~10 moves of theory, the only source I was left with were chess books... And they won't tell me if I played a wrong move! I wanted to study opening lines for my particular repertoire up to 20 moves and have a PGN of this that I could say load into Chess Position Trainer so I can practice them and see if I got them right. I found a phenomenal database of chess PGNs by codekiddy-chess on sourceforge.net and uploaded these games into SCID as a database. I was then able to filter by player ratings, series of moves/ECO, and result of the game. This was the best way to filter down grandmaster games that I wanted to look at to enhance my opening repertoire. But, these files were simply too big even after filtering them to import into Chess Position Trainer. I could not find any practical way to truncate these games down except manually so I created a python script to do it! Now, even grandmasters make mistakes sometimes so I made another script that analyzes the position of the board after the 20th move to ensure that I was only studying games where the color I want to play has an 'advantage', despite already knowing the outcome of the game.

With these two scripts you are able to truncate grandmaster games down to a number of moves that you want to study, as well as ensure that the color you are trying to study has an 'advantage' in the position!

Chess Position Trainer - https://www.chesspositiontrainer.com/index.php/de/

Shane's Chess Information Database (SCID) - https://sourceforge.net/projects/scid/files/latest/download?source=files

15 Million Games Chess Database - https://sourceforge.net/projects/codekiddy-chess/

Latest Version of Stockfish - https://stockfishchess.org/download/

# How to Run in Command Line
```

//Make sure that the directory you are in contains: Chess engine and your games input file
cd C:\usr\name  // Set to the directory you want to work from

python truncate.py input.txt output.txt // input.txt is your input file with your games
                                        // output.txt is the name of the file we will be generating with the outputs

python analyze.py input.pgn output.pgn  // input.pgn is your input file with your games
                                        // output.pgn is the name of the file we will be generating with the outputs
                                        
```

# More UCI Engine Communication Capabilities
There are a lot more methods that the python chess library has to offer, specifically with the chess.engine package.

Information can be found here - https://python-chess.readthedocs.io/en/latest/engine.html#reference

Examples:
Let Stockfish play against itself, 100 milliseconds per move.

Protocol for communicating with a chess engine process.
    Parameters:
    board – The position to analyse. The entire move stack will be sent to the engine.

    limit – An instance of chess.engine.Limit that determines when to stop the analysis.

    multipv – Optional. Analyse multiple root moves. Will return a list of at most multipv dictionaries rather than just a single info dictionary.

    game – Optional. An arbitrary object that identifies the game. Will automatically inform the engine if the object is not equal to the previous game (e.g.,      ucinewgame, new).

    info – Selects which information to retrieve from the engine. INFO_NONE, INFO_BASE (basic information that is trivial to obtain), INFO_SCORE, INFO_PV, INFO_REFUTATION, INFO_CURRLINE, INFO_ALL or any bitwise combination. Some overhead is associated with parsing extra information.

    root_moves – Optional. Limit analysis to a list of root moves.

    options – Optional. A dictionary of engine options for the analysis. The previous configuration will be restored after the analysis is complete. You can permanently apply a configuration with configure().
    
Stream information from the engine and stop on an arbitrary condition.
