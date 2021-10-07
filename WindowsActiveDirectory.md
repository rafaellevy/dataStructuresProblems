### Windows Active Directory

I decided to use recursion to find whether the user exists in the group, because
the Group object can have other Group objects in the groups attribute.

The time complexity is O(n) because the worst case scenario is you have to look
through every group within the Group object.

The space complexity is O(n) because each Group Object takes up the same space.
