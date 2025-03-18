class GraphicDesigner:
    def __init__(self, name):
        self.name = name

    def designLogo(self):
        print(f"{self.name} is designing a logo for the brand.")

class WebDeveloper:
    def __init__(self, name):
        self.name = name

    def buildWebsite(self):
        print(f"{self.name} is building a website for the brand.")

class DigitalSolutionsProvider(GraphicDesigner, WebDeveloper):
    def __init__(self, name):
        GraphicDesigner.__init__(self, name)
        WebDeveloper.__init__(self, name)

    def deliverProject(self):
        self.designLogo()
        self.buildWebsite()
        print(f"{self.name} has successfully delivered a complete brand identity and online presence!")

# Example usage
if __name__ == "__main__":
    provider = DigitalSolutionsProvider("Charlie")
    provider.deliverProject()