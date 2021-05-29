class ToDo:
    '''Record things to do for an event, e.g. an upcoming overseas trip'''
    def __init__(self, event: str):
        self._event = event
        self._todo_actions = []

    # Getter property for event name
    @property
    def event(self):
        return self._event


    def add_todo(self, todo: str):
        if todo not in self._event:
            self._todo_actions.append(todo)
            return f"Added {todo}!"
        else:
            return f"{todo} already existed."

    def delete_todo_item(self, index: int):
        if index - 1 > len(self._event): or index < 0:
            return f"Invalid index: {index}"
        else:
            return f"ToDo item: {index, self._todo_actions.pop(index)} removed"
            self._todo_actions.pop(index)

    def display_todo_list(self):
        event = self._event
        todo_action_items = '\n'.join(f'{idx}.  {val}' for idx, val in enumerate(self._todo_actions))
        return f"Event: {event}\n" + todo_action_items

    def __str__(self):
        return f"{self._event} {self._todo_actions}"

if __name__ == '__main__':
    # create a ToDo obj for 'things to bring tomorrow'
    t1 = ToDo('Things to bring tomorrow')
    # add a few todo actions to the obj
    t1.add_todo('Toileteries')
    t1.add_todo('Snacks')
    t1.add_todo('Indemnity Forms')
    # display the todo list
    print(t1.display_todo_list())
    print('\n')
    # remove a todo item
    print(t1.delete_todo_item(1))
    print('\n')
    # display the todo list
    print(t1.display_todo_list())
    print(t1)
