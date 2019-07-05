import sys

mines = []
destroyed_mines = []
ship_cordinate = []
x_axis_length_of_field = 0
y_axis_length_of_field = 0

def find_mines(field_file):
    global x_axis_length_of_field
    global y_axis_length_of_field
    input_list = field_file.split("\n")
    if '' in input_list:
        input_list.remove('')
    
    y_cordinate = 0
    for row in input_list:
        x_cordinate = 0
        for element in row:
            if element != '.':
                z_cordinate = None
                if ord(element) < 91 and ord(element) > 64:
                    z_cordinate = ord(element) - 38
                elif ord(element) < 123 and ord(element) > 96:
                    z_cordinate = ord(element) - 96
                mines.append([x_cordinate, y_cordinate, z_cordinate * (-1)])
            x_cordinate += 1
        x_axis_length_of_field = x_cordinate
        y_cordinate += 1
    y_axis_length_of_field = y_cordinate
    ship_cordinate.append(int(x_axis_length_of_field/2))
    ship_cordinate.append(int(y_axis_length_of_field/2))
    ship_cordinate.append(0)

def read_field_file():
    with open(sys.argv[1], 'r') as my_file:
        return my_file.read()

def read_script_file():
    with open(sys.argv[2], 'r') as my_file:
        return my_file.read()

def find_mines_for_plan(x_cordinate, y_cordinate):
    mines_to_destroy = []
    for mine in mines:
        if mine[0] == x_cordinate and mine[1] == y_cordinate:
            mines_to_destroy.append(mine)
    return mines_to_destroy

def destroy_mine(mines_to_destroy):
    for mine in mines:
        if mine == mines_to_destroy:
            mines.remove(mine)
            destroyed_mines.append(mine)

def increase_mines_cordinates(x, y):
    for mine in mines:
        mine[0] += x
        mine[1] += y
        mine[2] += 1

def decrease_mines_cordinates(x, y):
    for mine in mines:
        mine[0] -= x
        mine[1] -= y
        mine[2] += 1

def initialize_fire_points():
    fire_x = ship_cordinate[0]
    fire_y = ship_cordinate[1]
    return fire_x, fire_y

