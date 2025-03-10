from flask import Blueprint, redirect, request, url_for
from flask import render_template

from .db import get_db

bp = Blueprint("dashboard", __name__)

def get_groupped_links():
    db = get_db()
    groups = db.execute('SELECT * FROM groups').fetchall()
    data = []
    for group in groups:
        items = db.execute('SELECT * FROM links WHERE group_id = ?', (group['id'],)).fetchall()
        data.append({
            'id': group['id'],
            'name': group['group_name'],
            'icon': group['icon'],
            'items': [{'name': item['name'], 'url': item['link'], 'logo': item['logo']} for item in items]
        })
    return {'groups': data}

@bp.route("/")
def index():
    """Show all the posts, most recent first."""
    return render_template('index.html', data=get_groupped_links())

@bp.route('/add_link', methods=['GET', 'POST'])
def add_link():
    conn = get_db()
    if request.method == 'POST':
        group_id = request.form.get('group')
        new_group_name = request.form.get('new_group_name')
        new_group_icon = request.form.get('new_group_icon')
        link_name = request.form.get('link_name')
        link_url = request.form.get('link_url')
        link_logo = request.form.get('link_logo')

        if group_id:
            group_id = int(group_id)
        else:
            conn.execute('INSERT INTO groups (group_name, icon) VALUES (?, ?)', (new_group_name, new_group_icon))
            conn.commit()
            group_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]

        conn.execute('INSERT INTO links (name, link, logo, group_id) VALUES (?, ?, ?, ?)',
                     (link_name, link_url, link_logo, group_id))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard.index'))

    groups = conn.execute('SELECT * FROM groups').fetchall()
    conn.close()
    return render_template('add_link.html', groups=groups)
