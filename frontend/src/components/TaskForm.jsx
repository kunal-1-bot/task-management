
import { useState } from 'react';

function TaskForm({ onAddTask }) {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [status, setStatus] = useState('pending');

  function handleSubmit(event) {
    event.preventDefault();

    if (title.trim() === '') {
      alert('Please enter a task title.');
      return;
    }

    const newTask = {
      id: Date.now(),
      title: title.trim(),
      description: description.trim(),
      status,
    };

    onAddTask(newTask);

    setTitle('');
    setDescription('');
    setStatus('pending');
  }

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="title">Task title</label>
        <br />
        <input
          id="title"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
          placeholder="Enter task title"
        />
      </div>

      <br />

      <div>
        <label htmlFor="description">Description</label>
        <br />
        <textarea
          id="description"
          value={description}
          onChange={(event) => setDescription(event.target.value)}
          placeholder="Enter task description"
        />
      </div>

      <br />

      <div>
        <label htmlFor="status">Status</label>
        <br />
        <select
          id="status"
          value={status}
          onChange={(event) => setStatus(event.target.value)}
        >
          <option value="pending">Pending</option>
          <option value="in_progress">In Progress</option>
          <option value="completed">Completed</option>
        </select>
      </div>

      <br />

      <button type="submit">Add Task</button>
    </form>
  );
}

export default TaskForm;
