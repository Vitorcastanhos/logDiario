"""Module providing a function printing python version."""
from datetime import datetime
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.firestore import SERVER_TIMESTAMP
from email_sender import enviar_email_log
from whatsapp_sender import enviar_whatsapp_log

# Inicializar Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Título da página
st.set_page_config(page_title="Log Diário", layout="centered")
st.title("📋 Registro de Log Diário de Trabalho")

# Formulário de entrada
with st.form("log_form"):
    nome = st.text_input("Nome do colaborador")
    setor = st.text_input("Setor/Projeto")
    turno_inicio = st.time_input("Início do turno")
    turno_fim = st.time_input("Fim do turno")
    atividades = st.text_area("Descreva as atividades do dia")
    data_hoje = datetime.now().strftime("%Y-%m-%d")

    enviar = st.form_submit_button("Salvar Log")

# Processar envio somente após clicar em "Salvar Log"
if enviar:
    if nome and atividades:
        log_data = {
            "nome": nome,
            "setor": setor,
            "turno_inicio": str(turno_inicio),
            "turno_fim": str(turno_fim),
            "atividades": atividades,
            "data": data_hoje,
            "hora_envio": datetime.now().strftime("%H:%M:%S"),
            "criado_em": SERVER_TIMESTAMP,
        }

        db.collection("logs_diarios").add(log_data)
        st.success("✅ Log salvo com sucesso!")

        # Guardar dados na sessão para possível envio posterior
        st.session_state["log_para_envio"] = log_data
    else:
        st.warning("⚠️ Preencha ao menos seu nome e as atividades.")

# Exibir botão de envio manual após salvar
if "log_para_envio" in st.session_state:
    st.markdown("---")
    st.subheader("📤 Enviar Log Manualmente")

    if st.button("Enviar log por Email e WhatsApp"):
        log = st.session_state["log_para_envio"]

        assunto = f"Log diário – {log['nome']} ({log['data']})"
        corpo = f"""
        Nome: {log['nome']}
        Setor: {log['setor']}
        Turno: {log['turno_inicio']} às {log['turno_fim']}
        Data: {log['data']}
        Atividades:
        {log['atividades']}
        """

        mensagem = f"""
        📋 Log diário – {log['nome']} ({log['data']})
        🕘 Turno: {log['turno_inicio']} às {log['turno_fim']}
        📌 Setor: {log['setor']}
        📝 {log['atividades']}
        """

        destinatario = "castanhostecnologia@gmail.com"
        numero_destino = "+5571982746619"

        enviar_email_log(destinatario, assunto, corpo)
        enviar_whatsapp_log(numero_destino, mensagem)

        st.success("✅ Log enviado com sucesso!")

# Visualização de logs salvos
st.markdown("---")
st.header("📄 Logs Registrados")

logs_ref = db.collection("logs_diarios").order_by(
    "criado_em", direction=firestore.Query.DESCENDING)
logs = logs_ref.stream()

for log in logs:
    data = log.to_dict()
    st.markdown(f"""
    **👤 Nome:** {data.get('nome')}
    **📅 Data:** {data.get('data')} | **🕘 Início:** {data.get('turno_inicio')} | **🕔 Fim:** {data.get('turno_fim')}
    **📌 Setor:** {data.get('setor')}
    **📝 Atividades:** {data.get('atividades')}
    ---
    """)
