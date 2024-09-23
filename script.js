// Function to add a new task
function addTask() {
    const taskInput = document.getElementById('new-task');
    const taskText = taskInput.value.trim();

    if (taskText !== '') {
        const taskList = document.getElementById('task-list');

        // Create a new task list item
        const listItem = document.createElement('li');
        listItem.innerHTML = `
            <span onclick="toggleComplete(this)">${taskText}</span>
            <button class="remove-button" onclick="removeTask(this)">Remove</button>
        `;
        
        // Append the new task to the list
        taskList.appendChild(listItem);
        
        // Clear the input field
        taskInput.value = '';
    }
}

// Function to mark a task as complete
function toggleComplete(task) {
    task.parentNode.classList.toggle('completed');
}

// Function to remove a task from the list
function removeTask(button) {
    const task = button.parentNode;
    task.remove();
}
