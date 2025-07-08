import sys
import os
from behave import given, when, then
import todo_list  # Ensure the correct module name

# Insert the module path to the system path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

# Step 1: Initialize empty to-do list
@given('the To-Do list is empty')
def step_empty_list(context):
    todo_list.tasks = []  # Clear the tasks list before use


# Step 2: Initialize the to-do list with tasks
@given('the to-do list contains tasks')
def step_list_contains_tasks(context):
    todo_list.tasks = []  # Clear tasks before adding new ones
    for row in context.table:
        todo_list.add_task(row['Task'])
        if 'Status' in row.headings and row['Status'] == 'Completed':
            todo_list.mark_completed(row['Task'])


# Step 3: Add a task
@when('the user adds a task "{task}"')
def step_add_task(context, task):
    todo_list.add_task(task)


# Step 4: List all tasks
@when('the user lists all tasks')
def step_list_tasks(context):
    context.output = todo_list.list_tasks()


# Step 5: Mark task as completed
@when('the user marks task "{task}" as completed')
def step_mark_completed(context, task):
    todo_list.mark_completed(task)


# Step 6: Clear all tasks
@when('the user clears the to-do list')
def step_clear_list(context):
    todo_list.clear_tasks()


# Step 7: Delete a task
@when('the user deletes task "{task}"')
def step_delete_task(context, task):
    todo_list.delete_task(task)


# Step 8: Search for tasks
@when('the user searches for "{keyword}"')
def step_search_tasks(context, keyword):
    context.search_results = todo_list.search_tasks(keyword)


# Step 9: Verify task is in the to-do list
@then('the to-do list should contain "{task}"')
def step_should_contain(context, task):
    task_titles = [t['title'] for t in todo_list.tasks]
    assert task in task_titles


# Step 10: Verify task is not in the to-do list
@then('the to-do list should not contain "{task}"')
def step_should_not_contain(context, task):
    task_titles = [t['title'] for t in todo_list.tasks]
    assert task not in task_titles


# Step 11: Verify the output
@then('the output should contain')
def step_output_contains(context):
    expected = context.text.strip()
    actual = context.output.strip()
    assert expected == actual


# Step 12: Verify task completion status
@then('the to-do list should show task "{task}" as completed')
def step_task_completed(context, task):
    for t in todo_list.tasks:
        if t['title'] == task:
            assert t['status'] == 'Completed'


# Step 13: Verify the to-do list is empty
@then('the to-do list should be empty')
def step_list_empty(context):
    assert len(todo_list.tasks) == 0


# Step 14: Verify search results
@then('the search should find "{task}"')
def step_search_finds(context, task):
    found_titles = [t['title'] for t in context.search_results]
    assert task in found_titles
