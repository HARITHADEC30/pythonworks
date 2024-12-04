#initialze attributes (instanse variables)
#constructor

#initilaixing instanse variavle ---->constructor

# java--->ClassName
# javascript--->constructor
# python-->(__init__)




class movie:

    title:str

    rating:int

    run_time:int

    director:str

    genre:str

    def set_movie(self,title,rating,run_time,director,genre):
        self.title=title
        self.rating=rating
        self.run_time=run_time
        self.director=director
        self.genre=genre

    def display_movie(self):
        print(self.title,self.rating,self.run_time,self.director,self.genre)

movie_instance1=movie()
movie_instance2=movie()
movie_instance1.set_movie("ARM",9,2,"Jithim Lal","Drama")
movie_instance2.set_movie("KGF",9,2,"Prashanth Neel","Thriller")
movie_instance1.display_movie()
movie_instance2.display_movie()
