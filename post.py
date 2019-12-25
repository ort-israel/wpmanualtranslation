# Post class
class Post:

    def __init__(self, num_id, str_content, str_title, str_excerpt, str_name, str_guid):
        # Here be all class vars
        self.id = num_id
        self.content = str_content
        self.title = str_title
        self.excerpt = str_excerpt
        self.name = str_name
        self.link = str_guid

        # self.sections = get_sections(self.content)