def execute_command(command):

    global x_axis_length_of_field
    global y_axis_length_of_field

    if command.lower() == "alpha":            
        alpha_cordinates = []

        fire_x, fire_y = initialize_fire_points()
        while(fire_x > 0 and fire_y > 0):
            fire_x = fire_x - 1
            fire_y = fire_y - 1
            alpha_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_x > 0 and fire_y < y_axis_length_of_field):
            fire_x = fire_x - 1
            fire_y = fire_y + 1
            alpha_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_x < x_axis_length_of_field and fire_y > 0):
            fire_x = fire_x + 1
            fire_y = fire_y - 1
            alpha_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_x < x_axis_length_of_field and fire_y < y_axis_length_of_field):
            fire_x = fire_x + 1
            fire_y = fire_y + 1
            alpha_cordinates.append([fire_x, fire_y])   
        for alpha_cordinate in alpha_cordinates:
            mines_to_destroy = find_mines_for_plan(alpha_cordinate[0], alpha_cordinate[1])
            for mine in mines_to_destroy:
                destroy_mine(mine)

    if command.lower() == "beta":
        beta_cordinates = []

        fire_x, fire_y = initialize_fire_points()
        while(fire_x > 0):
            fire_x = fire_x - 1
            beta_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_y > 0):
            fire_y = fire_y - 1
            beta_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_y < y_axis_length_of_field):
            fire_y = fire_y + 1
            beta_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_x < x_axis_length_of_field):
            fire_x = fire_x + 1
            beta_cordinates.append([fire_x, fire_y])

        for beta_cordinate in beta_cordinates:
            mines_to_destroy = find_mines_for_plan(beta_cordinate[0], beta_cordinate[1])
            for mine in mines_to_destroy:
                destroy_mine(mine)

    if command.lower() == "gamma":
        gamma_cordinates = []

        fire_x, fire_y = initialize_fire_points()
        while(fire_x > 0):
            fire_x = fire_x - 1
            gamma_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        gamma_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_x < x_axis_length_of_field):
            fire_x = fire_x + 1
            gamma_cordinates.append([fire_x, fire_y])
 
        for gamma_cordinate in gamma_cordinates:
            mines_to_destroy = find_mines_for_plan(gamma_cordinate[0], gamma_cordinate[1])
            for mine in mines_to_destroy:
                destroy_mine(mine)

    if command.lower() == "delta":
        delta_cordinates = []

        fire_x, fire_y = initialize_fire_points()
        while(fire_y > 0):
            fire_y = fire_y - 1
            delta_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        delta_cordinates.append([fire_x, fire_y])

        fire_x, fire_y = initialize_fire_points()
        while(fire_y < y_axis_length_of_field):
            fire_y = fire_y + 1
            delta_cordinates.append([fire_x, fire_y])

        for delta_cordinate in delta_cordinates:
            mines_to_destroy = find_mines_for_plan(delta_cordinate[0], delta_cordinate[1])
            for mine in mines_to_destroy:
                destroy_mine(mine)

    if command.lower() == "north":
        ship_cordinate[1] += 1
        increase_mines_cordinates(2,0)
        x_axis_length_of_field = x_axis_length_of_field +2

    if command.lower() == "south":
        ship_cordinate[1] -= 1
        decrease_mines_cordinates(2,0)
        x_axis_length_of_field = x_axis_length_of_field - 2
   
    if command.lower() == "west":
        ship_cordinate[0] += 1
        increase_mines_cordinates(0,2)
        y_axis_length_of_field = y_axis_length_of_field + 2

    if command.lower() == "east":
        ship_cordinate[1] -= 1
        decrease_mines_cordinates(0,2)
        y_axis_length_of_field = y_axis_length_of_field - 2

def get_character_for_mine(mine_int):
    mine_int = mine_int * (-1)
    if mine_int > 0 and mine_int < 27:
        mine_int += 96
    elif mine_int > 26 and mine_int < 53:
        mine_int += 38
    else:
        mine_int = 42
    return chr(mine_int)

def print_updated_field_input(command_list):

    global x_axis_length_of_field
    global y_axis_length_of_field

    mine_x = 0
    mine_y = 0
    for command in command_list:
        if command == 'south':
            mine_x = mine_x - 2
        elif command == 'north':
            mine_x = mine_x + 2
        elif command == 'east':
            mine_y = mine_y - 2
        elif command == 'west':
            mine_y = mine_y + 2 

    for x in range(x_axis_length_of_field):
        row = ''
        for y in range(y_axis_length_of_field ):
            mine_found = [mine for mine in mines if (mine[0] == x and mine[1] == y)]
            if mine_found:
                row = row + get_character_for_mine(mine_found[0][2])
            else:
                row = row + '.'
        print(row)
    print("\n")

def main():
    field_file = read_field_file()
    script_file = read_script_file()
    find_mines(field_file)
    command_rows = script_file.split('\n')
    total_mines = len(mines)
    step = 1
    previous_command = []
    for row in command_rows:
        if len(mines) == 0:
            break;
        command_list = row.split(" ")
        print("Step: {} \n".format(step))
        print_updated_field_input(previous_command)
        print(row, "\n")

        for command in command_list:
            execute_command(command)

        step += 1
        ship_cordinate[2] -= 1

        print_updated_field_input(command_list)
        previous_command = command_list

    print("total mines:", total_mines)
    print("destroyed mines:", len(destroyed_mines))
    print("total Steps Taken:", step - 1, "\n")
    # print("")
    print("Remaining Mines:" ,(total_mines-len(destroyed_mines)))

if __name__ == '__main__':
    main()