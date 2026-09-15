from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import Lead, Business, Agent
from app.schema.agent import AgentCreate
from app.schema.business import BusinessCreate
from app.schema.lead import LeadCreate

app = FastAPI(
    title="AI Voice Agent Platform",
    description="AI-powered lead communication platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "AI Voice Agent Platform API",
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }

@app.get("/leads")
async def get_leads(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Lead)
    )

    leads = result.scalars().all()

    return leads

@app.post("/leads")
async def create_lead(
    lead_data: LeadCreate,
    db: AsyncSession = Depends(get_db),
):
    lead = Lead(
        business_id=lead_data.business_id,
        name=lead_data.name,
        phone=lead_data.phone,
        email=lead_data.email,
        notes=lead_data.notes,
    )

    db.add(lead)

    await db.commit()
    await db.refresh(lead)

    return lead

@app.post("/businesses")
async def create_business(
    business_data: BusinessCreate,
    db: AsyncSession = Depends(get_db),
):
    business = Business(
        name=business_data.name,
        email=business_data.email,
        phone=business_data.phone,
    )

    db.add(business)

    await db.commit()
    await db.refresh(business)

    return business

@app.post("/agents")
async def create_agent(
    agent_data: AgentCreate,
    db: AsyncSession = Depends(get_db),
):
    agent = Agent(
        business_id=agent_data.business_id,
        name=agent_data.name,
        system_prompt=agent_data.system_prompt,
        greeting=agent_data.greeting,
        voice=agent_data.voice,
    )

    db.add(agent)

    await db.commit()
    await db.refresh(agent)

    return agent

@app.get("/agents")
async def get_agents(
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Agent)
    )

    agents = result.scalars().all()

    return agents