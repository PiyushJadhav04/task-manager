# Task Manager

Simple task manager app that users will be able to write down their tasks.
Will evolve over time.

## Phase 1: Core API & Project Setup

### Backend

- FastAPI server initialized with basic health check endpoint
- RESTful API endpoints for task management:
  - `GET /tasks` - Retrieve all tasks
  - `POST /tasks` - Create new task
  - `GET /tasks/{id}` - Get specific task
  - `PUT /tasks/{id}` - Update task
  - `DELETE /tasks/{id}` - Delete task
- Pydantic models for request/response validation (`CreateTask`, `UpdateTask`)
- Field validation (title: min 1, max 200 characters)
- Error handling with HTTP 404 for missing tasks
- Basic data structure with task properties: `id`, `title`, `done` status

### Frontend

- React project initialized with Vite
- Basic project structure and build configuration

### Project Infrastructure

- Git repository initialized with basic commits
- Frontend `.gitignore` configured
- Project folder structure (backend, frontend)

### Next Steps

- Add database integration (currently using in-memory storage)
- Implement frontend UI components
- Add CORS configuration for backend-frontend communication
- Production-level refactoring and improvements
