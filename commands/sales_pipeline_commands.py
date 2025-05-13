from .base_command import BaseCommand

class AddOpportunityCommand(BaseCommand):
    def __init__(self, controller):
        self.controller = controller  # Recebe o SalesPipelineController

    def execute(self):
        contact = self.controller.contact_controller.search_contact()
        if not contact:
            self.controller.view.show_message('Contact not found. Add the contact first.')
            return
        
        try:
            opportunity_data = self.controller.view.get_opportunity_info()
            value = float(opportunity_data['value'])
            stage = opportunity_data['stage']
            
            opportunity = self.controller.repository.add(contact, value, stage)
            self.controller.view.show_message(f'Opportunity added successfully! ID: {opportunity.id}')
        except ValueError as e:
            self.controller.view.show_message(f'ERROR: {str(e)}')


class ListOpportunitiesCommand(BaseCommand):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        opportunities = self.controller.repository.get_all()
        self.controller.view.show_opportunities(opportunities)


class UpdateOpportunityStageCommand(BaseCommand):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        opportunity_id = self.controller.view.get_opportunity_id()
        if not opportunity_id:
            return
        
        if opportunity_id in self.controller.repository.opportunities:
            new_stage = self.controller.view.get_new_stage()
            if self.controller.repository.update_stage(opportunity_id, new_stage):
                self.controller.view.show_message('Opportunity updated successfully!')
            else:
                self.controller.view.show_message('Failed to update opportunity.')
        else:
            self.controller.view.show_message('Opportunity not found.')


class RemoveOpportunityCommand(BaseCommand):
    def __init__(self, controller):
        self.controller = controller

    def execute(self):
        opportunity_id = self.controller.view.get_opportunity_id()
        if not opportunity_id:
            return
        
        if self.controller.repository.remove(opportunity_id):
            self.controller.view.show_message('Opportunity removed successfully.')
        else:
            self.controller.view.show_message('Opportunity not found.')