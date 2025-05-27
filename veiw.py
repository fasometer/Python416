def index():
    with open("tamplates/index.html") as template:
        return template.read()


def blog():
    with open("tamplates/blog.html") as template:
        return template.read()
