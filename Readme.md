Esse projeto tem as instruções de uso e funcionamento do sistema de atendimento de clinica médica .

 Flask para backend e API com HTML/CSS e JavaScript pra frontend

patient_controller.py para funcionalidades de pacientes (como cadastrar e buscar pacientes).
appointment_controller.py para gerenciar os atendimentos (como criar e atualizar status de atendimentos).
consultation_controller.py para manipular as consultas (como marcar, buscar e cancelar consultas).

*/MENU - CADASTRO
• Clínica
• Usuário
• Controle de acesso permissão de usuário
• Paciente
• Empresa
• Feriado
• Medicamento
• Modelo de impressões (Atestado, encaminhamentos, laudos etc)
• Modelo de histórico clínico
• Modelo de conduta médica
• Modelo de hipótese diagnóstica
• Profissional
• Tipo de atendimento
• Funcionário
• Grupo de exames
• Exames
• Convênio
• Despesas/Conta a pagar


MENU - ATENDIMENTO
• Recepção
• Consulta Médica
• Histórico do paciente
• atestado
• Receituário especial
• Impressão de receita oftalmologista (Novo)

MENU - AGENDAMENTO
• Controle de agendamento e retorno

MENU - EXAMES
• Orçamento de exames
• exame beta HCG

MENU - FINANCEIRO
• Lançar contas a pagar
• Baixa de contas a pagar
• Lançamento de parcelas
• Baixa de contas a receber

MENU - RECIBO
• Emissão de recibo avulso

MENU - RELATÓRIOS
• Aniversariantes
• Exames
• Atendimento por profissional
• Atendimento por empresa
• Atendimento por paciente
• Atendimento por convênio
• Atendimento por tipo de consulta
• Financeiro: Fluxo de caixa
• Financeiro: Contas a pagar
• Financeiro: Forma de pagamento
• Financeiro: Contas a receber
• Financeiro: Contas recebidas
• Financeiro: Pacientes em atraso/*

create (POST): já implementado.
get_all (GET): para listar todos os registros de cada tipo (agendamento, consulta, etc.).
get_by_id (GET): para retornar dados específicos de um único agendamento, consulta, etc., usando o ID.

