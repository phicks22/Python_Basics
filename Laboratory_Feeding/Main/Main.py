from Model.Shark import Shark
from Model.Snake import Snake
from Animal_Containers.Sharks import Sharks
from Animal_Containers.Snakes import Snakes

# Sharks:
horn = Shark('Horn Shark', 'Heterodontus', 'francisci', 4.0, 25)
swell = Shark('Swell Shark', 'Cephaloscyllium', 'ventriosum', 3.5, 10)
white = Shark('Great White Shark', 'Carcharadon', 'carcharias', 20.0, 70)
shortfin_mako = Shark('Shortfin Mako', 'Isurus', 'oxyrinchus', 12.0, 30)
longfin_mako = Shark('Longfin Mako', 'Isurus', 'paucus', 14.0, 'Unknown')
lemon = Shark('Lemon Shark', 'Negaprion', 'bevriostris', 11.0, 27)
bull = Shark('Bull Shark', 'Carcharhinus', 'leucas', 11.5, 14)
great_hammer = Shark('Great Hammerhead Shark', 'Sphyrna', 'mokarran', 20.0, 35)
nurse = Shark('Nurse Shark', 'Ginglymostoma', 'cirratum', 14.0, 35)
porbeagle = Shark('Porbeagle Shark', 'Lamna', 'nasus', 6.6, 65)
black_tip = Shark('Blacktip Reef Shark', 'Carcharhinus', 'melanopterus', 5.2, 13)

# Snakes:
corn = Snake('Corn Snake', 'Pantherophis', 'guttatus', 6.0, 8)
ball_python = Snake('Ball Python', 'Python', 'regius', 6.0, 30)
blk_king = Snake('Mexican Black King Snake', 'Lampropeltis', 'getula nigrita', 5.0, 30)


print('Sharks:')

sharks = [horn, swell, white, shortfin_mako, longfin_mako, lemon, bull, great_hammer, nurse, porbeagle, black_tip]
shark_object = Sharks(sharks)
shark_object.print_all_sharks()

print('\n')
print('Snakes:')
snakes = [corn, ball_python, blk_king]
snake_object = Snakes(snakes)
snake_object.print_all_snakes()

