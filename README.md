# CodeVault - Code Snippet Manager

A Django web application for creating, managing, and sharing code snippets with notes and tags.

## Features

### Core Features
- **Code Snippet Management**: Create, read, update, and delete code snippets
- **Syntax Highlighting**: Automatic syntax highlighting for multiple programming languages
- **Notes System**: Add detailed notes and remarks for each code snippet
- **Tagging System**: Organize snippets with custom tags for easy categorization
- **Search & Filter**: Search snippets by title, code, notes, or tags
- **Markdown Export**: Export snippets as formatted Markdown files

### User Features
- **User Authentication**: Register, login, and manage personal snippets
- **Public/Private Snippets**: Control visibility of your snippets
- **User Dashboard**: View and manage your personal snippets
- **Responsive Design**: Modern, mobile-friendly interface

### Advanced Features
- **Tag-based Filtering**: Browse snippets by specific tags
- **Language Filtering**: Filter snippets by programming language
- **Pagination**: Efficient browsing with paginated results
- **Copy to Clipboard**: One-click code copying functionality
- **Admin Interface**: Full Django admin for managing snippets and tags

## Supported Programming Languages

- Python
- JavaScript
- Java
- C++
- C#
- PHP
- Ruby
- Go
- Rust
- Swift
- Kotlin
- TypeScript
- HTML
- CSS
- SQL
- Bash
- PowerShell
- Other

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd codevault
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Usage

### Creating Snippets
1. Log in to your account
2. Click "New Snippet" in the navigation
3. Fill in the snippet details:
   - **Title**: Descriptive name for your snippet
   - **Language**: Select the programming language
   - **Code**: Paste your code
   - **Notes**: Add explanations, usage notes, or remarks
   - **Tags**: Add relevant tags for categorization
   - **Visibility**: Choose public or private

### Managing Snippets
- **View**: Click on any snippet to see full details with syntax highlighting
- **Edit**: Use the edit button to modify your snippets
- **Delete**: Remove snippets you no longer need
- **Export**: Download snippets as Markdown files

### Searching and Filtering
- **Search**: Use the search bar to find snippets by title, code, notes, or tags
- **Language Filter**: Filter snippets by programming language
- **Tag Filter**: Browse snippets with specific tags
- **Combined Filters**: Use multiple filters together

### Tags
- **Browse Tags**: View all available tags and their usage
- **Tag Details**: Click on tags to see all snippets with that tag
- **Tag Management**: Create and manage tags through the admin interface

## Admin Interface

Access the Django admin at `/admin/` to:
- Manage all snippets and tags
- View user statistics
- Bulk operations on snippets
- Advanced filtering and search

## API Endpoints

The application provides the following main URLs:

- `/` - Home page with all public snippets
- `/my-snippets/` - User's personal snippets (login required)
- `/create/` - Create new snippet (login required)
- `/search/` - Search snippets
- `/tags/` - Browse all tags
- `/tags/<id>/` - View snippets with specific tag
- `/<id>/` - View specific snippet
- `/<id>/edit/` - Edit snippet (owner only)
- `/<id>/delete/` - Delete snippet (owner only)
- `/<id>/export/` - Export snippet as Markdown

## Markdown Export

Snippets can be exported as Markdown files containing:
- Snippet title and metadata
- Programming language information
- Tags and timestamps
- Notes section (if provided)
- Code block with proper syntax highlighting

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support or questions, please open an issue on the GitHub repository.

---

**CodeVault** - Your Personal Code Snippet Manager 