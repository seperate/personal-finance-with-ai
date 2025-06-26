from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List
from datetime import datetime
from decimal import Decimal


# User schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class User(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Category schemas
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    parent_id: Optional[int] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    color: Optional[str] = None
    icon: Optional[str] = None
    parent_id: Optional[int] = None


class Category(CategoryBase):
    id: int
    is_system: bool
    user_id: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Transaction schemas
class TransactionBase(BaseModel):
    date: datetime
    description: str
    amount: Decimal
    balance: Optional[Decimal] = None
    merchant_name: Optional[str] = None
    transaction_type: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None


class TransactionCreate(TransactionBase):
    category_id: Optional[int] = None
    uploaded_file_id: Optional[int] = None


class TransactionUpdate(BaseModel):
    date: Optional[datetime] = None
    description: Optional[str] = None
    amount: Optional[Decimal] = None
    balance: Optional[Decimal] = None
    category_id: Optional[int] = None
    merchant_name: Optional[str] = None
    transaction_type: Optional[str] = None
    reference_number: Optional[str] = None
    notes: Optional[str] = None
    is_verified: Optional[bool] = None


class Transaction(TransactionBase):
    id: int
    user_id: str
    category_id: Optional[int] = None
    uploaded_file_id: Optional[int] = None
    confidence_score: Optional[Decimal] = None
    is_verified: bool
    is_duplicate: bool
    duplicate_of: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Budget schemas
class BudgetBase(BaseModel):
    name: str
    description: Optional[str] = None
    amount: Decimal
    period: str
    start_date: datetime
    end_date: Optional[datetime] = None
    alert_threshold: Optional[Decimal] = Decimal('0.80')

    @validator('period')
    def validate_period(cls, v):
        allowed_periods = ['daily', 'weekly', 'monthly', 'quarterly', 'yearly']
        if v not in allowed_periods:
            raise ValueError(f'Period must be one of: {", ".join(allowed_periods)}')
        return v


class BudgetCreate(BudgetBase):
    category_id: Optional[int] = None


class BudgetUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[Decimal] = None
    period: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    category_id: Optional[int] = None
    is_active: Optional[bool] = None
    alert_threshold: Optional[Decimal] = None


class Budget(BudgetBase):
    id: int
    user_id: str
    category_id: Optional[int] = None
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Uploaded File schemas
class UploadedFileBase(BaseModel):
    original_filename: str
    file_size: int


class UploadedFileCreate(UploadedFileBase):
    filename: str
    file_path: str


class UploadedFileUpdate(BaseModel):
    status: Optional[str] = None
    processing_result: Optional[str] = None
    error_message: Optional[str] = None


class UploadedFile(UploadedFileBase):
    id: int
    user_id: str
    filename: str
    file_path: str
    status: str
    processing_result: Optional[str] = None
    error_message: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# AI Insight schemas
class AIInsightBase(BaseModel):
    insight_type: str
    title: str
    content: str
    data: Optional[str] = None
    confidence_score: Optional[Decimal] = None


class AIInsightCreate(AIInsightBase):
    expires_at: Optional[datetime] = None


class AIInsightUpdate(BaseModel):
    is_read: Optional[bool] = None
    is_dismissed: Optional[bool] = None


class AIInsight(AIInsightBase):
    id: int
    user_id: str
    is_read: bool
    is_dismissed: bool
    created_at: datetime
    expires_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# API Response schemas
class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[dict] = None


class PaginationMeta(BaseModel):
    page: int
    page_size: int
    total_pages: int
    total_items: int
    has_next: bool
    has_prev: bool


class PaginatedResponse(BaseModel):
    success: bool
    data: List[dict]
    meta: PaginationMeta


# PDF Processing schemas
class PDFProcessingStatus(BaseModel):
    file_id: int
    status: str
    progress: Optional[int] = None  # 0-100
    message: Optional[str] = None
    extracted_transactions: Optional[int] = None


class TransactionPreview(BaseModel):
    """For displaying transactions before user confirmation"""
    date: datetime
    description: str
    amount: Decimal
    balance: Optional[Decimal] = None
    merchant_name: Optional[str] = None
    transaction_type: Optional[str] = None
    confidence_score: Optional[Decimal] = None
    suggested_category: Optional[str] = None


class PDFProcessingResult(BaseModel):
    file_id: int
    status: str
    total_transactions: int
    transactions: List[TransactionPreview]
    processing_time: Optional[float] = None
    errors: Optional[List[str]] = None


# Authentication schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
    user_id: Optional[str] = None


# Dashboard schemas
class DashboardSummary(BaseModel):
    total_income: Decimal
    total_expenses: Decimal
    net_income: Decimal
    transactions_count: int
    active_budgets: int
    budget_utilization: Optional[Decimal] = None
    top_categories: List[dict]
    recent_transactions: List[Transaction]
