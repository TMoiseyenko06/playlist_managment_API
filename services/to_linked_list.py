
class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None

    def add_song(self,song_data):
        new_song = Node(song_data)
        if self.head is None:
            self.head = new_song
            self.tail = new_song
        else:
            new_song.prev = self.tail
            self.tail.next = new_song
            self.tail = new_song

    def play(self):
        self.current_song = self.head
        return self.current_song.data
    
    def play_next(self):
        if self.current_song.next == None:
            return self.current_song.data
        else:
            self.current_song = self.current_song.next
            return self.current_song.data
        
    def play_prev(self):
        if self.current_song.prev == None:
            return self.current_song.data
        else:
            self.current_song = self.current_song.prev
            return self.current_song.data
        
    def clear(self):
        self.head = None
        self.tail = None
        




            

