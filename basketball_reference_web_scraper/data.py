from enum import Enum


class Location(Enum):
    HOME = "HOME"
    AWAY = "AWAY"


class Outcome(Enum):
    WIN = "WIN"
    LOSS = "LOSS"


class Team(Enum):
    ATLANTA_HAWKS = "ATLANTA HAWKS"
    BOSTON_CELTICS = "BOSTON CELTICS"
    BROOKLYN_NETS = "BROOKLYN NETS"
    CHARLOTTE_HORNETS = "CHARLOTTE HORNETS"
    CHICAGO_BULLS = "CHICAGO BULLS"
    CLEVELAND_CAVALIERS = "CLEVELAND CAVALIERS"
    DALLAS_MAVERICKS = "DALLAS MAVERICKS"
    DENVER_NUGGETS = "DENVER NUGGETS"
    DETROIT_PISTONS = "DETROIT PISTONS"
    GOLDEN_STATE_WARRIORS = "GOLDEN STATE WARRIORS"
    HOUSTON_ROCKETS = "HOUSTON ROCKETS"
    INDIANA_PACERS = "INDIANA PACERS"
    LOS_ANGELES_CLIPPERS = "LOS ANGELES CLIPPERS"
    LOS_ANGELES_LAKERS = "LOS ANGELES LAKERS"
    MEMPHIS_GRIZZLIES = "MEMPHIS GRIZZLIES"
    MIAMI_HEAT = "MIAMI HEAT"
    MILWAUKEE_BUCKS = "MILWAUKEE BUCKS"
    MINNESOTA_TIMBERWOLVES = "MINNESOTA TIMBERWOLVES"
    NEW_ORLEANS_PELICANS = "NEW ORLEANS PELICANS"
    NEW_YORK_KNICKS = "NEW YORK KNICKS"
    OKLAHOMA_CITY_THUNDER = "OKLAHOMA CITY THUNDER"
    ORLANDO_MAGIC = "ORLANDO MAGIC"
    PHILADELPHIA_76ERS = "PHILADELPHIA 76ERS"
    PHOENIX_SUNS = "PHOENIX SUNS"
    PORTLAND_TRAIL_BLAZERS = "PORTLAND TRAIL BLAZERS"
    SACRAMENTO_KINGS = "SACRAMENTO KINGS"
    SAN_ANTONIO_SPURS = "SAN ANTONIO SPURS"
    TORONTO_RAPTORS = "TORONTO RAPTORS"
    UTAH_JAZZ = "UTAH JAZZ"
    WASHINGTON_WIZARDS = "WASHINGTON WIZARDS"

    # DEPRECATED TEAMS
    CHARLOTTE_BOBCATS = "CHARLOTTE BOBCATS"
    NEW_JERSEY_NETS = "NEW JERSEY NETS"
    NEW_ORLEANS_HORNETS = "NEW ORLEANS HORNETS"
    NEW_ORLEANS_OKLAHOMA_CITY_HORNETS = "NEW ORLEANS/OKLAHOMA CITY HORNETS"
    SEATTLE_SUPERSONICS = "SEATTLE SUPERSONICS"
    VANCOUVER_GRIZZLIES = "VANCOUVER GRIZZLIES"


class OutputType(Enum):
    JSON = "JSON"
    CSV = "CSV"


class OutputWriteOption(Enum):
    WRITE = "w"
    CREATE_AND_WRITE = "w+"
    APPEND = "a"
    APPEND_AND_WRITE = "a+"