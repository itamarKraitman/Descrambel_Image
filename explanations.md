To solve this assignment, I used image processing tools using openCV library, alongside with numPy and sqllite3.
<br>Firstly, I created a connection the SQLite database, and retrieve all the rows (tiles) in form of list of tuples, where each tuple is a tile.
I did not make any manipulations (order by and such) because I noticed that the destination x and y coordinates are originally organized in ascending order,
so iterating over the list is efficient enough.
<br>Secondly, for each tile, I seperated source, destination coordinates, and rotation from each other. Then captured the tile **itself**
from the scrambled image using numpy indexing, rotate it to the original image angle, and place it in the descrambled image.

