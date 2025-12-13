class Format():
    def __init__(self, names, descriptions, details):
        self.names = names
        self.descriptions = descriptions
        self.details = details
    
    def format_movies(self):
        with open("test.md", "w") as file:
            pass

        for i in range(len(self.names)):
            name = self.names[i].text
            description = self.descriptions[i].text
            details = self.details[i]

            markdown_content = f"# {i+1}. {name} \n* **IMDb Rating:** {details[0]} \n* **Type:** {details[1]} \n* **Duration:** {details[2]} \n* **Content Rating:** {details[3]} \n* **Description:** {description}\n"
            with open("test.md", "a") as file:
                file.write(markdown_content)

    def format_series(self):
        with open("test.md", "w") as file:
            pass

        for i in range(len(self.names)):
            name = self.names[i].text
            description = self.descriptions[i].text
            details = self.details[i]

            markdown_content = f"# {i+1}. {name} \n* **IMDb Rating:** {details[0]} \n* **Type:** {details[1]} \n* **Seasons:** {details[2]} \n* **Content Rating:** {details[3]} \n* **Description:** {description}\n"
            with open("test.md", "a") as file:
                file.write(markdown_content)

    def format_indian_movies(self):
        with open("test.md", "w") as file:
            pass

        for i in range(len(self.names)):
            name = self.names[i].text
            description = self.descriptions[i].text
            ratings = self.details[i].text

            markdown_content = f"# {name} \n* **IMDb Rating:** {ratings}/10 \n* **Type:** Movie \n* **Description:** {description}\n"
            with open("test.md", "a") as file:
                file.write(markdown_content) 