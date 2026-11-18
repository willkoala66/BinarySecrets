class CSVParser:
    """ A simple CSV parser
    """
    def __init__(self):
        pass
    
    def parse_str(self, csv_formated_input: str):
        """ Parses a CSV formatted String and returns a 2D Array of it

        Args:
            csv_formated_input (str): The CSV formatted String Input

        Returns:
            list (list<list\<str\>>)): the 2D array Of the Input 
        """
        f = csv_formated_input
        x = f.splitlines()
        g = []
        for i in x:
            g.append(i.split(","))
        return g
    
    
    
class CSVBuilder:
    colums: int
    rows: int
    def __init__(self):
        self.colums = 0
        self.rows = 0
    
    def add_colum(self, num: int):
        self.colums = self.colums + num
        
    def add_row(self, num: int):
        self.rows = self.rows + num
    
    def build_CSV_1D(self, data: list):
        """ Returns a CSV formatted string from a 1D array

        Args:
            data (list): A 1D array of input data

        Raises:
            ValueError: Amount of rows and colums and data in array do not match
        Returns:
            String (str): CSV formatted string
        """
        if len(data) != self.rows * self.colums:
            raise ValueError
        out = []
        for z in range(self.rows):
            out.append(["" for j in range(self.colums)])
        current_row = 0
        current_colum = 0
        for i in data:
            if current_row >= self.rows:
                current_colum = current_colum + 1
                current_row = 0
            if current_colum >= self.colums:
                break
                
            out[current_colum][current_row] = i
            current_row = current_row+1
        out_str = ""
        for col in out:
            for row in col:
                out_str = out_str + f"{row},"
            out_str = out_str + "\n"
        return out_str
    
if __name__ == "__main__":    
    c = CSVParser()    
    b  = c.parse_str("abcd,efgh\nhijk,lmnop")
    print(b)
    
    cars = ["Ford", "Volvo", "BMW", "Toyota"]
    cb = CSVBuilder()
    cb.add_colum(2)
    cb.add_row(2)
    print(cb.build_CSV_1D(cars))