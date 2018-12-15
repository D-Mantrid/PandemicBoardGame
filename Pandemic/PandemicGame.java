
/**
 * This is the main class of my pandemic game project.
 * 
 * @author Joe Salmon
 * @version 04.12.2018
 */
public class PandemicGame
{
    public static void main(String[] args)
	{
        System.out.println("starting new game type " + args[0]);
        switch (Integer.parseInt( args[0]) )
        {
            case 0:
            makeType0Game();        
            break;

            case 1:
            makeType1Game();
            break;

            case 2:
            makeType2Game();
            break;
        }
    }

    public static void makeType2Game()
    {
    	PandemicGame testgame;
    	Player jesus;
    	Player beyonce;
        Player susan;
        Player deadpool;
        beyonce = new Player("Beyonce",3);
        jesus = new Player("Jesus",3);
        Player[] currentPlayers;
        currentPlayers = new Player[2];
        currentPlayers[0] = jesus;
        currentPlayers[1] = beyonce;
        
        int[] infectRate;
        infectRate = new int[13];
        infectRate[0] = 2;
        infectRate[1] = 2;
        infectRate[2] = 2;
        infectRate[3] = 3;
        infectRate[4] = 3;
        infectRate[5] = 4;
        infectRate[6] = 4;
        infectRate[7] = 4;
        infectRate[8] = 4;
        infectRate[9] = 5;
        infectRate[10] = 5;
        infectRate[11] = 5;
        infectRate[12] = 6;
        
        int[] initalInfect;
        initalInfect = new int[3];
        initalInfect[0] = 3;
        initalInfect[1] = 3;
        initalInfect[2] = 3;
        int colours;
        colours = 4;
        int cure;
        cure = 1;
        int epidemics;
        epidemics = 5;
        testgame = new PandemicGame(currentPlayers, colours, cure,epidemics, infectRate, 8, initalInfect, 15,7,1,"/home/joe/Git/PandemicBoardGame/Pandemic/cities.csv");
    
        testgame.playGame();
    }
    public static void makeType1Game()
    {
    	PandemicGame testgame;
    	Player jesus;
    	Player beyonce;
        Player susan;
        Player deadpool;
        beyonce = new Player("Beyonce",0);
        jesus = new Player("Jesus",1);
        Player[] currentPlayers;
        currentPlayers = new Player[2];
        currentPlayers[0] = jesus;
        currentPlayers[1] = beyonce;
        
        int[] infectRate;
        infectRate = new int[13];
        infectRate[0] = 2;
        infectRate[1] = 2;
        infectRate[2] = 2;
        infectRate[3] = 3;
        infectRate[4] = 3;
        infectRate[5] = 4;
        infectRate[6] = 4;
        infectRate[7] = 4;
        infectRate[8] = 4;
        infectRate[9] = 5;
        infectRate[10] = 5;
        infectRate[11] = 5;
        infectRate[12] = 6;
        
        int[] initalInfect;
        initalInfect = new int[3];
        initalInfect[0] = 3;
        initalInfect[1] = 3;
        initalInfect[2] = 3;
        int colours;
        colours = 4;
        int cure;
        cure = 1;
        int epidemics;
        epidemics = 5;
        testgame = new PandemicGame(currentPlayers, colours, cure,epidemics, infectRate, 8, initalInfect, 15,7,1,"/home/joe/Git/PandemicBoardGame/Pandemic/cities.csv");
    
        testgame.playGame();
    }
    

    public static void makeType0Game()
    {
    	PandemicGame testgame;
    	Player jesus;
    	Player beyonce;
        Player susan;
        Player deadpool;
        beyonce = new Player("Beyonce",0);
        jesus = new Player("Jesus",0);
        Player[] currentPlayers;
        currentPlayers = new Player[2];
        currentPlayers[0] = jesus;
        currentPlayers[1] = beyonce;
        
        int[] infectRate;
        infectRate = new int[13];
        infectRate[0] = 2;
        infectRate[1] = 2;
        infectRate[2] = 2;
        infectRate[3] = 3;
        infectRate[4] = 3;
        infectRate[5] = 4;
        infectRate[6] = 4;
        infectRate[7] = 4;
        infectRate[8] = 4;
        infectRate[9] = 5;
        infectRate[10] = 5;
        infectRate[11] = 5;
        infectRate[12] = 6;
        
        int[] initalInfect;
        initalInfect = new int[3];
        initalInfect[0] = 3;
        initalInfect[1] = 3;
        initalInfect[2] = 3;
        int colours;
        colours = 4;
        int cure;
        cure = 5;
        int epidemics;
        epidemics = 5;
        testgame = new PandemicGame(currentPlayers, colours, cure,epidemics, infectRate, 8, initalInfect, 9,7,1,"/home/joe/Git/PandemicBoardGame/Pandemic/cities.csv");
    
        testgame.playGame();
    }

