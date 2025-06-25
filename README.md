# Personal Finance AI Web Application

An AI-powered personal finance management platform that processes PDF bank statements using OCR/AI technology to extract transaction data, providing intelligent insights and budget management.

## 🚀 Tech Stack

- **Frontend:** React with TypeScript
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL via Supabase
- **Authentication:** Supabase Auth
- **Deployment:** Railway.app
- **AI/OCR:** Advanced OCR technology for PDF processing

## 📋 Features

### Core Features
- **PDF Bank Statement Processing**: Upload and extract transaction data from PDF statements
- **AI-Powered Transaction Extraction**: Advanced OCR and AI models for accurate data extraction
- **Manual Data Correction**: Edit and validate extracted transactions before saving
- **Smart Categorization**: Automatic transaction categorization with AI
- **Duplicate Detection**: Intelligent detection across multiple uploads
- **Budget Management**: Create, track, and manage budgets with real-time insights
- **Financial Analytics**: Comprehensive reports and visualizations
- **Dashboard**: Real-time financial overview with AI-generated insights

## 🏗️ Project Structure

```
personal-finance-with-ai/
├── frontend/                 # React TypeScript frontend
├── backend/                  # FastAPI backend
│   ├── app/
│   │   ├── routers/         # API routes
│   │   ├── models/          # Database models
│   │   ├── schemas/         # Pydantic schemas
│   │   └── services/        # Business logic
│   ├── main.py             # FastAPI application entry point
│   └── requirements.txt    # Python dependencies
├── docs/                   # Documentation
├── scripts/               # Utility scripts
├── PRD.md                # Product Requirements Document
├── PROJECT_TASKS.md      # Detailed project tasks and progress
└── README.md            # This file
```

## 🚦 Getting Started

### Prerequisites
- Node.js (v18 or higher)
- Python 3.9+
- Git

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📚 Documentation

- [Product Requirements Document (PRD)](./PRD.md)
- [Project Tasks & Progress](./PROJECT_TASKS.md)

## 🔄 Development Workflow

1. **Phase 1**: Foundation Setup ✅
   - Project structure and environment
   - Basic authentication system
   - Database schema design

2. **Phase 2**: Core Features (In Progress)
   - PDF processing infrastructure
   - Transaction management system
   - Dashboard implementation

3. **Phase 3**: Advanced Features
   - Budget management
   - Reports & analytics
   - Data visualization

4. **Phase 4**: AI Integration
   - Machine learning models
   - Financial insights
   - Recommendation engine

5. **Phase 5**: Polish & Deployment
   - Performance optimization
   - Security audit
   - Production deployment

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Railway.app](https://railway.app) - Deployment platform
- [Supabase](https://supabase.com) - Database and authentication
- [FastAPI](https://fastapi.tiangolo.com) - Backend framework
- [React](https://reactjs.org) - Frontend framework

---

**Status**: 🚧 In Development  
**Last Updated**: June 25, 2025
