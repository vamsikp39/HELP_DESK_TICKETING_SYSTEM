from flask import Blueprint, render_template, request, redirect, url_for
from .models import Ticket
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

@bp.route('/add', methods=['POST'])
def add_ticket():
    title = request.form['title']
    description = request.form['description']
    new_ticket = Ticket(title=title, description=description)
    db.session.add(new_ticket)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/close/<int:id>')
def close_ticket(id):
    ticket = Ticket.query.get(id)
    if ticket:
        ticket.status = "Closed"
        db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:id>')
def delete_ticket(id):
    ticket = Ticket.query.get(id)
    if ticket:
        db.session.delete(ticket)
        db.session.commit()
    return redirect(url_for('main.index'))