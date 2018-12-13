use_sample_input = False
input_path = 'day13_sample.txt' if use_sample_input else 'day13_input.txt'

inpstr = open(input_path).read()

grid = [[c for c in line] for line in inpstr.splitlines()]

#59, 143
#19, 11
#7, 35
#7, 34

mapping = {
    '^/': '>',
    '^\\': '<',
    'v/': '<',
    'v\\': '>',
    '</': 'v',
    '<\\': '^',
    '>/': '^',
    '>\\': 'v',
    '^L': '<',
    '^R': '>',
    'vL': '>',
    'vR': '<',
    '<L': 'v',
    '<R': '^',
    '>L': '^',
    '>R': 'v'
}

def display_grid(grid):
    print('\n'.join(''.join(str(c) for c in line) for line in grid))

def make_cart(grid):
    class Cart():
        grid = grid
        direction = ['L', 'S', 'R']
        def __init__(self, state, coordinates):
            assert state in '^v<>'
            self.state = state
            self.position = coordinates
            if state in '^v':
                self.stepping_on = '|'
            elif state in '<>':
                self.stepping_on = '-'
            self.turn = 0

        def step(self):
            
            if self.state == 'X':
                return 
            y, x = self.position
            if self.state == '^':
                self.position[0] -= 1
            elif self.state == 'v':
                self.position[0] += 1
            elif self.state == '<':
                self.position[1] -= 1
            elif self.state == '>':
                self.position[1] += 1
                        
            newy, newx = self.position
            self.stepping_on, self.grid[y][x], self.grid[newy][newx] = self.grid[newy][newx], self.stepping_on, self
            
            if isinstance(self.stepping_on, Cart):
                
                self.state = 'X'
                othercart = self.stepping_on
                othercart.state = 'X'
                y, x = self.position
                self.grid[y][x] = othercart.stepping_on
                return

            if self.stepping_on in '|-':
                return 

            if self.stepping_on == '+':
                direction = self.direction[self.turn % len(self.direction)]
                self.turn += 1
                if direction == 'S':
                    return 
            elif self.stepping_on in '/\\':
                direction = self.stepping_on
            self.state = mapping[self.state+direction]
            
        def __eq__(self, other):
            if isinstance(other, Cart):
                return self.state == other.state
            else:
                return self.state == other
        
        def __repr__(self):
            return self.state
    return Cart

Cart = make_cart(grid)


def setup_grid(grid):
    carts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] in '^v<>':
                c = Cart(grid[i][j], coordinates =[i,j])
                grid[i][j] = c
                carts.append(c)
    return grid, carts

def find_carts(grid):
    carts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if isinstance(grid[i][j], Cart):
                carts.append(grid[i][j])
    return carts

grid, carts = setup_grid(grid)

flag = 1

while sum(c != 'X' for c in carts) > 1 :
    for cart in carts:
        cart.step()
        
        #Print the answer to Part 1
        if cart == 'X' and flag:            
            y, x = cart.position
            print(x,y)
            flag = 0
    carts = find_carts(grid)



#Print the answer to part 2
y,x = cart.position
print(x,y)