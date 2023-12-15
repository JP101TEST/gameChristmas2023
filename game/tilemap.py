
class Tilemap:
    def __init__(self,pos,size,type):
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.height = size[0]
        self.width = size[1]
        self.type = type

    def get_pos_x(self):
        return self.pos_x
    
    def get_pos_y(self):
        return self.pos_y

    def set_pos_x(self, new_pos_x):
        self.pos_x = new_pos_x
    
    def set_pos_y(self, new_pos_y):
        self.pos_y = new_pos_y

    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
    
    def get_PS(self):
        return (self.pos_y, self.pos_x, self.height, self.width)
    
    def get_type(self):
        return self.type
    

# # Writing the tilemap to a file
# with open("tilemap.txt", "w") as file:
#     for row in tilemap:
#         line = " ".join(map(str, row)) + "\n"
#         file.write(line)

# read_tilemap = []

# with open("tilemap.txt", "r") as file:
#     for line in file:
#         # Split the line into individual numbers and convert them to integers
#         row = list(map(int, line.strip().split()))
#         read_tilemap.append(row)

# # Displaying the read tilemap
# for row in read_tilemap:
#     print(row)
