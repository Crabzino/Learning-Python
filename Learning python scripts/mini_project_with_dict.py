#I own a game store and i am hosting a game night for a game called abruptly goblins


gamers = []

def add_gamer(gamer, gamers_list):
    if isinstance(gamer, dict) and "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)
    else:
        print("Gamer missing information")
    return gamers_list

kimberly = {"name": "kimberly", "availability": ["Mondays", "Tuesdays", "Fridays"]}
#thomas = {"name": "thomas", "availability": ["Tuesday", "Thursday", "Saturday"]}

add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
#print(gamers)


def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

count_availability = build_daily_frequency_table()
#print(count_availability)

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            if day in count_availability:
                count_availability[day] += 1
        
    return available_frequency
    
calculate_availability(gamers, count_availability)
#print(count_availability)



def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_availability = availability
            best_day = day
    return best_day

game_night = find_best_night(count_availability)
print(game_night)



def available_on_night(gamers_list, day):
    gamers_available_on_night = []
    for gamer in gamers_list:
        for availability in gamer["availability"]:
            if availability == day:
                gamers_available_on_night.append(gamer["name"])
    return gamers_available_on_night

attending_game_night = available_on_night(gamers, game_night)


#OR CAN BE DONE LIKE THIS, HOWEVER PRINTS OUT THE WHOLE LIST OF THE PEOPLE WHO ARE AVAILABLE,NOT JUST THE NAME
#def available_on_night(gamers_list, day):
    #return [gamer for gamer in gamers_list if day in gamer['availability']]

#attending_game_night = available_on_night(gamers, game_night)

#print(attending_game_night)



form_email = """
Dear {name},

I am happy to inform you that the day of the {game} game night shall occur on
{day_of_week}. Feel free to come by and we will all play.

Regards,
The Sorcery Society
"""


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, game=game, day_of_week=day))

#send_email(attending_game_night, game_night, "Abruptly Goblins")


