class ContentCreator:
    def __init__(self, name, followers):
        self.name = name
        self.followers = followers

    def createPost(self):
        if self.followers < 1000:
            print(f"{self.name} has a small following. Keep creating content!")
        elif 1000 <= self.followers < 10000:
            print(f"{self.name} is gaining popularity! Keep it up!")
        else:
            print(f"{self.name} is a well-known creator with a large following!")

class Tiktoker(ContentCreator):
    def __init__(self, name, followers):
        super().__init__(name, followers)

    def recordVideo(self):
        print(f"{self.name} is recording a new TikTok video!")

# Example usage
if __name__ == "__main__":
    creator = ContentCreator("Alice", 500)
    creator.createPost()

    tiktoker = Tiktoker("Bob", 15000)
    tiktoker.createPost()
    tiktoker.recordVideo()