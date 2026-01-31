#1 с прошлой домашки номер 2
'''
def make_task_manager():
    tasks = []
    next_id = 1
    def add_task(name):
        nonlocal next_id
        tasks = {'name' : 'name', 'completed': False}
        next_id += 1
        return next_id - 1
    def mark_task(task_id):
        if task_id in tasks:
            tasks[task_id]['completed'] = True
            return True
        return False
    def get_all_tasks():
        return tasks
    def get_incomplete_tasks():
     x = [ i for i in tasks if not tasks['completed']]
     return x
    def get_statistics():
        total_tasks = len(tasks)
        completed_tasks = sum(task for task in tasks if tasks['completed'])
        incomplete_tasks = total_tasks - completed_tasks
        y = [ total_tasks,  completed_tasks, incomplete_tasks]
        return y
    return add_task, mark_task, get_all_tasks, get_incomplete_tasks, get_statistics
add_task, mark_task_completed, get_all_tasks, get_incomplete_tasks, get_statistics = make_task_manager()
mark_task_completed(task1_id)
print( get_all_tasks())
print( get_incomplete_tasks())
print get_statistics())
'''

#2









