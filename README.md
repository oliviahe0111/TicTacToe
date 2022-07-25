# TicTacToe

## 1. Tic Tac Toe Python GUI application using Pygame (tictactoeApp.py)
- Two players can take turn place their chess (O or X) in order to complete a row, a column, or a diagonal with either three O's or three X's
- Players can easily place their chess by simply click in the position they want to place in by clicking any spaces of the grid of nine squares
- Players can restart the game using the "R" key on the key board


### Start View
<img alt="Screen Shot 2022-07-12 at 8 49 01 PM" src="https://user-images.githubusercontent.com/67666346/178646594-c6773c24-0f64-4d53-ad62-2b19e2812b81.png" width="200" height="200">

### Circle Wins
<img alt="image" src="https://user-images.githubusercontent.com/67666346/178646126-3a6f7313-1186-4b79-8ac9-564d21022d03.png" width="200" height="200">

### Cross Wins
<img alt="image" src="https://user-images.githubusercontent.com/67666346/178646800-6fd3325c-8db5-40fa-a911-b3b056ca51a4.png" width="200" height="200">

## 2. Console based Tic Tac Toe game
There are two verstions: Players can either play against another player or play against the computer.

### Mode 1. Console based unbeatable AI vs. human player Tic Tac Toe game using python (playWithAi.py)
- Players can choose to start the game or let the AI start the game.
<img width="488" alt="Screen Shot 2022-07-24 at 11 42 33 PM" src="https://user-images.githubusercontent.com/67666346/180714407-2bf272ec-c437-4be0-9d51-e30a1f74c4d5.png">

- The AI uses the Minimax algorithm to play against the player. The ending will either be the AI winning the game or the human player has successfully stopped the AI from winning the game and leading to a tie.

Win:<br />
<img width="97" alt="Screen Shot 2022-07-24 at 11 36 51 PM" src="https://user-images.githubusercontent.com/67666346/180714216-12e6ee30-ea3e-4dcb-ac34-6651a9da24cd.png">
<br />
Tie: <br />
<img width="371" alt="Screen Shot 2022-07-25 at 12 00 29 AM" src="https://user-images.githubusercontent.com/67666346/180717152-2372973f-8262-4b94-9c7e-9b68a29b3b88.png">


### Mode 2. Console based Tic Tac Toe game using python (main.py)
- Players can customize their user names at the start of the game.
- Players can place their chess by simply enter a number from 1 to 9 according to the grid of nine squares they want to put their chess in.

<img width="359" alt="Screen Shot 2022-07-12 at 9 02 27 PM" src="https://user-images.githubusercontent.com/67666346/178647998-0f891c20-b96a-40dd-acdb-e14a7381dfa9.png">

- Error message will pop out if a user tries to obtain a taken position.
<img width="394" alt="image" src="https://user-images.githubusercontent.com/67666346/178648212-dfc006cb-92e9-4295-ac97-9382c17c0af4.png">

- Error message will also pop out if a user enters number or anything beside 1 to 9.
<img width="385" alt="Screen Shot 2022-07-12 at 9 06 27 PM" src="https://user-images.githubusercontent.com/67666346/178648428-4f1062dc-3932-4f77-86b9-cfb764e3888d.png">


### References
1. Basic console based Tic Tac Toe in Python : https://www.youtube.com/watch?v=BHh654_7Cmw
2. Using Pygame to make a GUI for the game: https://www.youtube.com/watch?v=pc7XhHxSgrM
3. Using Minimax algorithm to make an un beatable AI opponent for human player: https://www.youtube.com/watch?v=JC1QsLOXp-I
