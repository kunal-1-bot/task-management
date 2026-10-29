
import { useState } from 'react';
import TaskForm from './components/TaskForm.jsx';

function App() {
  const [tasks, setTasks] = useState([]);

  function handleAddTask(newTask) {
    setTasks((previousTasks) => [...previousTasks, newTask]);
  }

  return (
    <div>
      <h1>My Task Manager</h1>
      <p>Manage your daily tasks in one place.</p>

      <h2>Create a New Task</h2>

      <TaskForm onAddTask={handleAddTask} />

      <hr />

      <h2>My Tasks ({tasks.length})</h2>

      {tasks.length === 0 ? (
        <p>No tasks yet. Add your first task!</p>
      ) : (
        <ul>
          {tasks.map((task) => (
            <li key={task.id}>
              <h3>{task.title}</h3>
              <p>{task.description || 'No description provided.'}</p>
              <p>Status: {task.status.replace('_', ' ')}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
