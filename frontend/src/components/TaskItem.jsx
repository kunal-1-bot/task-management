
function TaskItem({ task }) {
  return (
    <li>
      <h3>{task.title}</h3>

      <p>
        {task.description || 'No description provided.'}
      </p>

      <p>
        Status: {task.status.replace('_', ' ')}
      </p>
    </li>
  );
}

export default TaskItem;
