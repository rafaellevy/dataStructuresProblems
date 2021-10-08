class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    # if both are empty return false
    if user in group.users:
        return True
    if not user:
        return "please give the user a name"
    if len(group.groups) == 0:
        return False
    # if name is in users array return true
    # if name is not in users array:
        # iterate over all groups inside the groups array  
        # looking for the name inside of the users.array
    for object in group.groups:
        return is_user_in_group(user, object)

# Expect to be true
print(is_user_in_group(sub_child_user, child))
print()
# Expect to be true 
print(is_user_in_group(sub_child_user, parent))
print()
# Expect to be false
print(is_user_in_group("Some User", sub_child))
print()
#expect error message
print(is_user_in_group("", parent))