    // The Game Board contains all the objects of the game.
    public GameBoard gameBoard;
    
    // An array of the players who are playing
    public Player[] gamePlayers;
    
    // boolean attributes which indicae if the game is won or lost.
    public boolean gameOver;
    public boolean gameWon;
    public boolean gameLost;
    
    /**
     * adjustable features of the game that is set up, including
     * numberColours - number of colours of disease played with.
     * requiredForCure- the number of cards which must be discarded to cure a disease.
     * infectionRateSetting - the arrary of values needed for the infection rate.
     * maximumOutbreaks - the maximum number of outbreaks that can happen before the game is lost.
     * initalInfectionStep - an array whch provides the number of cities to get 1, 2 and 3 cubes initally.
     * cardsDrawnInitally - the number of cards drawn between the players at the start of the game.
     * maximumHandSize - The maximum handsize of the players.
     */ 

    public int numberColours;
    public int requiredForCure;
    public int[] infectionRateSetting;
    public int maximumOutbreaks;
    public int numberEpidemics;
    public int[] initalInfectionStep;
    public int cardsDrawnInitally;
    public int availableResearchStation;
    public int initalResearchStation;
    public String mapLocation;

    /**
     * This constructor for a Pandemic game creates a new instance of a GameBoard object called GameBoard with the given adjustable features of the game.
     * It requires an array of players to be provided.
     */
    public PandemicGame(Player[] currentGamePlayers, int currentNumberColours, int currentRequiredForCure, 
    int numberEpidemics, int[] currentInfectionRateSetting, int currentMaximumOutbreaks, int[] currentInitalInfectionStep, 
    int currentCardsDrawnInitally, int currentAvailableResearchStation, int currentInitalResearchStation, String currentMapLocation)
    {
        System.out.println("Setting up a new game of pandemic with the below features.");
        System.out.println(currentNumberColours + " Colours of disease.");
        System.out.println(currentRequiredForCure + " cards of the same colour must be discarded at a research station to cure a disease.");
        requiredForCure = currentRequiredForCure;
        System.out.println(numberEpidemics + " is the maximum number of epidemics.");
        System.out.println("The infection rate will develop in as such;- " + currentInfectionRateSetting[0] + currentInfectionRateSetting[1] +
        + currentInfectionRateSetting[2] + + currentInfectionRateSetting[3] + currentInfectionRateSetting[4] + ".");
        infectionRateSetting = currentInfectionRateSetting;
        System.out.println("Any more than " + currentMaximumOutbreaks + " outbreaks and the game will be lost");
        maximumOutbreaks = currentMaximumOutbreaks;
        System.out.println("The inital infection step will see " + currentInitalInfectionStep[0] + currentInitalInfectionStep[1] + 
                            currentInitalInfectionStep[2] + " cities infected ");
        initalInfectionStep = currentInitalInfectionStep;
        System.out.println("Between all players a maximum of " + currentCardsDrawnInitally + " cards are drawn at start of the game");
        cardsDrawnInitally = currentCardsDrawnInitally;
        System.out.println("There are " + currentAvailableResearchStation + " research stations which can be placed, and " + currentInitalResearchStation + 
                            " (min 1) are placed at the start of the game");
        System.out.println("Setting map location to " + currentMapLocation);
        
        mapLocation = currentMapLocation;
                            
        // initialise instance variables
        int startingHandSize;
        
        gameBoard = new GameBoard(currentNumberColours, infectionRateSetting,requiredForCure, numberEpidemics, currentInitalResearchStation, currentAvailableResearchStation, mapLocation);
        gamePlayers = currentGamePlayers;
        numberColours = currentNumberColours;
        requiredForCure = currentRequiredForCure;
        // sets the players to the gameboard
        sitPlayersDown();
        gameBoard.startGame(initalInfectionStep);
        startingHandSize = calcHandSize(cardsDrawnInitally);
        drawHands(startingHandSize);
        placePieces();
        gameBoard.shuffleInEpidemics(numberEpidemics);
        gameOver = false;        
    }
    
