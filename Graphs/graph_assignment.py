

class City:
    def __init__(self,name,population):
        self.name = name
        self.population = int(population)
        self.adjacent_cities = []
    
    def add_neighbor(self, city):
        """Adds a neighboring city to the adjacency list."""
        if city not in self.adjacent_cities:
            self.adjacent_cities.append(city)
            return True
        return False
        
    def graph_of_cities(population_file, road_network_file):
        """
        Read the text file and construct a graph of cities. Use the objects of a class City to model a city and the graph. 
        Note that conceptually, this is similar to the adjacency list representation of the graph. 
        """
        cities = {}
        with open(population_file, 'r') as f:
            for line in f:
                if ':' in line:
                    city_name = line.split(':')[0]
                    city_population = line.split(':')[1]
                    cities[city_name] = City(city_name, city_population)

        with open(road_network_file, 'r') as f:
            for line in f:
                if ':' in line:
                    city1_name, city2_name = line.strip().split(' : ')
                    
                    # Check if both cities exist in our map
                    if city1_name in cities and city2_name in cities:
                        city1 = cities[city1_name]
                        city2 = cities[city2_name]
                        
                        # Add bidirectional connection
                        city1.add_neighbor(city2)
                        city2.add_neighbor(city1)
    
        return cities


g = City()
        
        
        
