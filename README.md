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

## Phase 2: Database Integration

- Migrated from in-memory storage to SQLite via SQLAlchemy
- All task endpoints now read/write through the database

## Phase 3: Projects

- Added a `Project` table (`id`, `name`, `created_at`)
- Tasks now belong to a project via a `project_id` foreign key
- New project endpoints:
  - `GET /projects` - Retrieve all projects
  - `POST /projects` - Create new project
  - `GET /projects/{id}/tasks` - Get all tasks for a specific project
- `CreateTask` now requires a `project_id`

### Next Steps

- Implement frontend UI components
- Add CORS configuration for backend-frontend communication
- Production-level refactoring and improvements
