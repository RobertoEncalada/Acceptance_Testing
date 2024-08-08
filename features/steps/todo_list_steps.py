from behave import given, when, then
from todo_list import ToDoList

# Initialize a global instance of ToDoList for the steps
to_do_list = ToDoList()

#-----------------Primera Actividad-------------------#

@given('the to-do list is empty')
def step_impl(context):
    to_do_list.clear_tasks()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    to_do_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = [t['task'] for t in to_do_list.list_tasks()]
    assert task in tasks, f'Task "{task}" not found in the to-do list'


#-----------------Segunda Actividad-------------------#

@given('the to-do list contains tasks:')
def step_impl(context):
    to_do_list.clear_tasks()
    for row in context.table:
        to_do_list.add_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.output = to_do_list.list_tasks()

@then('the output should contain:')
def step_impl(context):
    expected_tasks = [row['Task'] for row in context.table]
    actual_tasks = [t['task'] for t in context.output]
    assert actual_tasks == expected_tasks, f"Expected {expected_tasks} but got {actual_tasks}"


#-----------------Tercera Actividad-------------------#

@given('the to-do list contains tasks to be marked:')
def step_impl(context):
    to_do_list.clear_tasks()
    for row in context.table:
        to_do_list.add_task(row['Task'])

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    to_do_list.complete_task(task)

@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    task_status = next((t['status'] for t in to_do_list.list_tasks() if t['task'] == task), None)
    assert task_status == 'Completed', f'Task "{task}" is not completed'


#-----------------Cuarta Actividad-------------------#

@given('the to-do list contains tasks to be cleared:')
def step_impl(context):
    to_do_list.clear_tasks()
    for row in context.table:
        to_do_list.add_task(row['Task'])

@when('the user clears the to-do list')
def step_impl(context):
    to_do_list.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert not to_do_list.list_tasks(), f'To-do list is not empty: {to_do_list.list_tasks()}'


#-----------------Quinta Actividad-------------------#

@given('the to-do list contains tasks to be deleted:')
def step_impl(context):
    to_do_list.clear_tasks()
    for row in context.table:
        to_do_list.add_task(row['Task'])

@when('the user deletes the task "{task}"')
def step_impl(context, task):
    to_do_list.delete_task(task)

@then('the to-do list should not contain "{task}"')
def step_impl(context, task):
    tasks = [t['task'] for t in to_do_list.list_tasks()]
    assert task not in tasks, f'Task "{task}" is still in the to-do list'
