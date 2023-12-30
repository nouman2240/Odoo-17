# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

class TMTasks(models.Model):
    _name = 'task_manager.task'
    _description = 'Task Management'
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    deadline = fields.Date(string='Deadline')
    completed = fields.Boolean(string='Completed')
    days_until_deadline = fields.Integer(string='Days Until Deadline', compute='_compute_days_until_deadline')


    @api.depends('deadline')
    def _compute_days_until_deadline(self):
        for task in self:
            if task.deadline:
                today_date = datetime.now().date()
                delta = task.deadline - today_date
                task.days_until_deadline =  delta.days
            else:
                task.days_until_deadline = 0
    
    def mark_task_completed(self):
        self.completed = True
    