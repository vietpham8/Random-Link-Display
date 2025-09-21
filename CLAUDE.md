# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Vietnamese link catalog/bookmark manager application with a Node.js backend and SQLite database. The application allows users to manage and display links in categorized collections with dynamic positioning, click tracking, and persistent data storage.

## Application Architecture

### Full-Stack Structure
- **Backend**: Node.js with Express.js server
- **Database**: SQLite with foreign key relationships
- **Frontend**: HTML/CSS/JavaScript served as static files
- **API**: RESTful endpoints for CRUD operations
- **Data Storage**: Persistent SQLite database with automatic initialization

### Key Components
- **Server Layer**: Express.js REST API with SQLite integration
- **Data Layer**: SQLite database with `catalogues` and `links` tables
- **UI Layer**: Dynamic DOM manipulation with API integration
- **Positioning Engine**: Client-side algorithm for non-overlapping random link placement
- **Admin Interface**: Modal-based management system with real-time updates

## Development Commands

### Setup and Installation
```bash
# Install dependencies
npm install

# Start development server with auto-reload
npm run dev

# Start production server
npm start

# Initialize database (automatic on first run)
npm run init-db
```

### Database Management
- Database file: `database.db` (SQLite)
- Automatic table creation on server start
- Default seed data inserted if tables are empty

## Database Schema

### Catalogues Table
```sql
CREATE TABLE catalogues (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  description TEXT NOT NULL,
  color TEXT NOT NULL DEFAULT '#667eea',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Links Table
```sql
CREATE TABLE links (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  catalogue_id INTEGER NOT NULL,
  url TEXT NOT NULL UNIQUE,
  description TEXT NOT NULL,
  clicks INTEGER DEFAULT 0,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (catalogue_id) REFERENCES catalogues (id) ON DELETE CASCADE
);
```

### API Data Structures

#### Catalogue Object
```javascript
{
  id: number,
  name: string,
  description: string,
  color: string,
  created_at: string
}
```

#### Link Object (with joined catalogue data)
```javascript
{
  id: number,
  catalogue_id: number,
  url: string,
  description: string,
  clicks: number,
  created_at: string,
  catalogue_name: string,
  catalogue_color: string
}
```

## API Endpoints

### Catalogues
- `GET /api/catalogues` - Get all catalogues
- `POST /api/catalogues` - Create new catalogue
- `DELETE /api/catalogues/:id` - Delete catalogue and associated links

### Links
- `GET /api/links` - Get all links (optional `?catalogue_id=X` filter)
- `POST /api/links` - Create new link
- `PATCH /api/links/:id/click` - Increment click count
- `DELETE /api/links/:id` - Delete specific link

### Data Management
- `GET /api/stats` - Get usage statistics
- `GET /api/export` - Export all data as JSON
- `POST /api/import` - Import data from JSON
- `DELETE /api/clear` - Clear all data

## Key Functionality

### Link Management
- **Add Links**: API-backed creation with server-side validation
- **Delete Links**: Persistent removal with confirmation dialogs
- **Click Tracking**: Database-backed increment with visual size effects
- **URL Validation**: Server-side duplicate prevention

### Catalogue Management
- **Create Catalogues**: Database persistence with unique name validation
- **Delete Catalogues**: Cascading deletion removes associated links
- **Color Coding**: Persistent visual differentiation
- **Filtering**: Real-time API filtering by catalogue

### Dynamic Positioning
- **Collision Detection**: Client-side `isOverlapping()` function
- **Auto-randomization**: Links reposition every 8-12 seconds
- **Manual Shuffle**: Space key or "Xáo trộn" button triggers repositioning
- **Responsive Layout**: Adjusts to window resize events

### Data Management
- **Export**: Server-generated JSON download
- **Import**: Server-side validation and bulk import
- **Persistence**: All data automatically saved to SQLite
- **Statistics**: Real-time usage analytics

## Development Workflow

### Running the Application
```bash
# Install dependencies
npm install

