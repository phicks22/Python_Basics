from Model.Shark import Shark
from Model.Snake import Snake
from Model.Snail import Snail
from Animal_Containers.Sharks import Sharks
from Animal_Containers.Snakes import Snakes
from Animal_Containers.Snails import Snails

# Sharks:
horn = Shark('Horn Shark', 'Heterodontus', 'francisci', 4.0, 25, 'Temperate')
swell = Shark('Swell Shark', 'Cephaloscyllium', 'ventriosum', 3.5, 10, 'Temperate')
white = Shark('Great White Shark', 'Carcharadon', 'carcharias', 20.0, 70, 'Temperate/Tropical')
shortfin_mako = Shark('Shortfin Mako', 'Isurus', 'oxyrinchus', 12.0, 30, 'Temperate')
longfin_mako = Shark('Longfin Mako', 'Isurus', 'paucus', 14.0, 'Unknown', 'Temperate')
lemon = Shark('Lemon Shark', 'Negaprion', 'bevriostris', 11.0, 27, 'Tropical')
bull = Shark('Bull Shark', 'Carcharhinus', 'leucas', 11.5, 14, 'Tropical/Fresh')
great_hammer = Shark('Great Hammerhead Shark', 'Sphyrna', 'mokarran', 20.0, 35, 'Tropical')
nurse = Shark('Nurse Shark', 'Ginglymostoma', 'cirratum', 14.0, 35, 'Tropical')
porbeagle = Shark('Porbeagle Shark', 'Lamna', 'nasus', 6.6, 65, 'Temperate')
black_tip = Shark('Blacktip Reef Shark', 'Carcharhinus', 'melanopterus', 5.2, 13, 'Tropical')

# Snakes:
corn = Snake('Corn Snake', 'Pantherophis', 'guttatus', 6.0, 8, False)
ball_python = Snake('Ball Python', 'Python', 'regius', 6.0, 30, False)
blk_king = Snake('Mexican Black King Snake', 'Lampropeltis', 'getula nigrita', 5.0, 30, True)

# Snails:
moon = Snail('Moon Snail', 'Neverita', 'reclusiana', 5.5, 7, False)
unicorn = Snail('Angular Unicorn', 'Acanithucella', 'spirata', 'Unknown', 'Unknown', True)
kellets = Snail('Kellet\'s Welk', 'Kelletia', 'keletii', 6.9, 50, False)
chestnut = Snail('Chestnut Cowrie', 'Neobernaya', 'spadicia', 2.6, 'Unknown', True)


print('Sharks:')

sharks = [horn, swell, white, shortfin_mako, longfin_mako, lemon, bull, great_hammer, nurse, porbeagle, black_tip]
shark_object = Sharks(sharks)
shark_object.print_all_sharks()

print('\n')
print('Snakes:')
snakes = [corn, ball_python, blk_king]
snake_object = Snakes(snakes)
snake_object.print_all_snakes()

print('\n')
print('Snails:')
snails = [moon, unicorn,kellets,chestnut]
snail_object = Snails(snails)
snail_object.print_all_snails()