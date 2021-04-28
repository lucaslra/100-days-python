from models import RollType

results = {
    RollType.ROCK: {
        RollType.ROCK: 0,
        RollType.PAPER: -1,
        RollType.SCISSORS: 1
    },
    RollType.PAPER: {
        RollType.ROCK: 1,
        RollType.PAPER: 0,
        RollType.SCISSORS: -1
    },
    RollType.SCISSORS: {
        RollType.ROCK: -1,
        RollType.PAPER: 1,
        RollType.SCISSORS: 0
    }
}
