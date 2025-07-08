# 📋 Log Diário de Trabalho

Este é um aplicativo web construído com [Streamlit](https://streamlit.io/) para registrar e acompanhar logs diários de atividades de trabalho. Os dados são armazenados no Firebase Firestore e podem ser enviados automaticamente por **Email** e **WhatsApp** de forma manual e segura.

## 🚀 Funcionalidades

- Registro de atividades diárias com nome, setor, horário e descrição.
- Armazenamento dos registros no Firebase Firestore.
- Visualização cronológica dos logs já registrados.
- Envio manual dos logs por:

  - 📧 Email (via Gmail)
  - 🛋 WhatsApp (via [UltraMsg](https://ultramsg.com))

## 🗄️ Interface

![Interface do app](https://via.placeholder.com/800x400.png?text=Exemplo+da+Interface+do+App)

---

## 🛠️ Tecnologias utilizadas

- [Python 3.11+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [Firestore](https://firebase.google.com/docs/firestore)
- [yagmail](https://github.com/kootenpv/yagmail) (para envio de email)
- [UltraMsg API](https://docs.ultramsg.com/) (para envio de WhatsApp)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/log-diario.git
cd log-diario
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Adicione seus arquivos sensíveis (não enviar ao Git):

- `firebase-key.json` (chave do seu projeto Firebase)
- `email_sender.py` (contendo seu email e senha de app)
- `whatsapp_sender.py` (com as credenciais da UltraMsg)

5. Execute a aplicação:

```bash
streamlit run app.py
```

---

## 🔐 Segurança

Adicione um arquivo `.gitignore` com:

```gitignore
firebase-key.json
email_sender.py
whatsapp_sender.py
.env
```

Nunca envie suas credenciais para repositórios públicos.

---

## 📧 Exemplo de envio por email

```python
from email_sender import enviar_email_log

enviar_email_log(
    destinatario="exemplo@empresa.com",
    assunto="Log diário – Fulano",
    corpo="Atividades realizadas hoje: ..."
)
```

---

## ☑️ To-do Futuro

- [ ] Autenticação por usuário (login)
- [ ] Painel de administração com filtros
- [ ] Agendamento automático do envio dos logs
- [ ] Exportação para Excel

---

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou pull requests. Sugestões são bem-vindas!

---

## 📝 Licença

Este projeto é de uso interno e pode ser adaptado conforme as necessidades da sua equipe.

---
