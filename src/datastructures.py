
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self._next_id = 1
        self.last_name = last_name
        # example list of members
        self._members = [
            {'id':1, 'name': 'John', 'age': 33, 'lucky_numbers': [7,13,22]},
            {'id':2,'name': 'Jane', 'age': 35, 'lucky_numbers': [10,14,3]},
            {'id':3,'name': 'Jimmy', 'age': 5, 'lucky_numbers': [1]} 
        ]
# jackson_family.add_member({'id':1, 'name': 'John', 'age': 33, 'lucky_numbers': [7, 13, 22]})
# jackson_family.add_member({'id':2,'name': 'Jane', 'age': 35, 'lucky_numbers': [10, 14, 3]})
# jackson_family.add_member({'id':3,'name': 'Jimmy', 'age': 5, 'lucky_numbers': [1]})

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id +=1
        return generated_id
        #  randint(0, 99999999)
    def add_member(self, member):
        # fill this method and update the return
        if member["name"] == '' or member["lucky_numbers"] == '':
            return None
        if member["age"] > 110:
            return 'wrong age'
        self._members.append(member)     
        return member

    def delete_member(self, id):
        # fill this method and update the return        
        for ele in self._members:
            if ele['id']==id : 
                self._members.remove(ele)
                return self._members     
            else:
                return "not found"

    def get_member(self, id):
        # fill this method and update the return
        for ele in self._members:
            if ele['id']==id : 
                member = ele
                break
            else: member=None
        return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
