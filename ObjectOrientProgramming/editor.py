class editor:

    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def __str__(self):
        return self.name

editor_instance1=editor("pycharm","jebrains")

editor_instance2=editor("vscode","microsoft")


print(editor_instance1)