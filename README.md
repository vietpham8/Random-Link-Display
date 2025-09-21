# Random Link Catalog - Static Site

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Netlify Status](https://api.netlify.com/api/v1/badges/your-badge-id/deploy-status)](https://app.netlify.com/sites/random-link/deploys)
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen.svg)](https://random-link.netlify.app/)
[![GitHub stars](https://img.shields.io/github/stars/vietpham8/Random-Link-Display?style=social)](https://github.com/vietpham8/Random-Link-Display/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/vietpham8/Random-Link-Display?style=social)](https://github.com/vietpham8/Random-Link-Display/network/members)

A Vietnamese link catalog/bookmark manager application converted to a static site for Netlify deployment. Manages links in categorized collections with dynamic positioning and click tracking using localStorage.

🌐 **[Live Demo: https://random-link.netlify.app/](https://random-link.netlify.app/)**

## 📸 Demo & Screenshots

### 🎮 Try it Live!
Visit **[random-link.netlify.app](https://random-link.netlify.app/)** to see the application in action:

1. **Main Interface**: Links floating randomly with beautiful animations
2. **Category Filter**: Click category buttons to filter links
3. **Admin Panel**: Press `Ctrl+M` to access management features
4. **Mobile Responsive**: Works perfectly on phones and tablets

### 🎯 Key Features Demo:
- **Dynamic Positioning**: Links reposition every 8-12 seconds
- **Click Tracking**: Link sizes grow based on popularity
- **Real-time Management**: Add/delete links and categories instantly
- **Data Persistence**: All data saved in browser localStorage
- **Export/Import**: Backup and restore your link collections

## 🚀 Features

- **Link Management**: Add, delete, and categorize links
- **Dynamic Positioning**: Non-overlapping random link placement with collision detection
- **Click Tracking**: Track and visualize link popularity
- **Category System**: Organize links into colored categories
- **Data Persistence**: Client-side storage using localStorage
- **Data Export/Import**: Backup and restore functionality
- **Responsive Design**: Works on desktop and mobile devices
- **Vietnamese Interface**: Complete Vietnamese language support

## 🔧 Technologies

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Storage**: localStorage (client-side)
- **Deployment**: Netlify-ready static site
- **Responsive**: CSS Grid/Flexbox

## 📦 Deployment

### Netlify Deployment from GitHub

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Static site version"
   git branch -M main
   git remote add origin https://github.com/vietpham8/Random-Link-Display.git
   git push -u origin main
   ```

2. **Connect to Netlify**:
   - Go to [Netlify](https://netlify.com)
   - Click "New site from Git"
   - Choose GitHub and select your repository
   - Build settings are automatically configured via `netlify.toml`

3. **Build Configuration** (automatic via netlify.toml):
   - Build command: `echo 'Static site - no build required'`
   - Publish directory: `.` (root)
   - No build process needed - pure static files

### Manual Deployment

1. **Zip the files**:
   ```bash
   # Include only necessary files
   zip -r random-link-catalog.zip index.html netlify.toml README.md
   ```

2. **Upload to Netlify**:
   - Go to Netlify dashboard
   - Drag and drop the zip file
   - Site will be automatically deployed

## 🏗️ Architecture

### Static Site Structure
```
├── index.html          # Main application file
├── netlify.toml         # Netlify configuration
├── README.md           # Documentation
├── .gitignore          # Git ignore rules
└── CLAUDE.md           # Development documentation
```

### Data Storage
- **Client-side only**: Uses localStorage API
- **No server required**: Pure static site
- **Persistent data**: Survives browser sessions
- **Cross-tab sync**: Data updates across browser tabs

### Key Components

#### DataStore Class
- Manages all data operations
- localStorage integration
- Default data initialization
- CRUD operations for catalogues and links

#### UI Functions
- Dynamic DOM manipulation
- Collision detection for positioning
- Responsive layout management
- Admin panel with tabs

## 🎮 Usage

### Basic Operations
- **View Links**: Links display randomly positioned on screen
- **Click Links**: Opens in new tab and increments click counter
- **Switch Categories**: Use category buttons to filter links
- **Randomize**: Press Space or "Xáo trộn" button to reposition

### Admin Functions
- **Open Admin**: Ctrl+M or "Quản lý" button
- **Add Categories**: Create new link categories with colors
- **Add Links**: Add new links to categories
- **Manage Data**: Export, import, or clear all data
- **View Stats**: See usage statistics

### Keyboard Shortcuts
- **Ctrl + M**: Open admin panel
- **Escape**: Close admin panel
- **Space**: Randomize link positions

## 🔧 Configuration

### Netlify Configuration (netlify.toml)
- **Redirects**: SPA-style routing to index.html
- **Headers**: Security and caching headers
- **Build**: No build process required

### Default Data
Initial catalogues and links are created automatically:
- **Công cụ** (Tools): Google, GitHub
- **Giải trí** (Entertainment): YouTube
- **Học tập** (Learning): Educational resources

## 🛠️ Development

### Local Development
1. **Clone repository**:
   ```bash
   git clone <repository-url>
   cd random-link-catalog
   ```

2. **Serve locally**:
   ```bash
   # Using Python 3
   python -m http.server 8000

   # Using Node.js
   npx serve .

   # Using PHP
   php -S localhost:8000
   ```

3. **Open browser**: Visit `http://localhost:8000`

### Code Structure

#### JavaScript Classes
- **DataStore**: localStorage management
- **UI Functions**: DOM manipulation and events
- **Utility Functions**: Text truncation, positioning

#### CSS Features
- **CSS Grid/Flexbox**: Responsive layouts
- **CSS Animations**: Floating link animations
- **CSS Variables**: Consistent theming
- **Media Queries**: Mobile responsiveness

## 📊 Data Format

### Catalogue Object
```javascript
{
  id: number,
  name: string,
  description: string,
  color: string,
  created_at: string
}
```

### Link Object
```javascript
{
  id: number,
  catalogue_id: number,
  url: string,
  description: string,
  clicks: number,
  created_at: string
}
```

## 🔒 Security Features

- **Input Validation**: Client-side form validation
- **XSS Prevention**: Proper DOM manipulation
- **URL Validation**: Browser-native URL validation
- **Safe Data Handling**: JSON parsing with error handling

## 🌐 Browser Support

- **Modern Browsers**: Chrome 60+, Firefox 55+, Safari 12+, Edge 79+
- **Required APIs**: localStorage, fetch (not used but supported), ES6+
- **Mobile Support**: iOS Safari 12+, Chrome Mobile 60+

## 📱 Mobile Features

- **Responsive Design**: Adapts to screen sizes
- **Touch Events**: Mobile-friendly interactions
- **Viewport Optimization**: Proper mobile scaling
- **Performance**: Optimized for mobile networks

## 🚀 Performance Optimizations

- **No External Dependencies**: Pure vanilla JavaScript
- **Minimal File Size**: Single HTML file approach
- **Client-side Storage**: No server requests needed
- **Efficient Rendering**: RequestAnimationFrame for positioning
- **Lazy Loading**: On-demand DOM updates

## 🔄 Migration from Server Version

The static version maintains full compatibility with the original server-based application:

- **Data Structure**: Identical JSON format
- **Feature Parity**: All original features preserved
- **Export/Import**: Seamless data migration
- **UI/UX**: Identical user experience

## 📈 Future Enhancements

Potential improvements for the static version:

- **PWA Support**: Service worker for offline functionality
- **Sync Options**: Cloud storage integration
- **Themes**: Multiple color schemes
- **Keyboard Navigation**: Enhanced accessibility
- **Export Formats**: CSV, bookmark file support

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute
- 🐛 **Bug Reports**: Report issues or bugs
- 💡 **Feature Requests**: Suggest new features
- 🔧 **Code Contributions**: Submit pull requests
- 📖 **Documentation**: Improve docs and guides
- 🌐 **Translations**: Add more language support
- 🎨 **UI/UX**: Design improvements

### Development Process
1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Make your changes**: Follow existing code style
4. **Test thoroughly**: Ensure everything works
5. **Commit changes**: `git commit -m 'Add amazing feature'`
6. **Push to branch**: `git push origin feature/amazing-feature`
7. **Submit pull request**: Describe your changes

### Code Guidelines
- Use consistent indentation (2 spaces)
- Add comments for complex logic
- Test on multiple browsers
- Follow existing naming conventions
- Update documentation if needed

### Feature Ideas
- **PWA Support**: Service worker for offline functionality
- **Cloud Sync**: Google Drive/Dropbox integration
- **Themes**: Dark mode and color schemes
- **Import Formats**: Browser bookmarks, CSV support
- **Keyboard Navigation**: Enhanced accessibility
- **Link Preview**: Thumbnail generation
- **Categories**: Nested subcategories
- **Search**: Full-text search functionality

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ **Commercial use** - Use in commercial projects
- ✅ **Modification** - Modify and distribute
- ✅ **Distribution** - Share with others
- ✅ **Private use** - Use for personal projects
- ✅ **Patent use** - Use any patents in the project

### Requirements:
- 📝 **License notice** - Include copyright notice
- 📝 **Copyright notice** - Include original copyright

### Limitations:
- ❌ **No warranty** - Software provided as-is
- ❌ **No liability** - Authors not liable for damages

## 🏆 Credits

### Creator
- **Alan Pham** ([@vietpham8](https://github.com/vietpham8)) - Original creator and maintainer

### Technologies Used
- **HTML5/CSS3/JavaScript** - Core technologies
- **localStorage API** - Client-side storage
- **Netlify** - Hosting and deployment
- **GitHub** - Version control and collaboration

### Inspiration
This project was inspired by the need for a simple, fast, and beautiful bookmark manager that works entirely in the browser without requiring server infrastructure.

## 📞 Support & Community

### Getting Help
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/vietpham8/Random-Link-Display/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/vietpham8/Random-Link-Display/discussions)
- 📖 **Documentation**: See [CLAUDE.md](CLAUDE.md) for technical details
- 🚀 **Deployment**: Check [DEPLOY.md](DEPLOY.md) for deployment guides

### Community Guidelines
- Be respectful and inclusive
- Help others learn and grow
- Share knowledge and experiences
- Provide constructive feedback
- Follow the code of conduct

### Star History
If you find this project useful, please consider giving it a ⭐ on GitHub!

---

Made with ❤️ by [Alan Pham](https://github.com/vietpham8)

**Happy bookmarking! 🔗✨**