# Start development server (with nodemon for auto-restart)
npm run dev

# Or start production server
npm start

# Application will be available at http://localhost:3000
```

### Testing
- **Manual Testing**: Use browser at http://localhost:3000
- **API Testing**: Test endpoints with tools like Postman or curl
- **Database Testing**: Check `database.db` file for data persistence
- **Cross-browser**: Test frontend in Chrome, Firefox, Safari, Edge
- **Responsive**: Test on mobile devices and different screen sizes

### Making Changes
**Backend Changes (server.js):**
1. Edit `server.js`
2. Server auto-restarts with nodemon (in dev mode)
3. Test API endpoints

**Frontend Changes (public/index.html):**
1. Edit `public/index.html`
2. Refresh browser to see changes
3. No build process required

**Database Changes:**
1. Delete `database.db` to reset
2. Restart server to recreate with default data
3. Or modify initialization in `server.js`

## Key Functions Reference

### Server-Side Functions (server.js)
- `initDatabase()` - Creates tables and seed data
- API route handlers for CRUD operations
- Database connection management
- Error handling and validation

### Client-Side Functions (public/index.html)

#### API Integration
- `apiRequest(endpoint, options)` - Generic API request handler
- `loadData()` - Fetches initial data from server
- `updateAllLists()` - Refreshes all data from API

#### Core UI Functions
- `renderLinks()` - Displays filtered links with positioning
- `renderCatalogueSelector()` - Updates category filter buttons
- `setRandomPosition(element, index)` - Calculates non-overlapping positions

#### Admin Functions
- `addCatalogue(name, description, color)` - Creates new category via API
- `addLink(catalogueId, url, description)` - Creates new link via API
- `deleteCatalogue(catalogueId)` - Removes category via API
- `deleteLink(linkId)` - Removes specific link via API

#### UI Management
- `showAdmin()` / `hideAdmin()` - Toggle admin panel
- `switchTab(tabName)` - Navigate admin panel tabs
- `switchCatalogue(catalogueId)` - Filter links by category via API
- `showMessage(message, type)` - Display success/error messages
- `showLoading(show)` - Toggle loading indicator

## Keyboard Shortcuts
- **Ctrl + M**: Open admin panel
- **Escape**: Close admin panel
- **Space**: Randomize link positions

## File Structure
```
├── package.json          # Node.js dependencies and scripts
├── server.js             # Express server and API endpoints
├── database.db           # SQLite database (auto-created)
├── public/
│   └── index.html        # Frontend application
└── CLAUDE.md             # This documentation file
```

## Customization Guidelines

### Adding New API Endpoints
1. Add route handler in `server.js`
2. Implement database queries
3. Add error handling and validation
4. Update frontend to use new endpoint

### Adding New Catalogue/Link Properties
1. Modify database schema in `initDatabase()`
2. Update API endpoints to handle new fields
3. Update frontend forms and rendering
4. Consider migration for existing data

### Styling Changes
- Edit CSS in `public/index.html` `<style>` section
- Main theme color: `#667eea`
- Gradient background: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`

### Database Modifications
- Schema changes require database recreation or migration
- Backup data before schema changes using export feature
- Default data defined in `initDatabase()` function

## Common Issues

### Performance
- SQLite handles thousands of links efficiently
- Large datasets may need pagination for UI
- Consider indexing for frequent queries

### Database Corruption
- SQLite is robust but backup regularly
- Use export feature for data backup
- Database file can be copied for backup

### Browser Compatibility
- Frontend uses modern JavaScript (ES6+)
- Requires support for: `fetch()`, `async/await`, template literals
- FileReader API required for import functionality

### Network Issues
- Frontend shows loading indicators for API calls
- Error messages displayed for failed requests
- Retry logic may be needed for unreliable connections

## Security Considerations
- Input validation on both client and server
- SQL injection prevention via parameterized queries
- No authentication system - consider adding for multi-user scenarios
- CORS enabled for development - configure for production
- No HTTPS - configure reverse proxy for production