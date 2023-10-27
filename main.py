import cells.cellfunctions as cfuncs
gamepanel = cfuncs.boardFuncs.nonIntBoardFuncs() and cfuncs.boardFuncs.intBoardFuncs()
game65536 = cfuncs.gameFuncs.nonIntGameFuncs(gamepanel) and cfuncs.gameFuncs.intGameFuncs(gamepanel)
game65536.start()
