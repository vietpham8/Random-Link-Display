#!/usr/bin/env python3
"""
Export SQLite database to JSON format for static site import
Converts catalogues and links from database.db to JSON format compatible with localStorage
"""

import sqlite3
import json
import os
from datetime import datetime

def connect_database():
    """Connect to SQLite database"""
    db_path = "database.db"
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file {db_path} not found!")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Enable column access by name
    return conn

def export_catalogues(conn):
    """Export all catalogues from database"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM catalogues ORDER BY created_at ASC")

    catalogues = []
    for row in cursor.fetchall():
        catalogue = {
            "id": row["id"],
            "name": row["name"],
            "description": row["description"],
            "color": row["color"],
            "created_at": row["created_at"]
        }
        catalogues.append(catalogue)

    print(f"[OK] Exported {len(catalogues)} catalogues")
    return catalogues

def export_links(conn):
    """Export all links from database"""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM links ORDER BY created_at ASC")

    links = []
    for row in cursor.fetchall():
        link = {
            "id": row["id"],
            "catalogue_id": row["catalogue_id"],
            "url": row["url"],
            "description": row["description"],
            "clicks": row["clicks"],
            "created_at": row["created_at"]
        }
        links.append(link)

    print(f"[OK] Exported {len(links)} links")
    return links

def create_export_data(catalogues, links):
    """Create export data structure compatible with static site"""
    export_data = {
        "catalogues": catalogues,
        "links": links,
        "export_info": {
            "exported_at": datetime.now().isoformat(),
            "source": "SQLite database.db",
            "format_version": "2.0",
            "total_catalogues": len(catalogues),
            "total_links": len(links)
        }
    }
    return export_data

def save_json_file(data, filename="sqlite_export.json"):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    file_size = os.path.getsize(filename)
    print(f"[OK] Saved to {filename} ({file_size:,} bytes)")
    return filename

def print_summary(catalogues, links):
    """Print export summary"""
    print("\n" + "="*50)
    print("EXPORT SUMMARY")
    print("="*50)

    print(f"Catalogues: {len(catalogues)}")
    for cat in catalogues:
        link_count = len([l for l in links if l['catalogue_id'] == cat['id']])
        print(f"   - {cat['name']}: {link_count} links")

    print(f"\nTotal Links: {len(links)}")
    total_clicks = sum(link['clicks'] for link in links)
    print(f"Total Clicks: {total_clicks}")

    if links:
        most_clicked = max(links, key=lambda x: x['clicks'])
        print(f"Most clicked: {most_clicked['description']} ({most_clicked['clicks']} clicks)")

def verify_data_integrity(catalogues, links):
    """Verify data integrity and relationships"""
    print("\nVerifying data integrity...")

    # Check if all links have valid catalogue_id
    catalogue_ids = {cat['id'] for cat in catalogues}
    orphaned_links = [link for link in links if link['catalogue_id'] not in catalogue_ids]

    if orphaned_links:
        print(f"[WARNING] {len(orphaned_links)} links have invalid catalogue_id")
        for link in orphaned_links:
            print(f"   - Link ID {link['id']}: '{link['description']}' -> catalogue_id {link['catalogue_id']}")
    else:
        print("[OK] All links have valid catalogue references")

    # Check for duplicate URLs
    urls = [link['url'] for link in links]
    if len(urls) != len(set(urls)):
        print("[WARNING] Duplicate URLs found")
    else:
        print("[OK] All URLs are unique")

def main():
    """Main export function"""
    print("Starting SQLite to JSON export...")
    print("-" * 40)

    try:
        # Connect to database
        print("Connecting to database...")
        conn = connect_database()

        # Export data
        print("Exporting catalogues...")
        catalogues = export_catalogues(conn)

        print("Exporting links...")
        links = export_links(conn)

        # Verify data
        verify_data_integrity(catalogues, links)

        # Create export structure
        print("Creating export data...")
        export_data = create_export_data(catalogues, links)

        # Save to JSON file
        print("Saving JSON file...")
        filename = save_json_file(export_data)

        # Print summary
        print_summary(catalogues, links)

        print("\n" + "="*50)
        print("EXPORT COMPLETED SUCCESSFULLY!")
        print("="*50)
        print(f"File created: {filename}")
        print("Next steps:")
        print("   1. Open your static site in browser")
        print("   2. Go to Admin panel (Ctrl+M)")
        print("   3. Data tab -> 'Nhap du lieu'")
        print(f"   4. Select {filename}")
        print("   5. All your data will be imported!")

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed")

    return True

if __name__ == "__main__":
    main()