from odoo import api, models, _

class ReportTask(models.AbstractModel):

    _name = 'report.task_manager.report_task'
    _description = 'Task Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        tasks = self.env['task_manager.task'].search([])
        data = dict(data or {})
        data.update({
            'tasks' : tasks
        })
        return data