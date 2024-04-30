let inputs = document.getElementById("inp");
let text = document.getElementById("todo");

function Add() {
    if (inputs.value === "") {
        alert("Please Enter Task");
    } else {
        // Create the main task container div
        let newTask = document.createElement("div");
        newTask.className = "flex space-x-2 w-full px-3 py-2 items-center rounded-lg bg-gray-600 bg-opacity-40 es";

        // Create the checkbox container
        let checkboxContainer = document.createElement("div");
        checkboxContainer.className = "flex justify-center w-5 h-5 border-2 border-solid rounded-full cursor-pointer border-white bg-transparent";
        checkboxContainer.innerHTML = `
            <svg width="16" height="16" fill="none"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.717 10.053a.667.667 0 0 1-1.044-.827l.053-.065 4.446-4.94a.667.667 0 0 1 1.043.826l-.052.065-4.446 4.94Z" fill="#fff"></path><path d="M7.186 11.748a.667.667 0 0 1-.869.152l-.068-.048-3.332-2.667a.667.667 0 0 1 .764-1.089l.069.048 3.332 2.667c.287.23.334.65.104.937Z" fill="#fff"></path></svg>
        `;
        checkboxContainer.setAttribute('id','check');
        newTask.appendChild(checkboxContainer);
        checkboxContainer.onclick = function () {
            newTask.classList.toggle("line-through");
            this.setAttribute('id','checked');
        };

        // Create the task description container
        let taskDescription = document.createElement("div");
        taskDescription.className = "break-word w-[calc(100%-36px)] flex-1 text-xs";
        taskDescription.textContent = inputs.value;
        newTask.appendChild(taskDescription);

        // Create the delete button
        let deleteButton = document.createElement("button");
        deleteButton.type = "button";
        deleteButton.innerHTML = `
            <svg width="16" height="16" fill="none">
                <path fill-rule="evenodd" clip-rule="evenodd" d="M5.148 11.803a.672.672 0 0 1-1.003-.892l.052-.059 6.655-6.655a.672.672 0 0 1 1.003.892l-.052.059-6.655 6.655Zm6.655 0a.672.672 0 0 1-.892.052l-.059-.052-1.426-1.426a.672.672 0 0 1 .892-1.003l.059.052 1.426 1.426a.672.672 0 0 1 0 .951ZM5.682 6.626a.672.672 0 0 0 .892-1.003L5.148 4.197l-.059-.052a.672.672 0 0 0-.892 1.003l1.426 1.426.059.052Z" fill="#7B7170"></path>
            </svg>
        `;
        deleteButton.addEventListener("click", function () {
            newTask.remove();
        });
        newTask.appendChild(deleteButton);

        // Append the new task to the task container
        text.appendChild(newTask);

        // Clear the input field after adding the task
        inputs.value = "";

    }
}
