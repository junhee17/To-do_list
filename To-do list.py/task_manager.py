def load_tasks():
    try:
        with open('tasks.txt', 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            print(task, file=f)

