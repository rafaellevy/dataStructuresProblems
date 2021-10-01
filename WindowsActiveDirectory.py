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
    """
    Return True if user is in the group, False otherwise.
    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # if both are empty return false
    if user in group.users:
        return True
    if len(group.groups) == 0:
        return False
    # if name is in users array return true
    # if name is not in users array:
        # iterate over all groups inside the groups array  
        # looking for the name inside of the users.array
    for object in group.groups:
        return is_user_in_group(user, object)
    
print(is_user_in_group(sub_child_user, child)) # True
print(is_user_in_group(sub_child_user, parent))  # True
print(is_user_in_group("Some User", sub_child))  # False