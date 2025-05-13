from commands.sales_pipeline_commands import (
    AddOpportunityCommand,
    ListOpportunitiesCommand,
    UpdateOpportunityStageCommand,
    RemoveOpportunityCommand
)

class SalesPipelineController:
    def __init__(self, view, sales_pipeline_repository, contact_controller):
        self.view = view
        self.repository = sales_pipeline_repository
        self.contact_controller = contact_controller
        
        # Inicializa os comandos
        self.commands = {
            'add': AddOpportunityCommand(self),
            'list': ListOpportunitiesCommand(self),
            'update': UpdateOpportunityStageCommand(self),
            'remove': RemoveOpportunityCommand(self),
        }

    def execute_command(self, command_name):
        """Executa um comando pelo nome."""
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            self.view.show_message('Invalid command.')