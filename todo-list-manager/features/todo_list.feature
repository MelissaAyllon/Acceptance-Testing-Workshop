Feature: To-Do List Manager

Scenario: Add a task to the to-do list
    Given the To-Do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
        | Task          |
        | Buy groceries |
        | Pay bills     |

Scenario: Mark a task as completed
    Given the to-do list contains tasks:
        | Task          | Status  |
        | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
    When the user edits the task "Buy groceries" to "Buy fruits"
    Then the to-do list should contain "Buy fruits" and not "Buy groceries"

Scenario: Delete a task from the to-do list
    Given the to-do list contains tasks:
        | Task          |
        | Buy groceries |
        | Pay bills     |
    When the user deletes the task "Pay bills"
    Then the to-do list should not contain "Pay bills"
