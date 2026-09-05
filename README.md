<div align="center">

# 🔮 NexaBot
### **Intelligent AI Customer Support System with Hybrid NLP Pipeline**

An enterprise-ready, local-first AI customer service chatbot powered by a hybrid architecture: **TF-IDF + Logistic Regression** for deterministic intent classification, **spaCy & Regex** for named entity recognition (NER), and **Google Gemini 2.5 Flash** for conversational fluency with a **100% offline fallback mode**.

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![spaCy](https://img.shields.io/badge/spaCy-3.7%2B-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-2.5%20Flash-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Offline Ready](https://img.shields.io/badge/Offline-100%25%20Functional-success?style=for-the-badge)](#-dual-engine-response-architecture)

<br/>

[🚀 Quick Start](#-quick-start) • [✨ Key Features](#-key-features) • [📸 Visual Showcase](#-visual-showcase) • [🧠 NLP Pipeline](#-nlp-architecture--pipeline) • [🎯 Supported Intents](#-supported-intents) • [🌐 API Docs](#-api-documentation) • [🛠️ Training & CLI](#-model-training--cli-testing)

---

</div>

<br/>

## 📸 Visual Showcase

### 1. 🌟 NexaBot Dashboard & Interactive Welcome Hub
Clean modern interface featuring quick-action topic pills, real-time status monitor, session persistence, and instant navigation.

<div align="center">
  <img src="assets/screenshots/nexabot-welcome.png" alt="NexaBot Welcome Hub & UI" width="95%" style="border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.5);" />
</div>

<br/>

### 2. ⚡ Live Conversation with Real-Time NLP Inspection
Full transparency into the machine learning pipeline: every bot response displays the **classified intent**, a **live confidence meter**, and **extracted entities** (such as Order IDs, dates, and products).

<div align="center">
  <img src="assets/screenshots/nexabot-chat-nlp.png" alt="NexaBot Live Chat & NLP Output" width="95%" style="border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.5);" />
</div>

<br/>

### 3. 🔐 User Authentication & Persistent Chat History
Local session management supporting guest browsing as well as registered customer accounts with PBKDF2 password encryption.

<div align="center">
  <img src="assets/screenshots/nexabot-auth-modal.png" alt="NexaBot Authentication Modal" width="95%" style="border-radius: 10px; box-shadow: 0 4px 20px rgba(0,0,0,0.5);" />
</div>

---

## 💡 Why NexaBot? (The Hybrid Advantage)

Most modern chatbots are either brittle rule-based decision trees or uncontrolled LLM wrappers. **NexaBot takes the best of both worlds**:

| Feature | Generic LLM Wrapper | Legacy Rule-Based Bot | 🔮 NexaBot Hybrid Pipeline |
|---|:---:|:---:|:---:|
| **Intent Determination** | Unpredictable / Black Box | Strict Pattern Matching | **Machine Learning (TF-IDF + LogReg)** |
| **Entity Extraction** | Prone to Hallucination | Manual String Parsing | **spaCy NER + Regex Validations** |
| **Response Latency** | High (1-4 seconds) | Ultra-fast (<10ms) | **Sub-millisecond ML + Fast Streaming** |
| **Offline Capability** | ❌ Fails without Internet | ✔️ Yes | **✔️ 100% Functional Local Fallback** |
| **Cost & Quota** | Expensive per token | Free | **Zero API cost in Demo / Local mode** |
| **Confidence Scoring** | ❌ Not available | ❌ Hardcoded | **✔️ Real-time % Probability Meter** |

---

## ✨ Key Features

* **🧠 Multi-Class Intent Classification**: Trained on 170+ real-world e-commerce & SaaS customer inquiries across 15 distinct intent categories.
* **📊 Transparent Confidence Meter**: Calculates and renders class probability scores for every prediction directly in the chat bubble.
* **🔍 Hybrid Named Entity Recognition (NER)**: Powered by spaCy's `en_core_web_sm` model (extracting dates, persons, orgs) combined with specialized regex patterns for tracking IDs (e.g., `#54321`) and emails.
* **🤖 Dual-Engine Response Generation**:
  * **Online Mode**: Integrates the official Google GenAI SDK (`gemini-2.5-flash`) anchored with system instructions to eliminate hallucinations.
  * **Local Offline Fallback**: Generates dynamic, entity-aware responses locally if no API key is set or when network is unavailable.
* **🎨 Glassmorphism Dark UI**: Built with pure HTML5, CSS3, and modern Vanilla JS. Includes glowing accents, responsive sidebar, auto-expanding textareas, typing animations, and 1-click clipboard copy.
* **💾 Local SQLite Session Storage**: Conversations and user accounts persist across browser sessions using SQLAlchemy 2.0.
* **🛡️ Security First**: Client-server API with PBKDF2-HMAC password hashing and signed session tokens.
* **⚡ Self-Contained**: Zero external database installations required (no Docker, Redis, or PostgreSQL needed).

---

## 🧠 NLP Architecture & Pipeline

NexaBot's pipeline processes customer inquiries in structured stages:

```
                          CUSTOMER INQUIRY
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │  Text Preprocessing   │
                     │  (Cleaning & Regex)   │
                     └───────────┬───────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │   TF-IDF Vectorizer   │
                     │  (ngram_range=(1,2))  │
                     └───────────┬───────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │  Logistic Regression  │
                     │   Intent Classifier   │
                     └───────────┬───────────┘
                                 │
                   ┌─────────────┴─────────────┐
                   ▼                           ▼
            Predicted Intent            Confidence Score
                   │                           │
                   └─────────────┬─────────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │   spaCy NER Engine    │
                     │ + Order/Email Regex   │
                     └───────────┬───────────┘
                                 │
                                 ▼
                     ┌───────────────────────┐
                     │  Response Dispatcher  │
                     └───────────┬───────────┘
                                 │
                ┌────────────────┴────────────────┐
                ▼                                 ▼
    [Gemini API Key Available]         [No Key / Offline Mode]
                │                                 │
     Google Gemini 2.5 Flash            Entity-Aware Local
       Anchored Generation                Fallback Engine
                │                                 │
                └────────────────┬────────────────┘
                                 │
                                 ▼
                       NEXABOT CHAT UI
          (Answer + Intent Badge + Confidence Bar + Entities)
```

---

## 🎯 Supported Intents

NexaBot accurately identifies 15 core customer support categories:

| Intent Tag | Category | Description | Sample Customer Query |
|---|---|---|---|
| `track_order` | Logistics | Inquiring about shipping or package whereabouts | *"Where is my order #54321?"* |
| `cancel_order` | Order Management | Requesting order cancellation before dispatch | *"I need to cancel order #98124 immediately"* |
| `return_order` | Returns | Returning items, return labels, and policy | *"The size doesn't fit, how can I return it?"* |
| `refund_status` | Billing | Checking pending refunds or money returns | *"When will my refund be credited to my bank?"* |
| `payment_issue` | Billing | Failed transactions, card declines, double charges | *"My card was charged twice during checkout"* |
| `shipping_information` | Logistics | Delivery times, shipping rates, and countries | *"How long does standard shipping take?"* |
| `product_information` | Sales | Specifications, compatibility, and availability | *"Does this model support 5G connectivity?"* |
| `account_issue` | Account | Locked accounts, profile updates, credentials | *"I am unable to sign into my dashboard"* |
| `password_reset` | Security | Password retrieval and OTP links | *"I forgot my password, how do I reset it?"* |
| `technical_issue` | Tech Support | Website bugs, broken buttons, checkout errors | *"The checkout page crashes when I click pay"* |
| `complaint` | Escalation | Escalating damaged items or poor experience | *"The package arrived completely broken and damaged"* |
| `contact_support` | Escalation | Requesting human agent or customer helpline | *"Can I speak to a live human agent?"* |
| `greeting` | Conversation | Starting conversation / greetings | *"Hi there, need some help!"* |
| `goodbye` | Conversation | Ending conversation / farewell | *"That will be all, thank you bye!"* |
| `thank_you` | Conversation | Gratitude and acknowledgement | *"Thank you so much, that answered my question!"* |

---

## 📂 Project Structure

```text
NexaBot/
├── assets/
│   └── screenshots/                # Application output visuals & UI demos
│       ├── nexabot-welcome.png     # Dashboard & welcome screen
│       ├── nexabot-chat-nlp.png    # Live chat with intent & entity badges
│       └── nexabot-auth-modal.png  # Account authentication modal
│
├── backend/
│   ├── main.py                     # FastAPI application entrypoint & static mounting
│   ├── api/                        # API route handlers
│   │   ├── chat.py                 # POST /api/chat & conversation management
│   │   ├── auth.py                 # POST /api/auth/register, login, me
│   │   ├── conversations.py        # GET /api/conversations/{id}
│   │   └── health.py               # GET /health diagnostic endpoint
│   ├── core/
│   │   ├── config.py               # Environment configuration via Pydantic
│   │   ├── database.py             # SQLite engine & session management
│   │   └── security.py             # PBKDF2 password hashing & token validation
│   ├── models/                     # SQLAlchemy ORM models (User, Message)
│   ├── schemas/                    # Pydantic validation schemas
│   └── services/                   # Core business logic
│       ├── intent_classifier.py    # TF-IDF + Logistic Regression inference
│       ├── ner_service.py          # spaCy NER + Regex entity extraction
│       ├── gemini_service.py       # Google GenAI integration & guardrails
│       └── response_service.py     # Pipeline coordinator & offline fallback
│
├── frontend/                       # Lightweight frontend (No Node.js needed)
│   ├── index.html                  # Responsive semantic HTML5 interface
│   ├── style.css                   # Glassmorphism dark aesthetic with animations
│   └── app.js                      # Chat state, asynchronous fetch, modal handlers
│
├── data/
│   ├── intents.json                # 15 intents with 170+ domain-specific samples
│   └── README.md                   # Dataset schema documentation
│
├── models/                         # Serialized ML artifacts
│   ├── intent_model.joblib         # Pre-trained Logistic Regression classifier
│   └── tfidf_vectorizer.joblib     # Pre-trained TF-IDF vectorizer
│
├── scripts/
│   ├── train_model.py              # Script to train & evaluate the ML model
│   └── test_model.py               # Interactive CLI testing tool
│
├── tests/                          # Pytest automated test suite
│   ├── test_health.py              # Health check tests
│   ├── test_nlp.py                 # Intent classification & NER tests
│   ├── test_chat.py                # Chat API endpoint tests
│   └── test_auth.py                # Auth & security tests
│
├── .env.example                    # Environment template
├── requirements.txt                # Reproducible Python dependencies
├── run.py                          # Cross-platform runner with pre-flight checks
├── setup.bat / run.bat             # 1-Click Windows execution scripts
├── setup.sh / run.sh               # 1-Click macOS / Linux execution scripts
└── LICENSE                         # MIT License
```

---

## ⚡ Quick Start

### 🪟 Windows (1-Click Run)

1. Clone or extract the repository:
   ```cmd
   git clone https://github.com/premthoke/NexaBot.git
   cd NexaBot
   ```
2. Run the automated installer:
   ```cmd
   .\setup.bat
   ```
   *(This creates a virtual environment, installs dependencies, and downloads the spaCy English model).*
3. (Optional) Open `.env` and paste your `GEMINI_API_KEY`.
4. Launch the application:
   ```cmd
   .\run.bat
   ```
5. Open your browser at **`http://localhost:8000`**.

---

### 🐧 Linux / 🍎 macOS

1. Clone the repository:
   ```bash
   git clone https://github.com/premthoke/NexaBot.git
   cd NexaBot
   ```
2. Make scripts executable and run setup:
   ```bash
   chmod +x setup.sh run.sh
   ./setup.sh
   ```
3. (Optional) Configure your `.env` file:
   ```bash
   cp .env.example .env
   # Add your GEMINI_API_KEY if desired
   ```
4. Start the server:
   ```bash
   ./run.sh
   # Or directly: python run.py
   ```
5. Visit **`http://localhost:8000`**.

---

## ⚙️ Configuration (`.env`)

A default `.env` is created automatically from `.env.example`:

```env
# Google Gemini API Key (Optional — leave empty for 100% offline Local NLP Demo)
GEMINI_API_KEY=your_gemini_api_key_here

# Model identifier
GEMINI_MODEL=gemini-2.5-flash

# SQLite Database Location
DATABASE_URL=sqlite:///./nexabot.db

# Application Secret Key
SECRET_KEY=nexabot_production_secret_key

# Host & Port
HOST=127.0.0.1
PORT=8000
```

> 💡 **Offline Guarantee**: If no `GEMINI_API_KEY` is provided, NexaBot runs effortlessly in **Local NLP Demo Mode** using its entity-aware fallback engine. No credit card, no internet connection, and no API limits!

---

## 🛠️ Model Training & CLI Testing

### Train or Retrain the Model
You can add your own custom intents or training examples to [`data/intents.json`](data/intents.json) and retrain the classifier:

```bash
python scripts/train_model.py
```
*Output displays dataset statistics, train/test split accuracy, and automatically serializes the model to `models/`.*

### Test via Terminal CLI
Quickly verify intent classification and entity extraction directly in your command line:

```bash
# Test a custom phrase
python scripts/test_model.py "Where is package #98234?"

# Launch interactive CLI mode
python scripts/test_model.py
```

---

## 🧪 Automated Testing

Run the comprehensive test suite with `pytest`:

```bash
pytest -v
```

Tests cover:
* ✅ System `/health` endpoint & configuration
* ✅ TF-IDF & Logistic Regression classification accuracy
* ✅ spaCy & Regex entity extraction
* ✅ Chat API request/response validation
* ✅ Authentication, PBKDF2 hashing, and token verification

---

## 🌐 API Documentation

FastAPI provides automated interactive API documentation accessible while NexaBot is running:

* **Interactive Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc Documentation**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Core Endpoints

| Method | Endpoint | Description | Sample Payload |
|---|---|---|---|
| `GET` | `/health` | System status, active AI mode, and model availability | *None* |
| `POST` | `/api/chat` | Main NLP query pipeline (Intent, Confidence, Entities, Reply) | `{"message": "Track order #54321"}` |
| `POST` | `/api/conversations/new` | Initializes a new conversation session | `{"session_id": "optional-uuid"}` |
| `GET` | `/api/conversations/{session_id}` | Retrieves history for a given session | *None* |
| `POST` | `/api/auth/register` | Registers a new customer account | `{"email": "...", "password": "...", "full_name": "..."}` |
| `POST` | `/api/auth/login` | Authenticates customer credentials | `{"email": "...", "password": "..."}` |
| `GET` | `/api/auth/me` | Returns profile of currently authenticated user | *Bearer Token Header* |

---

## 👨‍💻 Author

**Prem Thoke**
* GitHub: [@premthoke](https://github.com/premthoke)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