    public void playGame()
    {
        int i;
        int turns = 0;
        while (gameOver == false)
        {
            i = gamePlayers.length;
            while (i > 0 && !gameOver)
            {
                i = i -1;
                while (gamePlayers[i].getPlayerAction() > 0 && !gameOver)
                {
                
                    //here is where an action should happen
                    // System.out.println("Chance for action here!");
                    gamePlayers[i].makeDecision();
                    checkGameOver();
               }
                if (!checkGameOver())
                {
                    System.out.println(gamePlayers[i].getPlayerName() + " completed 4 actions");
                    gamePlayers[i].drawCard(2);
                    gameBoard.infectCityPhase(gameBoard.getInfectionRate());
                }
                checkGameOver();
            }
            turns++;
            if (!checkGameOver())
            {
                System.out.println("Ending turn " + turns + " everybody has had a go.");
            }
            resetAllPlayerAction();
        }
    }
    
    public void startOfTurnActions()
    {
    }
   
    public boolean checkGameOver()
    {
        if (checkGameWon())
        {
            for (int i = 0 ; i < 5 ; i++)
            {
                System.out.println("YOU WIN!!!");
            }

            gameOver = true;
        }
        checkGameLost();
        return gameOver;
    }
    
    // checks if the game is lost
    public void checkGameLost()
    {
        if (gameBoard.getOutbreakCount()>maximumOutbreaks)
        {
            System.out.println("game over, too many outbreaks!");
            gameLost = true;
            gameOver = true;
            looserPrint();            
        }
        else if (gameBoard.emptyDeck())
        {
            System.out.println("That's it game over, no more cards.");
            gameLost = true;
            gameOver = true;
            looserPrint();
        }
    }
    
    // Prints looser
    public void looserPrint()
    {
        for (int i = 0 ; i < 5 ; i++)
        {
            System.out.println("YOU GUYS SUCK AT THIS GAME!!");
        }
        
    }
    
    // sets all players actions back to 4
    public void resetAllPlayerAction()
    {
        int i = gamePlayers.length;
        while (i > 0)
        {
            i--;
            gamePlayers[i].resetPlayerAction();
        }
    }
    
    
    public void placePieces()
    {
        int i = gamePlayers.length;
        while (i > 0)
        {
            // placing pieces
            // System.out.println("Placing a piece for " + gamePlayers[i-1].getPlayerName());
            gameBoard.playerPieces[i-1] = new Piece(gamePlayers[i-1], gameBoard, gameBoard.researchCentres[0].getLocation());
            // System.out.println("making sure they know the piece is their piece!");
            gamePlayers[i-1].setPlayerPiece(gameBoard.playerPieces[i-1]);
            i = i -1;
        }
    }
    
    // calculates hand size based on number of players
    public int calcHandSize(int initalCardsDrawn)
    {
        int i = gamePlayers.length;
        return initalCardsDrawn/i;
    }
    
    public void drawHands(int handSize)
    {
        int i = gamePlayers.length;
        while (i > 0)
        {
            System.out.println("drawing hand for " + gamePlayers[i-1].getPlayerName());
            gamePlayers[i-1].drawCard(handSize);
            i = i -1;
        }
    }
    
    public boolean checkGameWon()
    {
        boolean isWon=true;
        for (int i = 0 ; i <gameBoard.diseases.length ; i ++)
        {
            isWon = isWon && gameBoard.diseases[i].getCured();
        }
        gameWon= isWon;
        return isWon;
    }
    
    
    

    public void sitPlayersDown()
    {
        int i = gamePlayers.length;
        while (i > 0)
        {
            System.out.println(gamePlayers[i-1].getPlayerName() + " has joined the game");
            gamePlayers[i-1].setGameBoard(gameBoard);
            i = i -1;
        }
    }
}
