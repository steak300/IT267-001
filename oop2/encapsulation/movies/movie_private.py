class Movie:
    def __init__(self,title,year,genre) -> None:
    #private begin with __
        self.__title = ''
        self.__year = year
        self.__genre = genre
    #private method
    def __get_movie(self):
        print(f'title:{self.__title}\ngenre: {self.__genre}')
        
    def print_detail(self):
        self.__get_movie()